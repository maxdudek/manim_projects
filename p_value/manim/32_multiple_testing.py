from manim import *
from probability_mobjects import *
from dudek_utils import *

class _32_multiple_testing(Scene):
    def construct(self):

        alex = GenericImageMobject("assets/alex.webp").scale_to_fit_height(2.8).move_to((-5,1.7,0))

        alex_devil = GenericImageMobject("assets/alex_devil.png").scale_to_fit_height(3.5).move_to((-5,-1.8,0))

        steve = GenericImageMobject("assets/steve.png").scale_to_fit_height(2.8).set_y(alex.get_y()).shift(RIGHT*0.2)

        steve_48 = GenericImageMobject("assets/steve_48.png", scale_to_resolution=2160).set_y(alex_devil.get_y()).align_to(steve, LEFT)

        arrow1 = Arrow(
            alex.get_edge_center(RIGHT),
            steve.get_edge_center(LEFT),
            stroke_width=7
        )

        n_1_txt = MathTex("m = 1").next_to(arrow1, UP)

        arrow2 = Arrow(
            alex_devil.get_edge_center(RIGHT),
            steve_48.get_edge_center(LEFT),
            stroke_width=7
        )

        n_48_txt = MathTex("m = 48").next_to(arrow2, UP)

        eq = VGroup()

        eq.add( # 0
            Tex(r"(Assuming $H_0$ is true)", font_size=36).align_on_border(UP).set_x(4)
        )

        eq.add( # 1
            Tex(r"$P$(at least one FP)", font_size=44).next_to(eq[-1], DOWN, buff=0.4).align_to(eq[-1], LEFT)
        )
        eq[-1][0][-3:-1].set_color(RED)

        eq.add( # 2
            MathTex(r"= 1 - P(\text{all TN})", font_size=44).next_to(eq[-1], DOWN, buff=0.2).shift(RIGHT*0.5)
        )
        eq[-1][0][-3:-1].set_color(GREEN)

        eq.add( # 3
            MathTex(r"= 1 - (1-\alpha)^m", font_size=44).next_to(eq[-1], DOWN, buff=0.2).align_to(eq[-1], LEFT)
        )
        eq[-1][0][6].set_color(PROB_PINK)

        eq.add( # 4
            MathTex(r"= 1 - (0.95)^{48}", font_size=44).next_to(eq[-1], DOWN, buff=0.2).align_to(eq[-1], LEFT)
        )
        eq[-1][0][4:8].set_color(PROB_PINK)

        eq.add( # 5
            MathTex(r"= 91\%", font_size=44).next_to(eq[-1], DOWN, buff=0.2).align_to(eq[-1], LEFT)
        )

        random_sampling_txt = Text("random sampling", font_size=32, color=GREEN).next_to(n_1_txt, UP).set_y(0)
        random_sampling_cross = Line(
            random_sampling_txt.get_edge_center(LEFT)+LEFT*0.15,
            random_sampling_txt.get_edge_center(RIGHT)+RIGHT*0.15,
            color=RED,
            stroke_width = 5,
        )

        luckiest_txt = Text("only show luckiest player", font_size=24, color=RED).next_to(steve_48, DOWN).shift(LEFT*1.5)
        red_circle = Circle(0.25, color=RED).move_to(steve_48.get_corner(DL)).shift(UP*0.2+RIGHT*0.14)

        multiple_testing_txt = Text("multiple testing", font_size=40, slant=ITALIC).next_to(steve_48, RIGHT, buff=0.5).shift(UP*0.5)
        p_hacking_txt = Text("p-hacking", font_size=40, slant=ITALIC).next_to(steve_48, RIGHT, buff=0.5).shift(DOWN*0.5)

        #################################################################
        # Animation (1)                                                 #
        #################################################################
        # self.add(NumberPlane(
        #     background_line_style={
        #         "stroke_width": 2,
        #         "stroke_opacity": 0.6
        #     }).set_z_index(-1))
        
        # self.add(alex, alex_devil, steve, steve_48, arrow1, arrow2, n_1_txt, n_48_txt, 
        #          eq, luckiest_txt, red_circle, multiple_testing_txt, p_hacking_txt, random_sampling_txt)
        
        self.play(
            FadeIn(alex)
        )

        self.play(
            FadeIn(steve),
            GrowArrow(arrow1),
            Write(n_1_txt)
        )

        self.wait()

        self.play(
            FadeIn(alex_devil)
        )

        self.play(
            FadeIn(steve_48),
            GrowArrow(arrow2),
            Write(n_48_txt)
        )

        self.wait()

        self.play(
            AnimationGroup(
                *[FadeIn(line) for line in eq],
                lag_ratio=0.05
            ),
            run_time=1
        )

        self.wait()

        self.play(
            Write(multiple_testing_txt),
            run_time=0.8
        )

        self.wait()

        self.play(
            Write(random_sampling_txt),
            run_time=0.8
        )

        self.wait()

        self.play(
            Create(red_circle),
            Write(luckiest_txt),
            run_time=0.8
        )

        self.play(
            Create(random_sampling_cross)
        )

        self.wait()

        self.play(
            Write(p_hacking_txt),
            run_time=0.8
        )

        self.wait()

        self.play(
            FadeOut(*[m for m in self.mobjects if m not in [alex, arrow2, n_48_txt, steve_48]]),
            Group(arrow2, n_48_txt, steve_48).animate.set_y(alex.get_y()),
            run_time=1
        )

        self.wait()

        # ##################################################################################

        Group(arrow2, n_48_txt, steve_48).set_y(alex.get_y())

        lower_txt = Tex(r"Lower $\alpha$", font_size = 48).next_to(alex, DOWN, buff=0.5)
        lower_txt[0][-1].set_color(PROB_PINK)

        alpha_new_txt = MathTex(r"\alpha_{\text{new}} = \frac{\alpha}{m}", font_size = 48).next_to(lower_txt, DOWN, buff=0.6).align_to(lower_txt, LEFT)

        alpha_new_txt[0][:4].set_color(GREEN_B)
        alpha_new_txt[0][5].set_color(PROB_PINK)

        bonferroni_txt = Text("(Bonferroni correction)", font_size=40, slant=ITALIC).next_to(alpha_new_txt, RIGHT, buff=0.5)

        correction_eq = VGroup()

        correction_eq.add( # 0
            Tex("If $H_0$ is true in all tests:", font_size=36).next_to(steve_48, RIGHT, buff=0.8).align_to(steve_48, UP)
        )

        correction_eq.add( # 1
            Tex(r"E[\#FP]", font_size = 44).next_to(correction_eq[-1], DOWN, buff=0.5).align_to(correction_eq[-1], LEFT)
        )
        correction_eq[-1][0][3:5].set_color(RED)

        correction_eq.add( # 2
            MathTex(r"= m \alpha_{\text{new}}", font_size = 44).next_to(correction_eq[-1], RIGHT, buff=0.2)
        )

        correction_eq[-1][0][2:].set_color(GREEN_B)

        correction_eq.add( # 3
            MathTex(r"= m \frac{\alpha}{m}", font_size = 44).next_to(correction_eq[-1], DOWN, buff=0.3).align_to(correction_eq[-1], LEFT)
        )
        correction_eq[-1][0][2].set_color(PROB_PINK)

        correction_eq.add( # 4
            MathTex(r"= \alpha", font_size = 44).next_to(correction_eq[-1], DOWN, buff=0.3).align_to(correction_eq[-1], LEFT)
        )
        correction_eq[-1][0][1].set_color(PROB_PINK)

        correction_eq.add( # 5
            MathTex(r"< 1", font_size = 44).next_to(correction_eq[-1], DOWN, buff=0.3).align_to(correction_eq[-1], LEFT)
        )

        correction_txt = Text("multiple testing correction", slant=ITALIC, font_size=50).align_on_border(DOWN, buff=0.7)

        #################################################################
        # Animation (2)                                                 #
        #################################################################
        # self.add(alex, arrow2, n_48_txt, steve_48)
        # self.add(correction_eq, correction_txt, lower_txt, alpha_new_txt, bonferroni_txt)

        self.play(
            Write(lower_txt),
            run_time=0.7
        )

        self.wait()

        self.play(
            Write(correction_txt),
            run_time = 1.1
        )

        self.wait()

        self.play(
            Write(alpha_new_txt),
            run_time=0.7
        )

        self.wait()

        self.play(
            Write(bonferroni_txt),
            run_time=0.8
        )

        self.wait()

        self.play(
            Write(correction_eq[0:3]),
            run_time=1.5
        )

        self.play(
            Transform(correction_eq[2][0][0].copy(), correction_eq[3][0][0]),
            Transform(correction_eq[2][0][1].copy(), correction_eq[3][0][1]),
            Transform(correction_eq[2][0][2:].copy(), correction_eq[3][0][2:]),
        )

        self.play(
            Transform(correction_eq[3][0][0].copy(), correction_eq[4][0][0]),
            Transform(correction_eq[3][0][2].copy(), correction_eq[4][0][1]),
        )

        self.play(
            FadeIn(correction_eq[5])
        )

        self.wait()

        self.play(
            FadeOut(*self.mobjects, shift=DOWN*0.2)
        )

        self.wait(0.1)





