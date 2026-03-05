from manim import *
from MF_Tools import *


# Angle Inscribed in a Semicircle (Thales's Theorem): An angle inscribed in a semicircle is a right angle (90 degrees).

def begining_of_part_three(self):
    # Tex objects
    text_obj1 = Text(
        "Angle Inscribed in a Semicircle (Thales's Theorem):",
        font_size=36
    )
    
    text_obj2 = Text(
        "An angle inscribed in a semicircle is a right angle (90 degrees).",
        font_size=26
    )
    
    text_obj1.next_to(text_obj2, UP, buff=0.2)
    
    
    # Write
    self.play(
        Write(text_obj1),
        run_time=1.5
    )
    
    self.play(
        FadeIn(text_obj2),
        run_time=1
    )
    
    self.wait(2)


    # FadeOut
    self.play(
        FadeOut(text_obj1),
        FadeOut(text_obj2),
        run_time=1.5
    )
    self.wait()


def part_three_main(self):
    # values & circle
    a_angle = ValueTracker(PI)
    b_angle = ValueTracker(2 * PI)
    c_angle = ValueTracker(PI / 4)
    
    circle = Circle(radius=2.6, color=BLUE)
    
    
    # Dots
    dot_a = always_redraw(lambda: Dot(circle.point_at_angle(a_angle.get_value()), color=YELLOW))
    dot_b = always_redraw(lambda: Dot(circle.point_at_angle(b_angle.get_value()), color=YELLOW))
    dot_c = always_redraw(lambda: Dot(circle.point_at_angle(c_angle.get_value()), color=GREEN))
    
    
    # Str dots
    dot_a_tex = always_redraw(
        lambda: Tex("A")
        .next_to(dot_a, LEFT, buff=0.2)
        .set_color(WHITE)
    )
    dot_b_tex = always_redraw(
        lambda: Tex("B")
        .next_to(dot_b, RIGHT, buff=0.2)
        .set_color(WHITE)
    )
    dot_c_tex = always_redraw(
        lambda: Tex("C")
        .next_to(dot_c, UP, buff=0.2)
        .set_color(WHITE)
    )
    
    
    # Lines
    line_ab = always_redraw(lambda: Line(dot_a.get_center(), dot_b.get_center()))
    
    line_ca = always_redraw(lambda: Line(dot_c.get_center(), dot_a.get_center()))
    line_cb = always_redraw(lambda: Line(dot_c.get_center(), dot_b.get_center()))
    
    
    # Inscribed angle & value
    def get_angle_val():
        arc_diff = abs((a_angle.get_value() % (2 * PI)) - (b_angle.get_value() % (2 * PI)))
        
        minor_arc = min(arc_diff, 2 * PI - arc_diff)
        
        return minor_arc / 2 / DEGREES
    
    
    acb_rightAngle = always_redraw(
        lambda: RightAngle(line_ca, line_cb, length=0.3, color=ORANGE, other_angle=False)
    )
    
    acb_val = always_redraw(
        lambda: MathTex(rf"{get_angle_val():.1f}^\circ")
        .next_to(acb_rightAngle, DOWN, buff=0.3)
        .set_color(WHITE)
        .set_stroke(color=BLACK, width=9, background=True)
    )
    
    
    # Render the sketch
    self.play(
        Create(circle), 
        
        Create(dot_a), 
        FadeIn(dot_a_tex),
        Create(dot_b), 
        FadeIn(dot_b_tex),
        Create(dot_c),
        FadeIn(dot_c_tex)
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
    
    self.wait()
    
    
    # Animation
    self.play(
        c_angle.animate.set_value(2*PI/3),
        run_time=1.5, 
        rate_func=smooth
    )
    
    self.wait(0.5)
    
    self.play(
        c_angle.animate.set_value(PI/4),
        run_time=1.5, 
        rate_func=smooth
    )
    
    self.wait()
    
    
    # FadeOut
    self.play(
        FadeOut(circle), 
        FadeOut(dot_a), 
        FadeOut(dot_b), 
        FadeOut(dot_c),
        
        FadeOut(dot_a_tex),
        FadeOut(dot_b_tex),
        FadeOut(dot_c_tex),  
        
        FadeOut(line_ab), 
        FadeOut(line_ca), 
        FadeOut(line_cb),
                   
        FadeOut(acb_rightAngle),
        FadeOut(acb_val)
    )
    
    self.wait()