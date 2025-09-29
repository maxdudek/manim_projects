from manim import *
from probability_mobjects import *
from dudek_utils import *
import random

class _22_million_die(Scene):
    def construct(self):

        million_die = GenericImageMobject("assets/million.png").scale_to_fit_width(4).set_y(2)

        million_sides_txt = Paragraph("(Just imagine this\n has a million sides)", font_size = 28, alignment="left").next_to(million_die, LEFT, buff=0.5)

        prob_eq = VGroup(
            MathTex(r"P( \text{rolling a}"),
            MathTex(f"{1000000:,}"),
            MathTex(r") = \frac{1}{1,000,000}")
        ).arrange(RIGHT, buff=0.15).scale(1).set_y(-1)

        prob_eq[1] = MathTex(f"{628347:,}").move_to(prob_eq[1])

        surprised_txt = Text("Surprised").set_y(-2.5)

        surprised_cross = Line(
            surprised_txt.get_edge_center(LEFT)+LEFT*0.2,
            surprised_txt.get_edge_center(RIGHT)+RIGHT*0.2,
            color=RED,
            stroke_width = 6,
        )

        surprised_rect = SurroundingRectangle(surprised_txt, color=GREEN, buff=0.2)

        random.seed(0)
        rolls = [random.randint(1,1000000) for i in range(5)]
        print(rolls)

        p_value_txt = Text("p-value", font_size=40)
        how_suprised = MarkupText('"How <i>suprised</i> are we?"', font_size=40)
        double_arrow = DoubleArrow((0,0,0), RIGHT*2.5)

        p_value_surprise = VGroup(
            p_value_txt,
            double_arrow,
            how_suprised
        ).arrange(RIGHT, buff=0.25).set_y(-2.5)

        alex=GenericImageMobject("assets/alex.webp").scale_to_fit_height(3.2).move_to((-5.5,1.8,0))

        pmf_plot = PMFBarPlot.binom(
            n=1000, p=0.5, width=8, height=3, 
            gap=0.01, alpha=1e-6, min_prob=0, x_prime_height_scale=1.1,
            x_label=Tex("$x$ (number of blaze rods)", font_size = 40),
            x_labels_font_size=20,
        ).align_on_border(DOWN, buff=0.3)

        x_prime_tracker = Integer(501, color=ORANGE)

        surprised_eq = VGroup(
            MathTex(r"P(X\geq"), 
            x_prime_tracker, 
            MathTex(r")"),
            DoubleArrow((0,0,0), RIGHT*2),
            MarkupText('"How <i>suprised</i>?"', font_size=40)
        ).arrange(RIGHT, buff=0.15).scale(0.9).set_y(2.5)
        x_prime_tracker.shift(UP*0.02 + RIGHT*0.02)

        surprised_eq_rect = SurroundingRectangle(surprised_eq, color=BLUE, buff=0.3)

        x_prime_tracker2 = Integer(501, color=RED)
        rare_eq = VGroup(
            MathTex(r"P(X=", color=RED), 
            x_prime_tracker2, 
            MathTex(r")", color=RED),
            DoubleArrow((0,0,0), RIGHT*2, color=RED),
            MarkupText('"How <i>rare</i>?"', font_size=40, color=RED)
        ).arrange(RIGHT, buff=0.15).scale(0.9).set_y(1)
        x_prime_tracker2.shift(UP*0.02 + RIGHT*0.02)

        one_sided_txt = Text('"One-sided"', font_size=40).move_to((4,-0.5,0))

        #################################################################
        # Animation (1)                                                 #
        #################################################################
        # self.add(NumberPlane(
        #     background_line_style={
        #         "stroke_width": 2,
        #         "stroke_opacity": 0.6
        #     }))
        # self.add(million_die, million_sides_txt, prob_eq, p_value_surprise)
        # self.add(surprised_eq, alex, pmf_plot, surprised_eq_rect, rare_eq, one_sided_txt)

        self.play(
            FadeIn(million_die, shift=DOWN*0.2)
        )

        self.play(
            FadeIn(million_sides_txt, shift=DOWN*0.2)
        )

        self.wait()

        self.play(
            Write(prob_eq),
            run_time=1
        )

        for roll in rolls:
            old_roll = prob_eq[1]
            prob_eq[1] = MathTex(f"{roll:,}").move_to(prob_eq[1])
            self.play(
                FadeOut(old_roll, shift=DOWN*0.5),
                FadeIn(prob_eq[1], shift=DOWN*0.5),
            )
            self.wait(0.1)

        self.play(
            Write(surprised_txt),
            run_time=0.5
        )

        self.play(
            Create(surprised_cross),
            run_time=0.3
        )

        self.wait()

        for roll in [1,1000000]:
            old_roll = prob_eq[1]
            prob_eq[1] = MathTex(f"{roll:,}").move_to(prob_eq[1])
            self.play(
                FadeOut(old_roll, shift=DOWN*0.5),
                FadeIn(prob_eq[1], shift=DOWN*0.5),
            )
            self.wait(0.3)

        self.play(
            Uncreate(surprised_cross),
            Create(surprised_rect)
        )

        self.wait()

        self.play(
            FadeOut(million_die, million_sides_txt, shift=DOWN*0.2),
            FadeIn(alex)
        )

        self.play(
            FadeIn(surprised_eq)
        )

        self.wait()

        self.play(
            FadeIn(rare_eq)
        )
        
        self.wait()

        self.play(
            Circumscribe(prob_eq[1], time_width=0.5)
        )

        self.wait()
        
        
        self.play(
            Indicate(surprised_eq[0][0][3], scale_factor=1.4),
            run_time=1.2
        )

        self.wait()

        self.play(
            Create(surprised_eq_rect),
            AnimationGroup(
                FadeOut(prob_eq, surprised_rect, surprised_txt),
                FadeIn(pmf_plot, shift=DOWN*0.2),
                lag_ratio=0.5
            )
        )

        # Restore colors
        self.play(
            AnimationGroup([
                pmf_plot.bars[i].animate.set_color(pmf_plot.color1 if pmf_plot.i2x(i) >= 501 else pmf_plot.color2)
                for i in range(len(pmf_plot.bars))
            ]),
            run_time=0.5
        )

        pmf_plot.x_prime.set_value(501)
        x_prime_tracker.add_updater(lambda v: v.set_value(round(pmf_plot.x_prime.get_value())))
        x_prime_tracker2.add_updater(lambda v: v.set_value(round(pmf_plot.x_prime.get_value())))
        pmf_plot.resume_updating()
        pmf_plot.x_prime_line.resume_updating()
        pmf_plot.x_prime_label.resume_updating()

        self.play(
            Create(pmf_plot.x_prime_line.reverse_points()),
            run_time=0.5
        )

        self.play(
            FadeIn(pmf_plot.x_prime_label, shift=UP*0.1),
            run_time=0.1
        )

        self.play(
            pmf_plot.x_prime.animate.set_value(540),
            run_time=1.7
        )

        self.play(
            pmf_plot.x_prime.animate.set_value(512),
            run_time=1.7
        )

        self.wait()

        self.play(
            Write(one_sided_txt),
            run_time=0.7
        )

        self.wait()

        self.play(
            FadeOut(*self.mobjects, shift=DOWN*0.2)
        )

        self.wait(0.1)





