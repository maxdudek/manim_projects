from manim import *
from probability_mobjects import *
from dudek_utils import *

class _33_conclusion(Scene):
    def construct(self):

        ############# conclusion
        conclusion_txt = Text("Conclusion", font_size=72, line_spacing=0.5)

        ############# blaze example
        steve=GenericImageMobject("assets/steve.png").move_to((-5,0,0))
        steve.height=3.5

        blaze_pos=(-1.5,0,0)
        blaze=GenericImageMobject("assets/blaze.webp").move_to(blaze_pos)
        blaze.height=3.8

        spinner = Spinner(0.5).scale(2).move_to((4,0,0))
        spinner.add_image(GenericImageMobject("assets/rod.png").scale(1.75))
        spinner_text = null_equation_blaze = Group(
            MathTex("P(", color=BLUE), GenericImageMobject("assets/rod.png").scale(1), MathTex(") = \mu = 0.5", color=BLUE)
        ).arrange(RIGHT, buff=0.1).move_to(spinner.get_edge_center(UP)).shift(UP*0.5)

        arrow=Arrow(start=blaze.get_edge_center(RIGHT), end=spinner.get_edge_center(LEFT)+LEFT*0.1)

        skull=GenericImageMobject("assets/skull.png").move_to(arrow).shift(UP*0.5)
        skull.height=0.5

        blaze_example = Group(steve, blaze, spinner, spinner_text, arrow, skull)

        ############# drug example
        person_green = GenericImageMobject("assets/person_green.png")
        person_white = GenericImageMobject("assets/person_white.png")

        drug_data = BinomDataGraphic(38, 48, person_green.copy(), person_white.copy(), 
                                     width=3, ncol=9).move_to((1.5,0,0))
        pill = GenericImageMobject("assets/pill.png").scale(2).next_to(drug_data, UP)
        
        no_drug_data = BinomDataGraphic(21, 48, person_green.copy(), person_white.copy(), 
                                        width=3, ncol=9).next_to(drug_data, RIGHT)
        no_pill = Group(
            GenericImageMobject("assets/pill.png").scale(2),
            GenericImageMobject("assets/dont.png").scale(0.4)
        ).next_to(no_drug_data, UP).set_y(pill.get_y())
        
        person_green.scale_to_fit_height(drug_data[1].height)

        legend = Group(
            person_green.copy(),
            Text("= recovered", font_size=32)
        ).arrange(RIGHT, buff=0.2).next_to(Group(drug_data, no_drug_data), DOWN)

        null_hypothesis_txt = Tex(
            r"null hypothesis",
            font_size = 60
        ).move_to((-3.5, 2, 0))

        alt_hypothesis_txt = Tex(
            r"alternative hypothesis",
            font_size = 60
        ).move_to((-3.5, -0.5, 0))
        alt_hypothesis_txt[0][0:11].set_color(YELLOW)

        null_equation = Group(
            MathTex("H_0: P("), person_green.copy(), MathTex("|"), pill.copy().scale(0.8),
            MathTex(") = P("), person_green.copy(), MathTex("|"), no_pill.copy().scale(0.8), MathTex(")")
        ).arrange(RIGHT, buff=0.1).next_to(null_hypothesis_txt, DOWN)

        alt_equation = Group(
            MathTex("H_1: P("), person_green.copy(), MathTex("|"), pill.copy().scale(0.8),
            MathTex(r") \neq P("), person_green.copy(), MathTex("|"), no_pill.copy().scale(0.8), MathTex(")")
        ).arrange(RIGHT, buff=0.1).next_to(alt_hypothesis_txt, DOWN)
        alt_equation[0][0][0:2].set_color(YELLOW)

        drug_example = Group(drug_data, pill, no_drug_data, no_pill, legend, 
                             null_hypothesis_txt, alt_hypothesis_txt, null_equation, alt_equation)

        ############# types of tests
        tests_txt = VGroup()
        TESTS_TXT_FONT=44
        TESTS_TXT_BUFF=0.6

        tests_txt.add(
            Text("- Binomial test", font_size=TESTS_TXT_FONT).align_on_border(UL, buff=0.8)
        )

        for txt in ["Two-proportion z-test", "One/Two sample z/t-test", "Chi-square test", "Fisher's exact test", "ANOVA (F-test)"]:
            tests_txt.add(
                Text(f"- {txt}", font_size=TESTS_TXT_FONT).next_to(tests_txt[-1], DOWN, buff=TESTS_TXT_BUFF).align_to(tests_txt[-1], LEFT)
            )

        null_equation_blaze = Group(
            MathTex("H_0: P("), GenericImageMobject("assets/rod.png").scale(1), MathTex(") = \mu = 0.5")
        ).arrange(RIGHT, buff=0.1).align_on_border(RIGHT).set_y(tests_txt[0].get_y())

        null_equation_drug = Group(
            MathTex("H_0: P("), person_green.copy(), MathTex("|"), pill.copy().scale(0.8),
            MathTex(") = P("), person_green.copy(), MathTex("|"), no_pill.copy().scale(0.8), MathTex(")")
        ).arrange(RIGHT, buff=0.1).align_on_border(RIGHT).set_y(tests_txt[1].get_y())

        pmf_plot = PMFBarPlot.binom(
            n=100, p=0.5, width=7, height=4, gap = 0.05,
            alpha=1e-8, min_prob=0,
            x_label=Tex("$x$ (number of rods)", font_size = 48)
        )

        # p_def = Paragraph(
        #     Tex(r"$\mathbf{p} = $ probability of getting results"),
        #     Tex(r"at least as extreme as observed results"),
        #     Tex(r"given $H_0$ is true"),
        # ).align_on_border(DL, buff=0.7)

        p_def = Tex(
            r"""
            $p = $ probability of getting \\
            results at least as extreme \\
            as observed results, \\
            given $H_0$ is true
            """,
            tex_environment="flushleft"
        ).align_on_border(DR, buff=1).align_to(tests_txt[-1], DOWN)
        p_def[0][0].set_color(BLUE_TXT)

        #################################################################
        # Animation (1)                                                 #
        #################################################################
        # self.add(NumberPlane(
        #     background_line_style={
        #         "stroke_width": 2,
        #         "stroke_opacity": 0.6
        #     }).set_z_index(-1))
        # self.add(tests_txt, null_equation_blaze, null_equation_drug, p_def)

        self.play(
            Write(conclusion_txt)
        )

        self.wait()

        self.play(
            Unwrite(conclusion_txt, reverse=False)
        )

        self.wait(0.1)

        self.play(
            FadeIn(blaze_example)
        )

        self.wait()

        self.play(
            AnimationGroup(
                FadeOut(blaze_example),
                FadeIn(drug_example),
                lag_ratio=0.8
            )
        )

        self.wait()

        self.play(
            FadeOut(drug_example),
            FadeIn(null_equation_blaze)
        )

        self.wait(0.1)

        self.play(
            Write(tests_txt[0]),
            run_time=1
        )

        self.play(
            FadeIn(pmf_plot)
        )

        self.wait()

        self.play(
            FadeOut(pmf_plot),
            FadeIn(null_equation_drug)
        )

        self.wait()

        self.play(
            Write(tests_txt[1]),
            run_time=1
        )

        self.wait()

        self.play(
            Write(tests_txt[2:]),
            run_time=3
        )

        self.wait()

        self.play(
            Write(p_def),
            run_time=3
        )

        self.wait()
        
        self.play(
            FadeOut(*self.mobjects, shift=DOWN*0.2)
        )

        self.wait(0.1)






