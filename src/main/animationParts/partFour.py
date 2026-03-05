from manim import *
from MF_Tools import *


# Alternate Segment Theorem (Tangent-Chord Theorem): The angle between a tangent and a chord through the point of contact is equal to the angle in the alternate segment.

def begining_of_part_four(self):
    # Tex objects
    text_obj1 = Text(
        "Alternate Segment Theorem (Tangent-Chord Theorem):",
        font_size=32
    )
    
    text_obj2 = Text(
        "The angle between a tangent and a chord through the\npoint of contact is equal to the angle in the alternate segment.",
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


def part_four_main(self):
    # values & circle
    a_angle = ValueTracker(PI /3)
    b_angle = ValueTracker(7 * PI / 4)
    c_angle = ValueTracker(5 * PI / 6)
    
    circle = Circle(radius=2.6, color=BLUE)
    
    
    # Dots
    dot_a = always_redraw(lambda: Dot(circle.point_at_angle(a_angle.get_value()), color=YELLOW))
    dot_b = always_redraw(lambda: Dot(circle.point_at_angle(b_angle.get_value()), color=YELLOW))
    dot_c = always_redraw(lambda: Dot(circle.point_at_angle(c_angle.get_value()), color=GREEN))
    
    
    # Str dots
    dot_a_tex = always_redraw(
        lambda: Tex("A")
        .next_to(dot_a, UP+RIGHT, buff=0.1)
        .set_color(WHITE)
    )
    dot_b_tex = always_redraw(
        lambda: Tex("B")
        .next_to(dot_b, DOWN+RIGHT, buff=0.1)
        .set_color(WHITE)
    )
    dot_c_tex = always_redraw(
        lambda: Tex("C")
        .next_to(dot_c, UP+LEFT, buff=0.1)
        .set_color(WHITE)
    )
    
    
    # Tangen
    tangent = always_redraw(
        lambda: TangentLine(
            circle,
            alpha=(b_angle.get_value() % (2 * PI)) / (2 * PI),
            length=5,
            color=RED
        )
    )
    
    
    # Lines
    line_ab = always_redraw(lambda: Line(dot_a.get_center(), dot_b.get_center()))
    line_ba = always_redraw(lambda: Line(dot_b.get_center(), dot_a.get_center(), color=BLACK))
    
    line_ca = always_redraw(lambda: Line(dot_c.get_center(), dot_a.get_center()))
    line_cb = always_redraw(lambda: Line(dot_c.get_center(), dot_b.get_center()))
    
    
    # Underlines
    underline_acb = always_redraw(
        lambda: Underline(acb_val[0], buff=0.1, color=YELLOW)
        .set_stroke(color=BLACK, width=9, background=True)
    )
    underline_tba = always_redraw(
        lambda: Underline(tba_val[0], buff=0.1, color=YELLOW)
        .set_stroke(color=BLACK, width=9, background=True)
    )
    
    
    # Inscribed angle & value
    def get_angle_val():
        arc_diff = abs((a_angle.get_value() % (2 * PI)) - (b_angle.get_value() % (2 * PI)))
        
        minor_arc = min(arc_diff, 2 * PI - arc_diff)
        
        return minor_arc / 2 / DEGREES    
    

    acb_angle = always_redraw(
        lambda: Angle(line_cb, line_ca, radius=0.8, color=ORANGE, other_angle=False)
    )
    
    acb_val = always_redraw(
        lambda: MathTex(rf"{get_angle_val():.1f}^\circ")
        .next_to(acb_angle, RIGHT, buff=0.3)
        .set_color(WHITE)
        .set_stroke(color=BLACK, width=9, background=True)
    )
    
    
    tba_angle = always_redraw(
        lambda: Angle(tangent, line_ba, radius=0.8, color=ORANGE, other_angle=False)
    )
    
    tba_val = always_redraw(
        lambda: MathTex(rf"{get_angle_val():.1f}^\circ")
        .next_to(tba_angle, UP, buff=0.3)
        .set_color(WHITE)
        .set_stroke(color=BLACK, width=9, background=True)
    )
    
    
    # Render the sketch
    self.add(line_ba)
    
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
        Create(line_ab),
    )
    
    self.play(
        Create(tangent)
    )
    
    self.play(
        FadeIn(acb_angle),
        FadeIn(acb_val),
        FadeIn(tba_angle),
        FadeIn(tba_val)
    )
    
    self.wait()


    # Animation
    self.play(
        Create(underline_acb),
        Create(underline_tba)
    )
    
    self.play(
        b_angle.animate.set_value(4*PI/3),
        run_time=3, 
        rate_func=there_and_back
    )
    
    self.wait()
    

    # FadeOut
    self.play(
        FadeOut(line_ba),
        
        FadeOut(circle),
        
        FadeOut(dot_a),
        FadeOut(dot_b),
        FadeOut(dot_c),
        
        FadeOut(tangent),
        
        FadeOut(dot_a_tex),
        FadeOut(dot_b_tex),
        FadeOut(dot_c_tex),
        
        FadeOut(underline_acb),
        FadeOut(underline_tba),

        FadeOut(line_ab),
        FadeOut(line_ca),
        FadeOut(line_cb),
        
        FadeOut(acb_angle),
        FadeOut(acb_val),
        FadeOut(tba_angle),
        FadeOut(tba_val),
        

    )
    
    self.wait()