from manim import *
from MF_Tools import *


# Inscribed Angle Theorem: The measure of an inscribed angle is half the measure of its intercepted arc or the central angle that subtends the same arc.


def begining_of_animation(self):
    text_obj1 = Text(
        "Inscribed Angle Theorem:",
        font_size=36
    )
    
    text_obj2 = Text(
        "The measure of an inscribed angle is half the measure\nof it's intercepted arc or the central angle that subtends\nthe same arc.",
        font_size=26
    )
    text_obj1.next_to(text_obj2, UP, buff=0.2)
    
    self.play(
        Write(text_obj1),
        Write(text_obj2),
        run_time=2
    )
    self.wait()

    self.play(
        FadeOut(text_obj1),
        FadeOut(text_obj2),
        run_time=1.5
    )
    self.wait()


def part_one_main(self):
    circle = Circle(radius=2.5, color=BLUE)
    center = Dot(ORIGIN, color=BLACK)
    
    a_angle = ValueTracker(5 * PI / 4)
    dot_a = always_redraw(lambda: Dot(circle.point_at_angle(a_angle.get_value()), color=YELLOW))
    
    b_angle = ValueTracker(7 * PI / 4)
    dot_b = always_redraw(lambda: Dot(circle.point_at_angle(b_angle.get_value()), color=YELLOW))

    c_angle = ValueTracker(3 * PI / 4)
    dot_c = always_redraw(lambda: Dot(circle.point_at_angle(c_angle.get_value()), color=GREEN))

    # Градус Дуги
    line_oa = always_redraw(lambda: Line(ORIGIN, dot_a.get_center()).set_color(BLACK))
    line_ob = always_redraw(lambda: Line(ORIGIN, dot_b.get_center()).set_color(BLACK))
    
    central_angle = always_redraw(
        lambda: Angle(line_oa, line_ob, radius=2.5, color=BLUE, other_angle=False)
    )
    
    central_val = always_redraw(
        lambda: MathTex(rf"{(b_angle.get_value() - a_angle.get_value()) / DEGREES:.1f}^\circ")
        .next_to(central_angle, DOWN, buff=0.3)
        .set_color(WHITE)
    )
    
    # Вписанный угол и его линии
    line_ca = always_redraw(lambda: Line(dot_c.get_center(), dot_a.get_center()))
    line_cb = always_redraw(lambda: Line(dot_c.get_center(), dot_b.get_center()))
    
    inscribed_angle = always_redraw(
        lambda: Angle(line_ca, line_cb, radius=0.8, color=ORANGE, other_angle=False)
    )
    
    inscribed_val = always_redraw(
        lambda: MathTex(rf"{(b_angle.get_value() - a_angle.get_value()) / 2 / DEGREES:.1f}^\circ")
        .next_to(inscribed_angle, DOWN, buff=0.3)
        .set_color(WHITE)
    )


    # Render the Circle
    self.add(
        center, 
        line_oa, 
        line_ob
    )
    
    self.play(
        Create(circle), 
        Create(dot_a), 
        Create(dot_b), 
        Create(dot_c)
    )
    
    self.play(
        FadeIn(central_angle), 
        FadeIn(central_val)
    )        
    
    self.play(
        Create(line_ca), 
        Create(line_cb)
    )

    self.play(
        FadeIn(inscribed_angle), 
        FadeIn(inscribed_val)
    ) 
    
    self.wait()

    # Animate Points
    self.play(
        c_angle.animate.set_value(PI / 3), 
        run_time=2, 
        rate_func=there_and_back
    )
    
    self.play(
        b_angle.animate.set_value(2 * PI), 
        run_time=2, 
        rate_func=there_and_back
    )
    
    self.play(
        c_angle.animate.set_value(PI / 2),
        b_angle.animate.set_value(5 * PI / 3),
        run_time=2, 
        rate_func=smooth
    )
    self.play(
        b_angle.animate.set_value(7 * PI / 4),
        run_time=1, 
        rate_func=smooth
    )
    
    self.wait()