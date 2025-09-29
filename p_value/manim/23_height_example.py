from manim import *
from probability_mobjects import *
from dudek_utils import *

class _23_height_example(Scene):
    def construct(self):

        continuous_txt = Text("continuous", slant=ITALIC).move_to((-1, 2.5, 0))

        decimal_number = DecimalNumber(1.00, num_decimal_places=3, font_size=60).move_to((3, 2.5, 0))
        decimal_tracker = ValueTracker(1.00)
        decimal_number.add_updater(lambda v: v.set_value(decimal_tracker.get_value()))

        person = SVGMobject("assets/person_white.svg").scale_to_fit_height(3.5).move_to((-4,0,0))

        brace = Brace(person, direction=RIGHT, sharpness=1, buff=0.3, stroke_width=1)

        height_txt = Tex("Height = ", font_size=60).next_to(brace, RIGHT).shift(UP*0.5)
        number_txt = Tex("5.814159265358979323846", font_size=60).next_to(height_txt, RIGHT)

        exact_prob_eq = Tex(r"P(height = 5.8141...) $\approx$ 0").move_to((1,-1.5,0))

        meaningless_txt = Text("meaningless", font_size=36, color=RED).next_to(exact_prob_eq, UP, buff=0.5).shift(RIGHT*2)
        arrow = Arrow(
            meaningless_txt.get_edge_center(LEFT),
            exact_prob_eq.get_edge_center(UP)+LEFT*0.5,
            color=RED
        )

        prob_geq = Tex(r"P(height $\geq$ 5.8141...) $\longrightarrow$ meaningful").align_to(exact_prob_eq, LEFT).set_y(-3)
        prob_geq[0][-10:].set_color(GREEN)

        #################################################################
        # Animation (1)                                                 #
        #################################################################
        # self.add(NumberPlane(
        #     background_line_style={
        #         "stroke_width": 2,
        #         "stroke_opacity": 0.6
        #     }))
        # self.add(continuous_txt, decimal_number, person, brace, height_txt, number_txt, 
        #          exact_prob_eq, meaningless_txt, arrow, prob_geq)
        # self.add(exact_prob_eq)
        # self.add(index_labels(exact_prob_eq[0]))


        self.play(
            Write(continuous_txt),
            run_time=0.8
        )

        self.wait()

        self.play(
            FadeIn(decimal_number),
            run_time=0.3
        )

        self.play(
            decimal_tracker.animate.set_value(4.726),
            run_time=3
        )

        self.play(
            FadeOut(decimal_number)
        )

        self.wait(0.2)

        self.play(
            FadeIn(person)
        )

        self.play(
            Create(brace),
            Write(height_txt)
        )

        self.wait(0.5)

        self.play(
            AddTextLetterByLetter(number_txt[0]),
            run_time=8
        )

        self.wait()

        self.play(
            FadeIn(exact_prob_eq[0][:9].copy(), exact_prob_eq[0][18]),
            Transform(number_txt[0][:6].copy(), exact_prob_eq[0][9:15]),
            Transform(number_txt[0][6:].copy(), exact_prob_eq[0][15:18]),
        )

        self.wait()

        self.play(
            Write(exact_prob_eq[0][19:]),
            run_time=0.6
        )

        self.wait()

        self.play(
            Write(meaningless_txt),
            GrowArrow(arrow)
        )

        self.wait()

        self.play(
            Write(prob_geq),
            run_time=1
        )

        self.wait()

        self.play(
            FadeOut(*self.mobjects, shift=DOWN*0.2)
        )

        self.wait(0.1)





