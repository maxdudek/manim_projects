from manim import *
from probability_mobjects import *
from dudek_utils import *

class _21_n1000_example(Scene):
    def construct(self):

        png501 = GenericImageMobject("assets/rod_501.png", scale_to_resolution=2160).align_on_border(DL, buff=1).shift(DOWN*0.5)
        data_graphic = Group(png501, SurroundingRectangle(png501, color = WHITE, buff=0.1))
        data_txt = Text("Data (501/1000)", color=WHITE, font_size=36).next_to(data_graphic, UP)
        data_txt[:4].set_color(ORANGE)
        data_txt[5:8].set_color(ORANGE)

        shouldnt_be_significant_txt = Text("shouldn't be significant", font_size=28, color=GREEN).next_to(data_txt, UP, buff=0.8)
        shouldnt_arrow = Arrow(
            shouldnt_be_significant_txt.get_edge_center(DOWN),
            data_txt.get_edge_center(UP),
            color=GREEN,
            buff=0.1
        )

        null_world = GenericImageMobject("assets/null_world.png").scale(0.5).move_to((2,2.5,0))

        steve_angel = GenericImageMobject("assets/steve_angel.png").scale(0.4).next_to(null_world, LEFT, buff=1)

        brace = BraceBetweenPoints((-2,1,0), (6,1,0), direction=UP, sharpness=1)

        params_txt = MathTex(r"n=1000, \mu=0.5", font_size=36).next_to(brace, DOWN)

        pmf_plot = PMFBarPlot.binom(
            n=1000, p=0.5, width=7.5, height=3, 
            gap=0.01, alpha=1e-6, min_prob=0,
            x_label=Tex("$x$ (number of blaze rods)", font_size = 40),
            x_labels_font_size=20, coloring_mode="equal",
        ).align_on_border(DOWN, buff=0.3).set_x(brace.get_x())

        BLUE_TXT="#76C9DC"
        x_prime_tracker = Integer(501, color=ORANGE)
        prob_tracker = DecimalNumber(0, num_decimal_places=3, color = BLUE_TXT)

        prob_eq = VGroup(
            MathTex(r"P(X=", color = BLUE_TXT), 
            x_prime_tracker, 
            MathTex(r") \approx", color = BLUE_TXT),
            prob_tracker
        ).arrange(RIGHT, buff=0.15).scale(0.8).move_to((5,0.2,0))
        x_prime_tracker.shift(UP*0.02 + RIGHT*0.02)

        x_prime_tracker.add_updater(lambda v: v.set_value(round(pmf_plot.x_prime.get_value())))
        prob_tracker.add_updater(lambda v: v.set_value(binom_pmf(
            x_prime_tracker.get_value(),
            n=1000,
            p=0.5
        )))

        rare_txt = Text("Rare", font_size=40).next_to(data_txt, DOWN).set_y(1)

        surprising_txt = Text("Surprising", font_size=40).next_to(data_txt, DOWN).set_y(-2)

        double_arrow = DoubleArrow(
            rare_txt.get_edge_center(DOWN),
            surprising_txt.get_edge_center(UP),
            color=GREY,
            stroke_width = 6
        )

        arrow_upper = Arrow(
            double_arrow.get_center(),
            double_arrow.get_edge_center(UP),
            color=double_arrow.color,
            stroke_width = double_arrow.stroke_width,
            buff=0
        )

        arrow_lower = Arrow(
            double_arrow.get_center(),
            double_arrow.get_edge_center(DOWN),
            color=GREY,
            stroke_width = 6,
            buff=0
        )

        X_SIZE=0.2
        x_arrow = VGroup(
            Line(double_arrow.get_center()+UR*X_SIZE, double_arrow.get_center()+DL*X_SIZE, color=RED, stroke_width=10),
            Line(double_arrow.get_center()+UL*X_SIZE, double_arrow.get_center()+DR*X_SIZE, color=RED, stroke_width=10),
        )

        
        #################################################################
        # Animation (1)                                                 #
        #################################################################
        # self.add(NumberPlane(
        #     background_line_style={
        #         "stroke_width": 2,
        #         "stroke_opacity": 0.6
        #     }))
        # self.add(data_graphic, data_txt, shouldnt_be_significant_txt, shouldnt_arrow)
        # self.add(null_world, brace, steve_angel, params_txt, pmf_plot)
        # self.add(rare_txt, surprising_txt, double_arrow, x_arrow)

        self.play(
            FadeIn(data_graphic[0]),
            Create(data_graphic[1]),
            Write(data_txt)
        )

        self.wait()

        self.play(
            Write(shouldnt_be_significant_txt),
            GrowArrow(shouldnt_arrow),
            run_time=0.5
        )

        self.wait()

        self.play(
            FadeIn(null_world, steve_angel, brace, shift=DOWN*0.2)
        )

        self.play(
            FadeIn(params_txt, pmf_plot, shift=DOWN*0.2)
        )

        # Restore colors
        self.play(
            AnimationGroup([
                pmf_plot.bars[i].animate.set_color(pmf_plot.color1 if pmf_plot.i2x(i) == 501 else pmf_plot.color2)
                for i in range(len(pmf_plot.bars))
            ])
        )

        pmf_plot.x_prime.set_value(501)
        pmf_plot.resume_updating()

        self.play(
            Write(prob_eq)
        )

        self.play(
            Circumscribe(prob_tracker, time_width=0.5)
        )

        self.wait()

        self.play(
            Circumscribe(shouldnt_be_significant_txt, time_width=0.5)
        )

        self.wait()

        self.play(
            FadeOut(data_graphic, data_txt, shouldnt_be_significant_txt, shouldnt_arrow, shift=DOWN*0.2)
        )

        self.play(
            Write(rare_txt),
            run_time=0.5
        )

        self.wait()

        self.play(
            Write(surprising_txt),
            GrowDoubleArrow(separate_double_arrow(double_arrow)),
            Create(x_arrow),
            run_time=0.8
        )

        self.wait()

        self.play(
            pmf_plot.x_prime.animate.set_value(516)
        )

        self.play(
            pmf_plot.x_prime.animate.set_value(485)
        )

        self.play(
            pmf_plot.x_prime.animate.set_value(501)
        )

        self.wait()

        self.play(
            FadeOut(*self.mobjects, shift=DOWN*0.2)
        )

        self.wait(0.1)





