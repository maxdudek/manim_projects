from manim import *
from probability_mobjects import *
from dudek_utils import *

class _31_malicious_researcher(Scene):
    def construct(self):

        mult_txt = Text("Multiple testing", font_size=72, line_spacing=0.5)

        steve_1200 = GenericImageMobject("assets/steve_1200.png", scale_to_resolution=2160).align_on_border(LEFT)

        rect = Rectangle(color = YELLOW, width=0.7, height=7.45).set_x(0.72)

        alex_devil = GenericImageMobject("assets/alex_devil.png").scale_to_fit_height(3).move_to((2.5, -2, 0))

        alex_devil.set_z_index(1)

        bubble = SVGMobject("assets/speech_bubble_right.svg", stroke_width=4).scale_to_fit_width(5.5).set_x(4).shift(DOWN*0.3)

        red_arrow = Arrow(
            alex_devil.get_corner(UL)+DOWN*0.5,
            (1,-0.4,0),
            stroke_width=4,
            color=RED,
            buff=0
        )

        red_circle = Circle(0.2, color=RED).move_to((0.9,-0.35,0))

        cheater_txt = Text("p = 0.0008, cheater!", font_size=24, color=RED).move_to(bubble).shift(UP*0.1)

        if_txt = Tex("If $H_0$ is true in all tests:", font_size=40).align_on_border(UR, buff=0.7).shift(LEFT*0.3)

        eq = VGroup()

        eq.add( # 0
            Tex(r"E[\#FP]").next_to(if_txt, DOWN, buff=0.4).align_to(if_txt, LEFT)
        )
        eq[-1][0][3:5].set_color(RED)

        eq.add( # 1
            MathTex(r"= m \alpha").next_to(eq[-1], RIGHT, buff=0.3).shift(UP*0.05)
        )
        eq[-1][0][-1].set_color(PROB_PINK)

        eq.add( # 2
            MathTex(r"= (1200)(0.05)").next_to(eq[-1], DOWN, buff=0.3).align_to(eq[-1], LEFT)
        )
        eq[-1][0][-5:-1].set_color(PROB_PINK)

        eq.add( # 3
            MathTex(r"= 60").next_to(eq[-1], DOWN, buff=0.2).align_to(eq[-1], LEFT)
        )

        eq[-1][0][1:].set_color(YELLOW)

        #######################################################################

        pmf_plot = PMFBarPlot.binom(
            n=100, p=0.5, width=2, height=5/4, 
            gap=0.01, alpha=1e-7, min_prob=0,
            x_labels_font_size = 0, y_nums=False,show_y_label=False, include_ticks=False
        )

        pmf_plots = VGroup(
            *[
                PMFBarPlot.binom(
                n=100, p=0.5, width=2, height=5/4, 
                gap=0.01, alpha=1e-7, min_prob=0, x_prime_height_scale=1.05,
                x_labels_font_size = 0, y_nums=False,show_y_label=False, include_ticks=False)

                for i in range(20)
            ]
        )

        pmf_plots.arrange_in_grid(
            rows=5,
            buff=0.1
        ).align_on_border(RIGHT)

        x_prime_values = [46, 50, 48, 42, 54, 45, 48, 51, 51, 48, 47, 49, 53, 54, 56, 51, 64, 44, 52, 50]

        def scale_to_fit_area(mobject, area):
            scale_factor = sqrt(area / (mobject.width * mobject.height))
            return(mobject.scale(scale_factor))

        images = Group()
        for i in range(20):
            image = GenericImageMobject(f"assets/ways_to_cheat/{i}.png")
            images.add(image)
            scale_to_fit_area(image, 0.3)
            image.move_to(pmf_plots[i].get_center()).shift(RIGHT*0.7)

        steve_angel = GenericImageMobject("assets/steve_angel.png").scale_to_fit_height(2.5).align_on_border(UL, buff=1).shift(RIGHT*1)

        red_rect = Rectangle(width=8/4 + 0.15, height=5/4 + 0.15, color=RED, stroke_width=6).move_to(pmf_plots[16])
        red_rect.set_z_index(1)

        sunglasses = VGroup(*[
            Rectangle(width=8/4 + 0.15, height=5/4 + 0.15, color=BLACK, fill_opacity=0.8).move_to(pmf_plots[i]) for i in range(20) if i != 16
        ])

        #################################################################
        # Animation (1)                                                 #
        #################################################################
        # self.add(NumberPlane(
        #     background_line_style={
        #         "stroke_width": 2,
        #         "stroke_opacity": 0.6
        #     }).set_z_index(-1))
        
        # self.add(steve_1200, rect, alex_devil, bubble, cheater_txt, if_txt, red_arrow, eq, red_circle)

        self.play(
            Write(mult_txt)
        )

        self.wait()

        self.play(
            Unwrite(mult_txt, reverse=False)
        )

        self.wait(0.1)

        self.play(
            FadeIn(alex_devil)
        )

        self.wait()

        self.play(
            FadeIn(steve_1200, shift=DOWN*0.1)
        )

        self.wait()

        self.play(
            Write(if_txt),
            run_time=1
        )

        self.play(
            Write(eq[:2]),
            run_time=1
        )

        self.play(
            Transform(eq[1][0][0].copy(), eq[2][0][0]),
            Transform(eq[1][0][1].copy(), eq[2][0][1:7]),
            Transform(eq[1][0][2].copy(), eq[2][0][7:]),
        )

        self.play(
            Transform(eq[2][0][0].copy(), eq[3][0][0]),
            Transform(eq[2][0][1:].copy(), eq[3][0][1:]),
        )

        self.play(
            Create(rect)
        )

        self.wait()

        self.play(
            GrowArrow(red_arrow),
            Create(red_circle)
        )

        self.play(
            Create(bubble),
            Write(cheater_txt),
            run_time=1
        )

        self.wait()

        self.play(
            FadeOut(*[m for m in self.mobjects if m is not alex_devil]),
            alex_devil.animate.align_on_border(LEFT, buff=0.8)
        )

        self.wait()

        #Transition
        bubble.scale_to_fit_width(5).set_x(-4.3)
        alex_devil.align_on_border(LEFT, buff=0.8)
        red_arrow2 = Arrow(
            alex_devil.get_edge_center(RIGHT),
            red_rect.get_edge_center(LEFT),
            stroke_width=6,
            color=RED
        )
        hate_txt = Text("i h8 u", font_size=24, color=RED).move_to(bubble).shift(UP*0.1)
        significant_txt = Text("Significant!", font_size=24, color=RED).move_to(bubble).shift(UP*0.1)

        #################################################################
        # Animation (2)                                                 #
        #################################################################
        # Testing
        
        # red_arrow2 = Arrow(
        #     alex_devil.get_edge_center(RIGHT),
        #     red_rect.get_edge_center(LEFT),
        #     stroke_width=6,
        #     color=RED
        # )
        # self.add(alex_devil)
        # self.add(bubble, pmf_plots, images, steve_angel, red_rect, red_arrow2, significant_txt)

        self.play(
            FadeIn(steve_angel)
        )

        self.play(
            Create(bubble),
            AddTextLetterByLetter(hate_txt),
            run_time=0.8
        )

        self.wait()

        self.play(
            AnimationGroup(
                *[FadeIn(plot) for plot in pmf_plots],
                lag_ratio=0.03
            ),
            run_time=0.5
        )

        # Restore colors
        self.play(
            AnimationGroup([
                plot.bars[i].animate.set_color(plot.color1 if plot.i2x(i) >= 50 else plot.color2)
                for plot in pmf_plots for i in range(len(plot.bars)) 
            ])
        )

        for plot in pmf_plots:
            plot.x_prime.set_value(50)
            plot.resume_updating()
            plot.x_prime_line.resume_updating()

        self.play(
            AnimationGroup([
                Create(plot.x_prime_line.reverse_points()) for plot in pmf_plots
            ], lag_ratio=0.03
            ),
            run_time=0.8
        )

        self.play(
            AnimationGroup([
                pmf_plots[i].x_prime.animate.set_value(x_prime_values[i]) for i in range(20)
            ]),
            run_time=0.8
        )

        self.wait()

        self.play(
            Create(red_rect)
        )

        self.wait()

        self.play(
            FadeIn(sunglasses, shift=np.array([0,0,0]))
        )

        self.wait(0.5)

        self.play(
            FadeOut(sunglasses, shift=np.array([0,0,0]))
        )

        self.wait()

        self.play(
            AnimationGroup(
                *[FadeIn(image) for image in images],
                lag_ratio=0.05
            ),
            run_time=1
        )

        self.wait()

        self.play(
            FadeOut(hate_txt),
            run_time=0.25
        )

        self.play(
            Create(red_arrow2),
            AddTextLetterByLetter(significant_txt)
        )

        self.wait()

        self.play(
            FadeOut(*self.mobjects, shift=DOWN*0.2)
        )

        self.wait(0.1)





