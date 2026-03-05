from manim import *
from MF_Tools import *


# Angle Inscribed in a Semicircle (Thales's Theorem): An angle inscribed in a semicircle is a right angle (90 degrees).

def begining_of_part_three(self):
    text_obj1 = Text(
        "Angle Inscribed in a Semicircle (Thales's Theorem):",
        font_size=36
    )
    
    text_obj2 = Text(
        "An angle inscribed in a semicircle is a right angle (90 degrees).",
        font_size=26
    )
    text_obj1.next_to(text_obj2, UP, buff=0.2)
    
    
    self.play(
        Write(text_obj1),
        run_time=2
    )
    
    self.play(
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


def part_three_main(self):
    circle = Circle(radius=2.6, color=BLUE)
    
    a_angle = ValueTracker(PI)
    dot_a = always_redraw(lambda: Dot(circle.point_at_angle(a_angle.get_value()), color=YELLOW))
    
    b_angle = ValueTracker(2 * PI)
    dot_b = always_redraw(lambda: Dot(circle.point_at_angle(b_angle.get_value()), color=YELLOW))


    c_angle = ValueTracker(PI / 4)
    dot_c = always_redraw(lambda: Dot(circle.point_at_angle(c_angle.get_value()), color=GREEN))
    
    line_ab = always_redraw(lambda: Line(dot_a.get_center(), dot_b.get_center()))
    
    line_ca = always_redraw(lambda: Line(dot_c.get_center(), dot_a.get_center()))
    line_cb = always_redraw(lambda: Line(dot_c.get_center(), dot_b.get_center()))
    
    
    acb_rightAngle = always_redraw(
        lambda: RightAngle(line_ca, line_cb, length=0.5, color=ORANGE, other_angle=False)
    )
    
    acb_val = always_redraw(
        lambda: MathTex(rf"{(b_angle.get_value() - a_angle.get_value()) / 2 / DEGREES:.1f}^\circ")
        .next_to(acb_rightAngle, DOWN, buff=0.3)
        .set_color(WHITE)
    )
    
    self.play(
        Create(circle), 
        Create(dot_a), 
        Create(dot_b), 
        Create(dot_c)
    )
    
    self.play(
        Create(line_ca), 
        Create(line_cb),
        Create(line_ab)
    )
    
    self.play(
        FadeIn(acb_rightAngle),
        FadeIn(acb_val)
    )
    
    self.play(
        c_angle.animate.set_value(2*PI/3),
        run_time=1, 
        rate_func=smooth
    )
    self.wait(0.2)
    self.play(
        c_angle.animate.set_value(PI/4),
        run_time=1, 
        rate_func=smooth
    )
    
    self.wait()
    
    self.play(
        FadeOut(circle), 
        FadeOut(dot_a), 
        FadeOut(dot_b), 
        FadeOut(dot_c),
        
        FadeOut(acb_rightAngle),
        FadeOut(acb_val),

        FadeOut(line_ab), 
        FadeOut(line_ca), 
        FadeOut(line_cb)
    )
    
    self.wait()