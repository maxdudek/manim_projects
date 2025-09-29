from manim import *
from probability_mobjects import *
from dudek_utils import *

class _20_intro(Scene):
    def construct(self):

        # Alex
        alex=GenericImageMobject("assets/alex.webp").scale_to_fit_height(3.5).move_to((-5,-1.5,0))

        steve=GenericImageMobject("assets/steve.png").scale_to_fit_height(3.5).move_to((0,-1.5,0))

        spinner = Spinner(0.5).scale(1.8).move_to((4.5,-1.5,0))
        spinner.add_image(GenericImageMobject("assets/rod.png").scale(1.7))

        p_value_definition = Tex(
            r"""
            \begin{flushleft}
            The probability of getting a result \textit{at least} as extreme as the\\
            data that we see, given that the null hypothesis ($H_0$) is true.
            \end{flushleft}
            """,
            font_size = 44
        ).move_to((0,1.8,0))

        p_value_header = Text("p-value:", weight = BOLD, font_size=48, color = BLUE).next_to(p_value_definition, UP, buff=0.4)

        png67 = GenericImageMobject("assets/rod_67.png").scale_to_fit_width(2.7).move_to((4.8,-1.5,0))
        data_graphic = Group(png67, SurroundingRectangle(png67, color = WHITE, buff=0.2))
        data_txt = Text("Data (67/100)", color=WHITE, font_size=36).next_to(data_graphic, UP)
        data_txt[:4].set_color(ORANGE)
        data_txt[5:7].set_color(ORANGE)

        pmf_plot = PMFBarPlot.binom(
            n=100, p=0.5, width=6.5, height=2.7, 
            gap=0.05, alpha=1e-8, min_prob=0,
            x_label=Tex("$x$ (number of blaze rods)", font_size = 40)
        ).move_to((-2.7,-1.7,0))
        pmf_x = pmf_plot.axes.c2p(50,0)[0]

        null_world = GenericImageMobject("assets/null_world.png").scale(0.5).align_on_border(UP)

        steve_angel = GenericImageMobject("assets/steve_angel.png").scale(0.4).next_to(null_world, LEFT, buff=1)

        null_hypothesis_txt = Tex(r"null hypothesis").next_to(null_world, RIGHT, buff=1)

        brace = BraceBetweenPoints((-4,1,0), (4,1,0), direction=UP, sharpness=1).scale(1.5)

        BLUE_TXT="#76C9DC"
        x_prime_tracker = Integer(59, color=ORANGE)
        prob_tracker = DecimalNumber(0, num_decimal_places=4, color = BLUE_TXT)

        prob_eq = VGroup(
            MathTex(r"p =", color = BLUE_TXT),
            MathTex(r"P(X\geq", color = BLUE_TXT), 
            x_prime_tracker, 
            MathTex(r")", color = BLUE_TXT),
            MathTex(r"\approx", color = BLUE_TXT),
            prob_tracker
        ).arrange(RIGHT, buff=0.15).scale(0.9).move_to((0.5,0.5,0))

        x_prime_tracker.shift(UP*0.02 + RIGHT*0.02)

        x_prime_tracker.add_updater(lambda v: v.set_value(round(pmf_plot.x_prime.get_value())))
        prob_tracker.add_updater(lambda v: v.set_value(pbinom(
            x_prime_tracker.get_value(),
            n=100,
            p=0.5
        )))

        

        p_eq_correct = VGroup(
            MathTex(r"p ="),
            MathTex(r"P(X\geq"), 
            MathTex(r"67", color=ORANGE),
            MathTex(r")"),
        ).arrange(RIGHT, buff=0.15).scale(1.3).set_y(1.5)
        p_eq_correct[1][0][-1].shift(LEFT*0.05)
        p_eq_correct[0][0][0].set_color(BLUE_TXT)

        p_eq_incorrect = VGroup(
            MathTex(r"p =", color=LIGHT_PINK),
            MathTex(r"P(X = ", color=LIGHT_PINK), 
            MathTex(r"67", color=LIGHT_PINK),
            MathTex(r")", color=LIGHT_PINK),
        ).arrange(RIGHT, buff=0.15).scale(1.3).next_to(p_eq_correct, DOWN, buff=1.5)

        rect_p_eq_incorrect = SurroundingRectangle(p_eq_incorrect, buff=0.2)

        why_not_txt = Text("why not?", font_size=36, color=LIGHT_PINK).next_to(p_eq_incorrect, DOWN, buff=0.4)

        not_useful_txt = Text("not useful", font_size=42, color=LIGHT_PINK).move_to((4.5, 0.5, 0))

        arrow = Arrow(
            not_useful_txt.get_edge_center(DOWN),
            rect_p_eq_incorrect.get_corner(UR),
            stroke_width = 5,
            max_tip_length_to_length_ratio = 0.15,
        )

        not_useful_txt.shift(UP*0.2)

        #################################################################
        # Animation (1)                                                 #
        #################################################################
        # Testing
        # self.add(NumberPlane(), Dot(ORIGIN))
        # self.add(alex, steve, spinner, p_value_definition, p_value_header)
        # self.add(data_graphic, data_txt, pmf_plot, p_value_definition, p_value_header)
        # # self.add(null_world, steve_angel, brace, null_hypothesis_txt)
        # self.add(prob_eq)
        # self.add(index_labels(prob_eq[2]))
        
        self.play(
            FadeIn(alex, shift=DOWN*0.2)
        )

        self.wait()

        self.play(
            Write(p_value_header[:-1]),
            run_time=0.5
        )

        self.wait()

        self.play(
            FadeIn(steve, shift=DOWN*0.2)
        )

        self.play(
            FadeIn(spinner, shift=DOWN*0.2)
        )

        self.wait()

        self.play(
            Write(p_value_header[-1]),
            Write(p_value_definition),
        )

        self.wait()

        self.play(
            AnimationGroup(
                FadeOut(spinner, shift=DOWN*0.2),
                FadeIn(data_graphic, data_txt, shift=DOWN*0.2),
                lag_ratio=0.2
            )
        )

        self.wait()

        self.play(
            AnimationGroup(
                FadeOut(steve, alex, shift=DOWN*0.2),
                FadeIn(pmf_plot, shift=DOWN*0.2),
                lag_ratio=0.2
            )
        )

        # Restore colors
        self.play(
            AnimationGroup([
                pmf_plot.bars[i].animate.set_color(pmf_plot.color1 if pmf_plot.i2x(i) >= 59 else pmf_plot.color2)
                for i in range(len(pmf_plot.bars))
            ]),
            run_time=0.5
        )

        pmf_plot.x_prime.set_value(59)
        pmf_plot.resume_updating()
        pmf_plot.x_prime_line.resume_updating()

        self.play(
            Create(pmf_plot.x_prime_line.reverse_points()),
            Write(prob_eq),
            run_time=0.8
        )


        pmf_plot.x_prime_label.resume_updating()
        pmf_plot.x_prime_label.set_opacity(0)
        self.add(pmf_plot.x_prime_label)
        pmf_plot.x_prime_label.resume_updating()
        self.remove(pmf_plot.x_prime_label)
        pmf_plot.x_prime_label.set_opacity(1)

        self.play(
            Write(pmf_plot.x_prime_label),
            run_time=0.1
        )

        self.play(
            pmf_plot.x_prime.animate.set_value(67),
            run_time=1
        )

        self.wait(0.1)

        self.play(
            AnimationGroup(
                FadeOut(p_value_definition, p_value_header, shift=DOWN*0.2),
                FadeIn(null_world, steve_angel, brace, null_hypothesis_txt, shift=DOWN*0.2),
                lag_ratio=0.5
            )
        )

        self.wait()

        x_prime_tracker.clear_updaters()

        self.play(
            AnimationGroup(
                FadeOut(pmf_plot, pmf_plot.x_prime_line, data_graphic, data_txt, null_world, steve_angel, brace, null_hypothesis_txt, pmf_plot.x_prime_label, prob_eq[4:], shift=DOWN*0.2),
                AnimationGroup(
                    ReplacementTransform(prob_eq[0], p_eq_correct[0]),
                    ReplacementTransform(prob_eq[1], p_eq_correct[1]),
                    ReplacementTransform(prob_eq[2][0], p_eq_correct[2][0][0]),
                    ReplacementTransform(prob_eq[2][1], p_eq_correct[2][0][1]),
                    ReplacementTransform(prob_eq[3], p_eq_correct[3]),
                ),
                lag_ratio=0.5
            )
        )

        #################################################################
        # Animation (1)                                                 #
        #################################################################
        # self.add(p_eq_correct)

        self.play(
            FadeIn(alex, shift=DOWN*0.2)
        )

        self.wait()

        self.play(
            Indicate(p_eq_correct[1][0][-1], scale_factor=1.4),
            run_time=1.5
        )

        self.wait()

        self.play(
            *[ReplacementTransform(p_eq_correct[i].copy(), p_eq_incorrect[i]) for i in range(4)],
        )

        self.play(
            Indicate(p_eq_incorrect[1][0][-1], scale_factor=1.4),
            Write(why_not_txt),
            run_time=1.5
        )

        self.wait()

        self.play(
            Create(rect_p_eq_incorrect)
        )

        self.wait()

        self.play(
            Write(not_useful_txt),
            GrowArrow(arrow)
        )

        self.wait()

        self.play(
            FadeOut(*self.mobjects, shift=DOWN*0.2)
        )

        self.wait(0.1)





