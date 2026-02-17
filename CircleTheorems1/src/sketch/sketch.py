from manim import *
from MF_Tools import *

class Sketch_Animation(Scene):
    def construct(self):
        circle = Circle(radius=2, color=BLUE)
        
        # Трекер для значения alpha (от 0 до 1)
        alpha1_tracker = ValueTracker(0.30)
        line1_length = ValueTracker(5)
        alpha2_tracker = ValueTracker(0.55)
        line2_length = ValueTracker(5)
        
        def get_ticks(start, end, n=1):
            mid = (start + end) / 2
            vec = end - start
            if np.linalg.norm(vec) < 0.1: return VGroup() # Скрываем, если точки совпали
            
            angle = angle_of_vector(vec)
            ticks = VGroup()
            spacing = 0.1
            
            for i in range(n):
                offset = (i - (n - 1) / 2) * spacing
                pos = mid + normalize(vec) * offset
                tick = Line(start=DOWN*0.1, end=UP*0.1, color=WHITE).rotate(angle + PI).move_to(pos)
                ticks.add(tick)
            return ticks
        
        
        def get_line1():
            return TangentLine(
                circle,
                alpha1_tracker.get_value(),
                length=line1_length.get_value(),
                color=YELLOW
            )

        def get_line2():
            return TangentLine(
                circle,
                alpha2_tracker.get_value(),
                length=line2_length.get_value(),
                color=YELLOW
            )
        def get_intersection_dot():
            # Получаем актуальные координаты концов линий
            # line1 и line2 - это Mobject, у них есть методы get_start() и get_end()
            curr_line1 = get_line1()
            curr_line2 = get_line2()
            
            # Функция line_intersection вычисляет точку пересечения двух прямых,
            # проходящих через заданные пары точек.
            point = line_intersection(
                [curr_line1.get_start(), curr_line1.get_end()],
                [curr_line2.get_start(), curr_line2.get_end()]
            )
            
            return Dot(point, color=RED, radius=0.1)

        intersection_dot = always_redraw(get_intersection_dot)
        # Касательная, которая обновляется при изменении трекера
        tangent = always_redraw(get_line1)
        
        tangent2 = always_redraw(get_line2)
        
        # Точка касания (опционально, для наглядности)
        dot = always_redraw(lambda: Dot(
            circle.point_from_proportion(alpha1_tracker.get_value()), 
            color=RED
        ))
        
        dot2 = always_redraw(lambda: Dot(
            circle.point_from_proportion(alpha2_tracker.get_value()), 
            color=RED
        ))
        
        
        
        ticks1 = always_redraw(lambda: get_ticks(
            dot.get_center(),      # От точки на окружности
            intersection_dot.get_center(), # До точки пересечения
            n=1
        ))

        ticks2 = always_redraw(lambda: get_ticks(
            dot2.get_center(), 
            intersection_dot.get_center(), 
            n=1
        ))

        self.play(
            Write(circle), 
            run_time=2   
        )
        self.play(
            Write(tangent),
            Write(tangent2),
            Write(intersection_dot),
            Write(dot), 
            Write(dot2),
            run_time=0.5
        )
        
        self.play(
            Write(ticks1),
            Write(ticks2),
            
            run_time=0.3
        )
        # Анимация изменения значения alpha от 0 до 1 за 5 секунд
        self.play(
            alpha1_tracker.animate.set_value(0.42),
            alpha2_tracker.animate.set_value(0.68),
            
            line2_length.animate.set_value(6),
            line1_length.animate.set_value(6),
            
            run_time=2, 
            rate_func=smooth
        )
        
        self.wait(0.4)
        
        self.play(
            alpha1_tracker.animate.set_value(0.87),
            alpha2_tracker.animate.set_value(1),
            
            run_time=2, 
            rate_func=smooth
        )
        
        alpha2_tracker.set_value(0),
        
        self.play(
            alpha1_tracker.animate.set_value(0.8),
            alpha2_tracker.animate.set_value(0.2),
            line2_length.animate.set_value(15),
            line1_length.animate.set_value(15),
            
            run_time=2, 
            rate_func=smooth
        )
        
        self.wait()
        
