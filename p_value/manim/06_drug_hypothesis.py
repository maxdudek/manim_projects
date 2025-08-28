from manim import *
from probability_mobjects import *
from dudek_utils import *

class DrugHypothesis(Scene):
    def construct(self):
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

        #################################################################
        # Animation (1)                                                 #
        #################################################################
        # Testing
        # self.add(NumberPlane(), Dot(ORIGIN))
        # self.add(drug_data, pill, no_drug_data, no_pill, legend, 
        #          null_hypothesis_txt, null_equation, alt_hypothesis_txt, alt_equation)
        

        self.play(
            FadeIn(drug_data, pill, no_drug_data, no_pill, legend, shift=DOWN*0.1)
        )

        self.wait()

        self.play(
            Write(null_hypothesis_txt),
            FadeIn(null_equation, shift=DOWN*0.1)
        )

        self.wait()

        self.play(
            Indicate(null_equation[4][0][1]),
            run_time=2
        )

        self.wait()

        self.play(
            Write(alt_hypothesis_txt),
            FadeIn(alt_equation, shift=DOWN*0.1)
        )

        self.wait()

        self.play(
            Indicate(alt_equation[4][0][1:3]),
            run_time=2
        )

        self.wait()

        self.play(
            FadeOut(*self.mobjects, shift=DOWN*0.1)
        )

        self.wait()
