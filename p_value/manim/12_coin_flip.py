from manim import *
from probability_mobjects import *
from dudek_utils import *

class CoinFlip(Scene):
    def construct(self):
        n_header = Variable(1, label=Tex("$n = $ number of coin flips "), var_type=Integer).set_y(2.5)

        n_vals = [1, 2, 3, 4, 10, 20, 50, 100]
        # n_vals = [1, 2, 10, 100]
        pmf_plots = [
            PMFBarPlot.binom(
            n=n, p=0.5, width=7, height=4, gap = 0.1 if n < 10 else 0.05,
            alpha=1e-8, min_prob=0,
            x_label=Tex("$x$ (number of heads)", font_size = 48)
            ).shift(RIGHT*1)
            for n in n_vals
        ]

        coin_flip = GenericImageMobject("assets/coin_flip.png").scale(2).move_to((-5,2.2,0))

        binomial_txt = Text("Binomial\ndistribution", font_size=36).move_to((4.5,0,0))   

        x_prime_tracker = Integer(56, color=BLUE)
        prob_tracker = DecimalNumber(0, num_decimal_places=3, color = BLUE)

        prob_eq = VGroup(
            MathTex(r"P(X\geq", color = BLUE), 
            x_prime_tracker, 
            MathTex(r") \approx", color = BLUE),
            prob_tracker
        ).arrange(RIGHT, buff=0.15).scale(0.8).move_to((4.5,0,0))


        x_prime_tracker.add_updater(lambda v: v.set_value(round(pmf_plots[-1].x_prime.get_value())))
        prob_tracker.add_updater(lambda v: v.set_value(pbinom(
            x_prime_tracker.get_value(),
            n=n_vals[-1],
            p=0.5
        )))

        pmf_plots[-1].x_prime_label.set_z_index(1)
        pmf_plots[-1].x_prime_line.set_z_index(1)


        #################################################################
        # Animation (1)                                                 #
        #################################################################
        # Testing
        # self.add(NumberPlane(), Dot(ORIGIN))
        # self.add(n_header, pmf_plots[-1], coin_flip, prob_eq)

        self.play(
            FadeIn(coin_flip, n_header, shift=DOWN*0.1),
            Create(pmf_plots[0].axes),
            Write(pmf_plots[0].x_label),
            Write(pmf_plots[0].x_num_labels),
            Write(pmf_plots[0].y_label),
        )

        self.add(*pmf_plots[0].bars)
        self.play(
            pmf_plots[0].create_bars(lag_ratio = 0.25)
        )

        self.wait()

        self.play(
            Circumscribe(pmf_plots[0].bars[0])
        )

        self.wait()

        self.play(
            Circumscribe(pmf_plots[0].bars[1])
        )

        self.wait()

        for i in range(1,len(pmf_plots)):
            self.wait()
            self.play(
                n_header.tracker.animate.set_value(n_vals[i]),
                ReplacementTransform(pmf_plots[i-1], pmf_plots[i])
            )
            if n_vals[i] == 2:
                for k in range(3):
                    self.play(
                        Circumscribe(pmf_plots[i].x2bar(k), time_width=0.5)
                    )
                    self.wait(0.5)

        self.wait()

        self.play(
            Write(binomial_txt)
        )

        self.wait()

        self.play(
            Circumscribe(n_header.label[0][0], time_width=0.5)
        )

        self.wait()

        self.play(
            Circumscribe(pmf_plots[-1].x_num_labels[6], time_width=0.5)
        )

        self.wait()

        self.play(
            Circumscribe(pmf_plots[-1].x2bar(59), time_width=0.5, buff=0.01)
        )

        self.wait()

        self.play(
            FadeOut(binomial_txt)
        )

        # Restore colors
        self.play(
            AnimationGroup([
                pmf_plots[-1].bars[i].animate.set_color(pmf_plots[-1].color1 if pmf_plots[-1].i2x(i) >= 56 else pmf_plots[-1].color2)
                for i in range(len(pmf_plots[-1].bars))
            ])
        )

        pmf_plots[-1].x_prime.set_value(56)
        pmf_plots[-1].resume_updating()

        self.play(
            Create(pmf_plots[-1].x_prime_line.reverse_points()),
        )

        self.play(
            FadeIn(pmf_plots[-1].x_prime_label, shift=UP*0.5),
            run_time=0.1
        )

        self.wait()

        self.play(
            Write(prob_eq)
        )

        self.wait()

        self.play(
            pmf_plots[-1].x_prime.animate.set_value(62),
            run_time=2
        )

        self.play(
            pmf_plots[-1].x_prime.animate.set_value(48),
            run_time=2
        )

        self.wait()

        self.play(
            FadeOut(*self.mobjects, shift=DOWN*0.1)
        )

        self.wait()


