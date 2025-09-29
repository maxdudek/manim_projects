from manim import *
from probability_mobjects import *
from dudek_utils import *
footnote = __import__('34_footnote_two_sided')

class _35_two_sided(Scene):
    def construct(self):

        footnote_sector, footnote_angle, footnote_border, footnote_txt = footnote.get_footnote(1, redraw=False)

        pmf_plot = PMFBarPlot.binom(
            n=100, p=0.5, width=8, height=3.5, 
            gap=0.04, alpha=1e-8, min_prob=0, coloring_mode="two-sided", x_prime=56,
            x_prime_height_scale=1.1,
            x_label=Tex("$x$ (number of blaze rods)", font_size = 40)
        ).shift(LEFT*0.5+DOWN*0.3)
        pmf_plot.x_prime_line.set_z_index(1)

        pmf_plot.resume_updating()
        pmf_plot.x_prime_line.resume_updating()
        pmf_plot.x_prime_label.resume_updating()

        x_prime_upper_tracker = Integer(56, color=ORANGE)
        x_prime_lower_tracker = Integer(44, color=ORANGE)
        prob_upper_tracker = DecimalNumber(0, num_decimal_places=3, color = BLUE)
        prob_lower_tracker = DecimalNumber(0, num_decimal_places=3, color = BLUE)
        prob_total_tracker = DecimalNumber(0, num_decimal_places=3, color = BLUE)

        prob_eq = VGroup(
            MathTex(r"p = P(X\geq", color = BLUE),  # 0
            x_prime_upper_tracker,                  # 1
            MathTex(r") + P(X \leq", color = BLUE), # 2
            x_prime_lower_tracker,                  # 3
            MathTex(r")", color = BLUE)             # 4
        ).arrange(RIGHT, buff=0.15).scale(0.8).move_to((3.8,2,0))

        x_prime_upper_tracker.shift(UP*0.01, RIGHT*0.05)
        x_prime_lower_tracker.shift(UP*0.01, RIGHT*0.05)

        prob_eq.add( # 5
            MathTex(r"=", color = BLUE).scale(0.8).next_to(prob_eq[0][0][1], DOWN, buff=0.6)
        )

        prob_eq.add(
            prob_upper_tracker.scale(0.9).next_to(prob_eq[0][0][-1], DOWN).set_y(prob_eq[-1].get_y())
        )

        prob_eq.add(
            MathTex(r"+", color = BLUE).scale(0.8).next_to(prob_eq[2][0][1], DOWN).set_y(prob_eq[-1].get_y())
        )

        prob_eq.add(
            prob_lower_tracker.scale(0.9).next_to(prob_eq[2][0][-1], DOWN).set_y(prob_eq[-1].get_y())
        )

        prob_eq.add(
            MathTex(r"=", color = BLUE).scale(0.8).next_to(prob_eq[5], DOWN, buff=0.6)
        )

        prob_eq.add(
            prob_total_tracker.scale(0.9).next_to(prob_eq[-1], RIGHT)
        )


        x_prime_upper_tracker.add_updater(lambda v: v.set_value(round(
            max(pmf_plot.x_prime.get_value(), 2*pmf_plot.mode-pmf_plot.x_prime.get_value()) 
        )))
        x_prime_lower_tracker.add_updater(lambda v: v.set_value(round(
            min(pmf_plot.x_prime.get_value(), 2*pmf_plot.mode-pmf_plot.x_prime.get_value()) 
        )))
        prob_upper_tracker.add_updater(lambda v: v.set_value(pbinom(
            x_prime_upper_tracker.get_value(),
            n=100,
            p=0.5
        )))
        prob_lower_tracker.add_updater(lambda v: v.set_value(pbinom(
            x_prime_upper_tracker.get_value(),
            n=100,
            p=0.5
        )))
        prob_total_tracker.add_updater(lambda v: v.set_value(prob_upper_tracker.get_value() + prob_upper_tracker.get_value()))

        one_sided_txt = Tex("One-sided $R$", font_size=55, color=PROB_PINK).move_to((4,-0.5,0))
        two_sided_txt = Tex("Two-sided $R$", font_size=55, color=PROB_PINK).next_to(one_sided_txt, DOWN)

        reject_h0_txt = MarkupText("Reject H<sub>0</sub>!", font_size=40, color=PROB_PINK).move_to((-3,2,0))
        reject_h0_txt.add_updater(lambda v: v.set_opacity(1 if (pmf_plot.x_prime.get_value() >= 61 or pmf_plot.x_prime.get_value() <= 39) else 0))

        #################################################################
        # Animation (1)                                                 #
        #################################################################
        # self.add(NumberPlane(
        #     background_line_style={
        #         "stroke_width": 2,
        #         "stroke_opacity": 0.6
        #     }).set_z_index(-1))
        # self.add(pmf_plot, pmf_plot.x_prime_line, pmf_plot.x_prime_label)
        # self.add(prob_eq)
        # self.add(one_sided_txt, two_sided_txt)

        self.add(footnote_sector, footnote_txt, footnote_border)

        self.play(
            FadeIn(pmf_plot, pmf_plot.x_prime_line, pmf_plot.x_prime_label)
        )

        prob_lower_tracker.resume_updating()
        prob_upper_tracker.resume_updating()
        prob_total_tracker.resume_updating()

        self.play(
            FadeIn(prob_eq)
        )
        
        self.play(
            pmf_plot.x_prime.animate.set_value(41),
            run_time=3
        )

        self.play(
            pmf_plot.x_prime.animate.set_value(64),
            run_time=3
        )

        self.play(
            pmf_plot.x_prime.animate.set_value(54),
            run_time=2
        )

        # Recolor bars to one-sided rejection
        pmf_plot.freeze_bars()
        self.play(
            AnimationGroup([
                pmf_plot.bars[i].animate.set_color(PROB_PINK if pmf_plot.i2x(i) >= 59 else pmf_plot.color2)
                for i in range(len(pmf_plot.bars))
            ]),
            FadeIn(one_sided_txt)
        )

        self.wait(0.5)

        # Recolor bars to two-sided rejection
        self.play(
            AnimationGroup([
                pmf_plot.bars[i].animate.set_color(PROB_PINK if (pmf_plot.i2x(i) >= 61 or pmf_plot.i2x(i) <= 39) else pmf_plot.color2)
                for i in range(len(pmf_plot.bars))
            ]),
            FadeOut(one_sided_txt),
            FadeIn(two_sided_txt)
        )

        self.add(reject_h0_txt)

        self.play(
            pmf_plot.x_prime.animate.set_value(64),
            run_time=3
        )

        self.play(
            pmf_plot.x_prime.animate.set_value(34),
            run_time=3
        )

        self.wait()

        reject_h0_txt.clear_updaters()

        self.play(
            FadeOut(*self.mobjects, shift=DOWN*0.2)
        )

        self.wait(0.1)






