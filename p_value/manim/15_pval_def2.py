from manim import *
from probability_mobjects import *
from dudek_utils import *

class PvalDef2(Scene):
    def construct(self):

        alex=GenericImageMobject("assets/alex.webp").move_to((-5,-2,0)).scale_to_fit_height(3)

        p_value_header = Text("p-value:", weight = BOLD, font_size=48, color = BLUE).move_to((0,3,0))

        p_value_definition = Tex(
            r"""
            \begin{flushleft}
            The probability of getting a result \textit{at least}\\
            as extreme as the data that we see,\\
            given that the null hypothesis ($H_0$) is true.
            \end{flushleft}
            """,
            font_size = 55
        ).next_to(p_value_header, DOWN, buff=0.8)

        #################################################################
        # Animation (1)                                                 #
        #################################################################
        # Testing
        # self.add(NumberPlane(), Dot(ORIGIN))
        # self.add(alex, p_value_header, p_value_definition)

        self.play(
            FadeIn(alex, p_value_header, shift=DOWN*0.2, run_time=0.5),
            Write(p_value_definition, run_time=3)
        )

        self.wait()


        self.play(
            p_value_definition[0][65:101].animate.scale(1.2).set_color(GREEN),
            run_time=0.7
        )
        self.play(
            p_value_definition[0][65:101].animate.scale(1/1.2),
            run_time=0.7
        )

        self.wait()

        self.play(
            FadeOut(*self.mobjects, shift=DOWN*0.1)
        )

        self.wait()
