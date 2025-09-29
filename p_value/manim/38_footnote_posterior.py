from manim import *
from probability_mobjects import *
from dudek_utils import *
footnote = __import__('34_footnote_two_sided')

class _38_footnote_posterior(Scene):
    def construct(self):

        footnote_sector, footnote_angle, footnote_border, footnote_txt = footnote.get_footnote(3)

        p_ineq = Tex(r"$p$-value $\neq P(H_0)$", font_size = 60).set_y(footnote_border.get_y())
        p_ineq[0][7:9].set_color(RED)
        p_ineq[0][:7].set_color(BLUE_B)

        xkcd_1 = GenericImageMobject("assets/xkcd_1.png").scale(1.5).align_on_border(DL, buff=0.6)
        xkcd_2 = GenericImageMobject("assets/xkcd_2.png").scale(1.5).next_to(xkcd_1, RIGHT).shift(UP*0.32)
        xkcd_txt = MarkupText(f'<span underline="single" underline_color="{BLUE_D}">xkcd.com/1132/</span>', font_size=40, color=BLUE_D, font="Arial").next_to(xkcd_2, DOWN)

        at_least_txt = Tex("P(data at least as extreme), assuming $H_0$ is true", color=BLUE_B, font_size = 36).next_to(p_ineq[0][0:7], DOWN, buff=0.8)
        at_least_arrow = DoubleArrow(
            at_least_txt.get_edge_center(UP),
            p_ineq[0][0:7].get_edge_center(DOWN),
            buff=0.05,
            color=BLUE_B
        )
        at_least_arrow = separate_double_arrow(at_least_arrow)

        #####################################
        pmf_plot = PMFBarPlot(
            [0, 1], [35/36, 1/36],
            width=4,height=4.8,show_y_label=False, gap=0.25, x_prime=1,
            x_labels_font_size=1
        ).align_on_border(DOWN, buff=1).set_x(xkcd_2.get_x())

        die6 = GenericImageMobject("assets/die6.png").scale_to_fit_width(0.5)
        dice = Group(die6, die6.copy()).arrange(RIGHT, buff=0.1).move_to(pmf_plot.x_num_labels[1]).shift(DOWN*0.2)

        truth_txt = Text("truth", font_size=30).move_to(pmf_plot.x_num_labels[0]).shift(DOWN*0.1)

        null_txt = Tex("$H_0$: sun did not explode", font_size=36).next_to(pmf_plot, RIGHT).set_y(1.5).shift(LEFT, 0.5)

        p_eq = MathTex(r"p = \frac{1}{36} = 0.027", font_size=36, color=BLUE).next_to(pmf_plot, RIGHT).set_y(0.5).shift(LEFT, 0.5)

        wrong_eq = MathTex(
            r"""
            \text{If } &p = P(H_0), \text{ then:} \\
            P(H_1) &= P(\text{sun exploded}) \\
                   &= 1-P(H_0) \\
                   &= 1-p \\
                   &= 0.973 
            """,
            font_size = 32,
            color=RED
        ).next_to(p_eq, DOWN, buff=0.5).shift(RIGHT*0.8)

        ridiculous_txt = Text("ridiculous!!", font_size=24, color=RED).move_to((4,-3,0))

        ridiculous_arrow = Arrow(
            ridiculous_txt.get_edge_center(UP),
            wrong_eq.get_edge_center(DOWN)
        )

        #####################################
        frequentist_txt = Text("Frequentist", slant=ITALIC).move_to((-3.5,1.2,0))
        bayesian_txt = Text("Bayesian", slant=ITALIC).move_to((3.5,1.2,0))

        dividing_line = Line(
            (0,1,0),
            (0,-4.1,0)
        )

        freq_def = Tex(r"probability $\longleftrightarrow$ frequency", font_size=40).next_to(frequentist_txt, DOWN, buff=0.7)
        bayes_def = Tex(r"probability $\longleftrightarrow$ belief/confidence", font_size=40).next_to(bayesian_txt, DOWN, buff=0.7)

        steve_angel = GenericImageMobject("assets/steve_angel.png").scale(0.4).move_to((-2,-1.7,0))
        steve_devil = GenericImageMobject("assets/steve_devil.png").scale(0.4).move_to(steve_angel)

        freq_eq = MathTex("P(H_0) = 0", font_size=58).set_y(steve_devil.get_y()).align_to(freq_def, LEFT)
        _1_txt = MathTex("1", font_size=58).move_to(freq_eq[0][-1])
        _q_txt = MathTex(r"\text{?}", font_size=58).move_to(freq_eq[0][-1])

        unknown_txt = Text('"unknown"', font_size=36).align_on_border(DOWN, buff=0.7).set_x(-3.5)

        number_line = NumberLine(
            x_range=[0, 1, 0.1],
            length=4,
            include_numbers=True,
            numbers_to_include=[0, 0.5, 1.0]
        ).move_to((3.5,-3.2,0)) 

        p_value_dot = Dot(radius=0.15, color=PURPLE)
        p_value_dot.move_to(number_line.n2p(0.7))

        definitely_h0_txt = Tex("Definitely $H_0$", font_size=24).move_to(number_line.n2p(1)).shift(UP*0.5)
        definitely_h1_txt = Tex("Definitely $H_1$", font_size=24).move_to(number_line.n2p(0)).shift(UP*0.5)

        bayes_eq = MathTex("P(H_0) =", font_size=58, color=PURPLE_B).set_y(freq_eq.get_y()).set_x(2)
        bayes_eq_data = MathTex(r"P(H_0 \text{ given data}) =", font_size=58, color=PURPLE_B).set_y(freq_eq.get_y()).align_to(bayes_eq, LEFT)

        prior_txt = Tex("$P(H_0)$ = prior probability (before data)", font_size = 36).next_to(bayes_eq_data, UP)

        thumbnail = GenericImageMobject("assets/3b1b_thumbnail.png").scale_to_fit_height(6)

        #################################################################
        # Animation (1)                                                 #
        #################################################################
        # self.add(NumberPlane(
        #     background_line_style={
        #         "stroke_width": 2,
        #         "stroke_opacity": 0.6
        #     }).set_z_index(-1))
        # self.add(footnote_sector, footnote_border, footnote_txt)
        # self.add(p_ineq, )
        # self.add(xkcd_1)
        # self.add(xkcd_2, xkcd_txt, at_least_txt, at_least_arrow)
        # self.add(pmf_plot, dice, truth_txt, null_txt, p_eq, wrong_eq, ridiculous_txt, ridiculous_arrow)
        # self.add(frequentist_txt, bayesian_txt, freq_def, bayes_def, steve_devil,
        #          freq_eq, unknown_txt, number_line, p_value_dot,
        #          definitely_h0_txt, definitely_h1_txt, bayes_eq, prior_txt)

        self.add(footnote_sector)
        self.play(
            footnote_angle.animate.set_value(TAU),
            Create(footnote_border),
            run_time=0.5
        )
        self.play(
            Write(footnote_txt),
            run_time=0.6
        )

        self.play(
            Write(p_ineq)
        )

        self.wait()

        self.play(
            Indicate(p_ineq[0][7:9], color=RED, scale_factor=1.4),
            run_time=1.3
        )

        self.wait()

        self.play(
            Write(at_least_txt),
            GrowDoubleArrow(at_least_arrow),
            run_time=0.8
        )

        self.wait()

        self.play(
            FadeIn(xkcd_1, xkcd_2, xkcd_txt)
        )

        self.wait()

        self.play(
            AnimationGroup(
                FadeOut(xkcd_2, xkcd_txt, at_least_txt, at_least_arrow),
                FadeIn(pmf_plot, dice, truth_txt),
                lag_ratio=0.8
            ) 
        )

        self.wait()

        self.play(
            Write(null_txt),
            run_time=0.8
        )

        self.play(
            Write(p_eq),
            run_time=0.8
        )

        self.wait(0.1)

        self.play(
            Write(wrong_eq)
        )

        self.play(
            Write(ridiculous_txt),
            GrowArrow(ridiculous_arrow)
        )

        self.wait()

        self.play(
            Circumscribe(p_ineq[0][-5:])
        )

        self.wait()

        self.play(
            AnimationGroup(
                FadeOut(pmf_plot, dice, truth_txt, null_txt, p_eq, wrong_eq, ridiculous_txt, ridiculous_arrow, xkcd_1),
                Write(frequentist_txt),
                lag_ratio=0.7
            )   
        )

        self.wait()

        self.play(
            Write(freq_def),
            run_time=0.8
        )

        self.wait()

        self.play(
            FadeIn(steve_devil)
        )

        self.wait()

        self.play(
            FadeIn(steve_angel),
            FadeOut(steve_devil)
        )

        self.wait()

        self.play(
            FadeOut(steve_angel)
        )

        self.wait()

        self.play(
            FadeIn(freq_eq),
            FadeIn(steve_devil)
        )

        self.wait(0.5)

        self.play(
            FadeIn(steve_angel, _1_txt),
            FadeOut(steve_devil, freq_eq[0][-1]),
        )

        self.wait(0.5)

        self.play(
            FadeIn(_q_txt),
            FadeOut(steve_angel, _1_txt),
        )

        self.wait()

        self.play(
            Write(unknown_txt),
            run_time=0.8
        )

        self.wait()

        self.play(
            Write(bayes_def),
            run_time=0.8
        )

        self.wait()

        self.play(
            Write(bayesian_txt),
            run_time=0.8
        )

        self.wait()

        self.play(
            Write(bayes_eq)
        )

        self.play(
            FadeIn(number_line, definitely_h0_txt, definitely_h1_txt, p_value_dot)
        )

        self.wait()

        self.play(
            Transform(bayes_eq[0][-2:], bayes_eq_data[0][-2:]),
            FadeIn(bayes_eq_data[0][4:-2], shift=DOWN*1),
            p_value_dot.animate.move_to(number_line.n2p(0.2))
        )

        self.wait()

        self.play(
            Circumscribe(bayes_eq_data)
        )

        self.wait()

        self.play(
            Write(prior_txt),
            run_time=0.8
        )

        self.wait()

        self.play(
            FadeOut(*[m for m in self.mobjects if m not in [footnote_sector, footnote_border, footnote_txt]])
        )

        self.play(
            FadeIn(thumbnail)
        )

        self.wait()

        self.play(
            FadeOut(*self.mobjects)
        )

        self.wait(0.1)






