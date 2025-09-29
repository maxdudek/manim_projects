from manim import *
from probability_mobjects import *
from dudek_utils import *

class _24_intuitive_answer(Scene):
    def construct(self):

        alex=GenericImageMobject("assets/alex.webp").scale_to_fit_height(3.5).move_to((-5,0,0))

        p_eq_correct = VGroup(
            MathTex(r"p ="),
            MathTex(r"P(X\geq"), 
            MathTex(r"67", color=ORANGE),
            MathTex(r")"),
        ).arrange(RIGHT, buff=0.15).scale(1.3).set_y(2)
        p_eq_correct[1][0][-1].shift(LEFT*0.05)
        p_eq_correct[0][0][0].set_color(BLUE_TXT)

        p_eq_incorrect = VGroup(
            MathTex(r"p =", color=LIGHT_PINK),
            MathTex(r"P(X = ", color=LIGHT_PINK), 
            MathTex(r"67", color=LIGHT_PINK),
            MathTex(r")", color=LIGHT_PINK),
        ).arrange(RIGHT, buff=0.15).scale(1.3).next_to(p_eq_correct, DOWN, buff=1)

        rect_p_eq_correct = SurroundingRectangle(p_eq_correct, buff=0.2, color=GREEN)

        why_not_txt = Text("why not?", font_size=36, color=LIGHT_PINK).next_to(p_eq_incorrect, DOWN, buff=0.4)

        if_h0_txt = Tex("If $H_0$ is true:").align_to(p_eq_incorrect, LEFT).set_y(-2)
        prob_eq = Tex("P(wrong significant result)").move_to((-2.5, -2.8, 0))
        prob_eq[0][2:-1].set_color(RED)
        significance_threshold_txt = Tex("= significance threshold").next_to(prob_eq, RIGHT)
        

        #################################################################
        # Animation (1)                                                 #
        #################################################################
        # self.add(NumberPlane(
        #     background_line_style={
        #         "stroke_width": 2,
        #         "stroke_opacity": 0.6
        #     }))
        # self.add(alex, p_eq_correct, p_eq_incorrect, rect_p_eq_correct, why_not_txt,
        #          if_h0_txt, prob_eq, significance_threshold_txt)

        self.play(
            FadeIn(alex, p_eq_correct, p_eq_incorrect, why_not_txt)
        )

        self.play(
            Create(rect_p_eq_correct)
        )

        self.wait()

        self.play(
            Write(if_h0_txt),
            run_time=0.6
        )

        self.play(
            Write(prob_eq),
            run_time=0.8
        )

        self.wait()

        self.play(
            Indicate(rect_p_eq_correct)
        )
        
        self.wait()

        self.play(
            Write(significance_threshold_txt),
            run_time=0.8
        )

        self.wait()

        self.play(
            FadeOut(*self.mobjects, shift=DOWN*0.2)
        )

        self.wait(0.1)





