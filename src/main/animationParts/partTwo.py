from manim import *
from MF_Tools import *


# Angles Subtended by the Same Arc: Inscribed angles that subtend the same arc are congruent.

def begining_of_part_two(self):
    # Tex objects
    text_obj1 = Text(
        "Angles Subtended by the Same Arc:",
        font_size=36
    )
    
    text_obj2 = Text(
        "Inscribed angles that subtend the same arc are congruent.",
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


def part_two_main(self):
    # values & circle
    a_angle = ValueTracker(4 * PI / 3)
    b_angle = ValueTracker(5 * PI / 3)
    c_angle = ValueTracker(5 * PI / 6)
    d_angle = ValueTracker(PI / 2)
    e_angle = ValueTracker(PI / 6)
    
    circle = Circle(radius=2.6, color=BLUE)
    
    
    # Dots
    center = Dot(ORIGIN, color=BLACK)
    
    dot_a = always_redraw(lambda: Dot(circle.point_at_angle(a_angle.get_value()), color=YELLOW))
    dot_b = always_redraw(lambda: Dot(circle.point_at_angle(b_angle.get_value()), color=YELLOW))
    dot_c = always_redraw(lambda: Dot(circle.point_at_angle(c_angle.get_value()), color=GREEN))
    dot_d = always_redraw(lambda: Dot(circle.point_at_angle(d_angle.get_value()), color=GREEN))
    dot_e = always_redraw(lambda: Dot(circle.point_at_angle(e_angle.get_value()), color=GREEN))
    
    
    # Str dots
    dot_a_tex = always_redraw(
        lambda: Tex("A")
        .next_to(dot_a, DOWN+LEFT, buff=0.2)
        .set_color(WHITE)
    )
    dot_b_tex = always_redraw(
        lambda: Tex("B")
        .next_to(dot_b, DOWN+RIGHT, buff=0.2)
        .set_color(WHITE)
    )
    dot_c_tex = always_redraw(
        lambda: Tex("C")
        .next_to(dot_c, UP+LEFT, buff=0.2)
        .set_color(WHITE)
    )
    dot_d_tex = always_redraw(
        lambda: Tex("D")
        .next_to(dot_d, UP, buff=0.2)
        .set_color(WHITE)
    )
    dot_e_tex = always_redraw(
        lambda: Tex("E")
        .next_to(dot_e, UP+RIGHT, buff=0.2)
        .set_color(WHITE)
    )


    # Lines
    line_oa = always_redraw(lambda: Line(ORIGIN, dot_a.get_center()).set_color(BLACK))
    line_ob = always_redraw(lambda: Line(ORIGIN, dot_b.get_center()).set_color(BLACK))
    
    line_ca = always_redraw(lambda: Line(dot_c.get_center(), dot_a.get_center()))
    line_cb = always_redraw(lambda: Line(dot_c.get_center(), dot_b.get_center()))
    
    line_da = always_redraw(lambda: Line(dot_d.get_center(), dot_a.get_center()))
    line_db = always_redraw(lambda: Line(dot_d.get_center(), dot_b.get_center()))
    
    line_ea = always_redraw(lambda: Line(dot_e.get_center(), dot_a.get_center()))
    line_eb = always_redraw(lambda: Line(dot_e.get_center(), dot_b.get_center()))
    
    
    # Underlines
    underline_acb = Underline(acb_val[0], buff=0.1, color=YELLOW)
    underline_adb = Underline(adb_val[0], buff=0.1, color=YELLOW)
    underline_aeb = Underline(aeb_val[0], buff=0.1, color=YELLOW)
    
    
    # Center angle & value
    central_angle = always_redraw(
        lambda: Angle(line_oa, line_ob, radius=2.6, color=BLUE, other_angle=False)
    )
    
    central_val = always_redraw(
        lambda: MathTex(rf"{(b_angle.get_value() - a_angle.get_value()) / DEGREES:.1f}^\circ")
        .next_to(central_angle, DOWN, buff=0.3)
        .set_color(WHITE)
    )
    
    
    # Inscribed angle & value
    def get_angle_val():
        arc_diff = abs((a_angle.get_value() % (2 * PI)) - (b_angle.get_value() % (2 * PI)))
        
        minor_arc = min(arc_diff, 2 * PI - arc_diff)
        
        return minor_arc / 2 / DEGREES
    
    
    acb_angle = always_redraw(
        lambda: Angle(line_ca, line_cb, radius=0.8, color=ORANGE, other_angle=False)
    )
    
    acb_val = always_redraw(
        lambda: MathTex(rf"{get_angle_val():.1f}^\circ")
        .next_to(acb_angle, DOWN, buff=0.3)
        .set_color(WHITE)
        .set_stroke(color=BLACK, width=9, background=True)
    )
    
    
    adb_angle = always_redraw(
        lambda: Angle(line_da, line_db, radius=0.8, color=ORANGE, other_angle=False)
    )
    
    adb_val = always_redraw(
        lambda: MathTex(rf"{get_angle_val():.1f}^\circ")
        .next_to(adb_angle, DOWN, buff=0.3)
        .set_color(WHITE)
        .set_stroke(color=BLACK, width=9, background=True)
    )
    
    
    aeb_angle = always_redraw(
        lambda: Angle(line_ea, line_eb, radius=0.8, color=ORANGE, other_angle=False)
    )
    
    aeb_val = always_redraw(
        lambda: MathTex(rf"{get_angle_val():.1f}^\circ")
        .next_to(aeb_angle, DOWN, buff=0.3)
        .set_color(WHITE)
        .set_stroke(color=BLACK, width=9, background=True)
    )


    # Render the sketch
    self.add(
        center, 
        line_oa, 
        line_ob
    )
    
    self.play(
        Create(circle), 
        
        Create(dot_a), 
        FadeIn(dot_a_tex),
        Create(dot_b), 
        FadeIn(dot_b_tex),
        Create(dot_c),
        FadeIn(dot_c_tex),
        Create(dot_d),
        FadeIn(dot_d_tex),
        Create(dot_e),
        FadeIn(dot_e_tex),
    )
    
    self.play(
        FadeIn(central_angle), 
        FadeIn(central_val)
    )        
    
    self.play(
        Create(line_ca), 
        Create(line_cb),
        Create(line_da), 
        Create(line_db),
        Create(line_ea), 
        Create(line_eb)
    )

    self.play(
        FadeIn(acb_angle), 
        FadeIn(acb_val),
        FadeIn(adb_angle), 
        FadeIn(adb_val),
        FadeIn(aeb_angle), 
        FadeIn(aeb_val)
    ) 
    
    self.wait()


    # Animation
    self.play(
        Create(underline_acb),
        Create(underline_adb),
        Create(underline_aeb)
    )
    
    self.play(
        a_angle.animate.set_value(5 * PI / 4), 
        b_angle.animate.set_value(7 * PI / 4), 
        run_time=4, 
        rate_func=smooth
    )
    
    self.wait(0.5)
    
    self.play(
        a_angle.animate.set_value(4 * PI / 3), 
        b_angle.animate.set_value(5 * PI / 3), 
        run_time=4, 
        rate_func=smooth
    )
    
    self.wait()
    
    
    # FadeOut
    self.play(
        FadeOut(center), 
        FadeOut(line_oa), 
        FadeOut(line_ob),

        FadeOut(circle), 
        FadeOut(dot_a), 
        FadeOut(dot_b), 
        FadeOut(dot_c),
        FadeOut(dot_d),
        FadeOut(dot_e),
        
        FadeOut(dot_a_tex),
        FadeOut(dot_b_tex),
        FadeOut(dot_c_tex),
        FadeOut(dot_d_tex),
        FadeOut(dot_e_tex),
        
        FadeOut(underline_acb),
        FadeOut(underline_adb),
        FadeOut(underline_aeb),        
        
        FadeOut(central_angle), 
        FadeOut(central_val),

        FadeOut(line_ca), 
        FadeOut(line_cb),
        FadeOut(line_da), 
        FadeOut(line_db),
        FadeOut(line_ea), 
        FadeOut(line_eb),

        FadeOut(acb_angle), 
        FadeOut(acb_val),
        FadeOut(adb_angle), 
        FadeOut(adb_val),
        FadeOut(aeb_angle), 
        FadeOut(aeb_val)
    )
    
    self.wait()