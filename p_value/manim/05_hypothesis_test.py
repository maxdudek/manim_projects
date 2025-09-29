from manim import *
from probability_mobjects import *
from dudek_utils import *

class HypothesisTest(Scene):
    def construct(self):

        hypothesis_testing_txt = Text("Hypothesis testing", font_size=60)

        dividing_line = Line(
            start=self.camera.frame_center + UP*self.camera.frame_height/2, 
            end = self.camera.frame_center + DOWN*self.camera.frame_height/2
        )

        steve_angel = GenericImageMobject("assets/steve_angel.png").scale(0.5).align_on_border(UL)
        steve_devil = GenericImageMobject("assets/steve_devil.png").scale(0.5).align_on_border(UR).shift(RIGHT*0.1)

        lucky_txt = Text(
            "Lucky", font_size=48
        ).move_to(self.camera.frame_center + LEFT*self.camera.frame_width/4).align_on_border(UP)
        cheating_txt = Text(
            "Cheating", font_size=48, color=YELLOW
        ).move_to(self.camera.frame_center + RIGHT*self.camera.frame_width/4).align_on_border(UP)

        null_spinner = Spinner(0.5).next_to(lucky_txt, DOWN).scale(1.7).set_x(lucky_txt.get_x()).set_y(0)
        null_spinner.add_image(GenericImageMobject("assets/rod.png").scale(1.7))

        null_equation = Group(
            MathTex("P(", color=BLUE), GenericImageMobject("assets/rod.png").scale(1), MathTex(") = \mu = 0.5", color=BLUE)
        ).arrange(RIGHT, buff=0.1).next_to(null_spinner, DOWN)

        alt_spinner = Spinner(0.5).next_to(cheating_txt, DOWN).scale(1.7).set_x(cheating_txt.get_x()).set_y(0)
        alt_spinner.add_image(GenericImageMobject("assets/rod.png").scale(1.7))

        alt_equation = Group(
            MathTex("P(", color=BLUE), GenericImageMobject("assets/rod.png").scale(1), MathTex(") = \mu > 0.5", color=BLUE)
        ).arrange(RIGHT, buff=0.1).next_to(alt_spinner, DOWN)

        null_hypothesis_txt = Tex(
            r"\textit{null} hypothesis ($H_0$)"
        ).align_on_border(DOWN).set_x(lucky_txt.get_x())

        alt_hypothesis_txt = Tex(
            r"\textit{alternative} hypothesis ($H_1$)"
        ).align_on_border(DOWN).set_x(cheating_txt.get_x())
        alt_hypothesis_txt[0][0:11].set_color(YELLOW)
        alt_hypothesis_txt[0][22:24].set_color(YELLOW)


        #################################################################
        # Animation (1)                                                 #
        #################################################################
        # Testing
        # self.add(NumberPlane(), Dot(ORIGIN))
        # self.add(dividing_line, steve_angel, steve_devil, lucky_txt, cheating_txt,
        #          null_spinner, null_equation, alt_spinner, alt_equation,
        #          null_hypothesis_txt, alt_hypothesis_txt)

        self.play(
            Write(hypothesis_testing_txt)
        )

        self.wait()

        self.play(
            Unwrite(hypothesis_testing_txt, reverse=False)
        )

        self.wait()

        self.play(
            Create(dividing_line),
            FadeIn(steve_angel, shift=DOWN*0.3),
            Write(lucky_txt)
        )

        self.wait()

        self.play(
            FadeIn(steve_devil, shift=DOWN*0.3),
            Write(cheating_txt)
        )

        self.wait()

        self.play(
            FadeIn(null_spinner.circle, null_spinner.arrow, null_spinner.image),
            Create(null_spinner.sector),
            FadeIn(alt_spinner.circle, alt_spinner.arrow, alt_spinner.image),
            Create(alt_spinner.sector),
            run_time=1
        )

        self.wait()

        self.play(
            Circumscribe(null_spinner, time_width=0.5, shape=Circle, buff=-0.6)
        )

        self.wait()

        self.play(
            alt_spinner.probability.animate.set_value(0.67),
            Circumscribe(alt_spinner, time_width=0.5, shape=Circle, buff=-0.6)
        )

        self.wait()

        self.play(
            FadeIn(null_equation, alt_equation, shift=DOWN*0.3)
        )

        self.wait()

        self.play(
            Indicate(null_equation[2][0][2]),
            Indicate(alt_equation[2][0][2]),
            run_time=2
        )

        self.wait()

        self.play(
            Circumscribe(null_equation[2][0][2:], time_width=0.5)
        )
        self.wait()
        self.play(
            Circumscribe(alt_equation[2][0][2:], time_width=0.5)
        )
        self.wait()

        self.play(
            Write(null_hypothesis_txt)
        )
        
        self.wait()

        self.play(
            Write(alt_hypothesis_txt)
        )

        self.wait()

        self.play(
            FadeOut(*self.mobjects, shift=DOWN*0.1)
        )
        
        self.wait()

        