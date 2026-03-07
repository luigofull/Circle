from manim import *


# Inscribed Angle Theorem: The measure of an inscribed angle is half the measure of its intercepted arc or the central angle that subtends the same arc.


def part_one(self):
    # === Text animation ===
    text_obj1_big = Text(
        "Inscribed Angle Theorem:",
        font_size=38,
        font="Arial",
    )
    
    text_obj1_small = Text(
        "Inscribed Angle Theorem:",
        font_size=30,
        font="Arial",
    )
    
    paragraph_obj = Paragraph(
        "The measure of an inscribed",
        "angle is half the measure of",
        "its intercepted arc or the central",
        "anglethat subtends the same arc.",
        line_spacing=0.6,
        font_size=26,
        alignment="left",
        font="Arial",
    )    
    
    
    text_obj1_small.shift(UP *2.5)
    
    self.play(
        Write(text_obj1_big),
        run_time=1.5
    )
    
    self.play(Transform(text_obj1_big, text_obj1_small))
    self.remove(text_obj1_big)
    self.play(text_obj1_small.animate.shift(RIGHT*3.5))

    self.play(FadeIn(paragraph_obj.next_to(text_obj1_small, DOWN, buff=0.3)))
    
    underline1 = Underline(paragraph_obj[1][7:11], color=YELLOW)
    underline2 = Underline(paragraph_obj[2][3:30], color=GREEN, buff=-0.01)
    underline3 = Underline(paragraph_obj[3], color=GREEN, buff=-0.01)
    
    self.play(Create(underline1), Create(underline2))
    self.play(Create(underline3))
    
    
    
    # === Circle animation ===
    
    # valueTrackers & circle
    a_angle = ValueTracker(PI / 6)
    b_angle = ValueTracker(5 * PI / 3)
    c_angle = ValueTracker(5 * PI / 6)
    
    circle = Circle(radius=2.6, color=BLUE)
    
    
    # Dots
    center = Dot(ORIGIN, color='#111111')
    
    dot_a = always_redraw(lambda: Dot(circle.point_at_angle(a_angle.get_value()), color=YELLOW))
    dot_b = always_redraw(lambda: Dot(circle.point_at_angle(b_angle.get_value()), color=YELLOW))
    dot_c = always_redraw(lambda: Dot(circle.point_at_angle(c_angle.get_value()), color=GREEN))
    

    # Lines
    line_oa = always_redraw(lambda: Line(center.get_center(), dot_a.get_center()).set_color('#111111'))
    line_ob = always_redraw(lambda: Line(center.get_center(), dot_b.get_center()).set_color('#111111'))
    
    line_ca = always_redraw(lambda: Line(dot_c.get_center(), dot_a.get_center()))
    line_cb = always_redraw(lambda: Line(dot_c.get_center(), dot_b.get_center()))
    
    
    # Center angle & value
    def get_central_angle_val():
        arc_diff = abs((a_angle.get_value() % (2 * PI)) - (b_angle.get_value() % (2 * PI)))
        
        minor_arc = min(arc_diff, 2 * PI - arc_diff)
        
        return minor_arc / DEGREES
    
    
    central_angle = always_redraw(
        lambda: Angle(line_ob, line_oa, radius=2.6, color=BLUE, other_angle=False)
    )
    
    central_val = always_redraw(
        lambda: MathTex(rf"{get_central_angle_val():.1f}^\circ")
        .move_to(
            central_angle.point_from_proportion(0.5) + 
            normalize(central_angle.point_from_proportion(0.5) - center.get_center()) * 0.7
        )
        .set_color(WHITE)
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
        .move_to(
            acb_angle.point_from_proportion(0.5) + 
            normalize(acb_angle.point_from_proportion(0.5) - dot_c.get_center()) * 0.7
        )
        .set_color(WHITE)
        .set_stroke(color='#111111', width=9, background=True)
    )
    
    
    # Underlines
    underline_acb = always_redraw(
        lambda: Underline(
            acb_val[0], 
            buff=0.1, 
            color=YELLOW
        )
        .set_stroke(color='#111111', width=9, background=True)
    )
    underline_aob = always_redraw(
        lambda: Underline(
            central_val[0], 
            buff=0.1, 
            color=GREEN
        )
        .set_stroke(color='#111111', width=9, background=True)
    )
    
    
    
    # VGoups
    static_objects = VGroup(center, line_oa, line_ob)
    dinamic_objects = VGroup(
        circle,
        dot_a,
        dot_b,
        dot_c
    )
    central_objects = VGroup(central_angle, central_val, underline_aob)
    line_objects = VGroup(line_ca, line_cb)
    angle_objects = VGroup(acb_angle, acb_val, underline_acb)
    
    
    # shift left
    static_objects.shift(LEFT * 3.5)
    dinamic_objects.shift(LEFT * 3.5)
    central_objects.shift(LEFT * 3.5)
    line_objects.shift(LEFT * 3.5)
    angle_objects.shift(LEFT * 3.5)
    
    
    
    # Render the sketch
    self.add(
        center, 
        line_oa, 
        line_ob
    )
    
    self.play(
        Create(circle), 
        
        Create(dot_a),
        Create(dot_b), 
        Create(dot_c),
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
        FadeIn(acb_angle), 
        FadeIn(acb_val)
    ) 
    
    self.wait()


    # Animation
    self.play(
        Create(underline_acb),
        Create(underline_aob)
    )
    
    self.play(
        c_angle.animate.set_value(7 * PI / 6), 
        run_time=2, 
        rate_func=there_and_back
    )
    
    self.play(
        b_angle.animate.set_value(4 * PI / 3), 
        run_time=2, 
        rate_func=there_and_back
    )
    
    self.play(
        c_angle.animate.set_value(PI / 2),
        b_angle.animate.set_value(3 * PI / 2),
        run_time=2, 
        rate_func=smooth
    )
    
    self.play(
        b_angle.animate.set_value(7 * PI / 4),
        run_time=1, 
        rate_func=smooth
    )
    
    self.play(
        c_angle.animate.set_value(5 * PI / 6),
        b_angle.animate.set_value(5 * PI / 3),
        run_time=1, 
        rate_func=smooth
    )
    
    self.wait(3)
    

    # FadeOut
    self.play(
        FadeOut(text_obj1_small),
        FadeOut(paragraph_obj),
        
        FadeOut(center), 
        FadeOut(line_oa), 
        FadeOut(line_ob),

        FadeOut(circle), 
        FadeOut(dot_a), 
        FadeOut(dot_b), 
        FadeOut(dot_c),
        
        FadeOut(underline1),
        FadeOut(underline2),
        FadeOut(underline3),
        FadeOut(underline_acb),
        FadeOut(underline_aob),

        FadeOut(central_angle), 
        FadeOut(central_val),

        FadeOut(line_ca), 
        FadeOut(line_cb),

        FadeOut(acb_angle), 
        FadeOut(acb_val)
    )
    
    self.wait()