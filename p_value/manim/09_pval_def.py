from manim import *
from probability_mobjects import *
from dudek_utils import *

class PvalDef(Scene):
    def construct(self):

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
        # p_value_definition[0][65:101].set_color(GREEN)

        p_value_definition2 = Tex(
            r"""
            \begin{flushleft}
            Just \textit{how lucky} our friend would have to \\
            be if they weren't cheating.
            \end{flushleft}
            """,
            font_size = 55
        ).set_y(-2).align_to(p_value_definition, LEFT)

        arrow = DoubleArrow(
            p_value_definition.get_edge_center(DOWN),
            p_value_definition.get_edge_center(DOWN) + DOWN*1.4,
            color = GREEN
        )

        rod = GenericImageMobject("assets/rod.png")
        red_x = GenericImageMobject("assets/red_x.png")

        data_graphic = BinomDataGraphic(67, 100, rod, red_x, width=3, nrow=10).move_to((0,0,0))
        data_txt = Text("Data (67/100)", color=WHITE, font_size=36).next_to(data_graphic, UP)
        data_txt[:4].set_color(ORANGE)
        data_txt[5:7].set_color(ORANGE)

        # probability_txt = Text("probability?", font_size=48).next_to(data_graphic, DOWN, buff=0.5)

        probability_eq = Group(
            MathTex("P(", font_size=52), rod.copy().scale(2), MathTex(r" \geq 67) \text{?}", font_size=52)
        ).arrange(RIGHT, buff=0.1).next_to(data_graphic, DOWN, buff=0.5)

        #################################################################
        # Animation (1)                                                 #
        #################################################################
        # Testing
        # self.add(NumberPlane(), Dot(ORIGIN))
        # self.add(p_value_definition, p_value_header, p_value_definition2, arrow)

        self.play(
            FadeIn(p_value_header, shift=DOWN*0.2, run_time=0.5),
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
            Write(p_value_definition2, run_time=3)
        )

        self.wait()

        self.play(
            p_value_definition2[0][34:55].animate.scale(1.2).set_color(GREEN),
            run_time=0.7
        )
        self.play(
            p_value_definition2[0][34:55].animate.scale(1/1.2),
            run_time=0.7
        )

        self.wait()

        self.play(
            Create(arrow),
            p_value_definition[0][65:101].animate.scale(1.2).set_color(GREEN),
            run_time=0.7
        )
        self.play(
            p_value_definition[0][65:101].animate.scale(1/1.2),
            run_time=0.7
        )

        self.wait()

        self.play(
            Indicate(p_value_definition[0][30:46]),
            run_time=2
        )

        self.wait()

        self.play(
            Indicate(p_value_definition2[0][4:12]),
            run_time=2
        )

        self.wait()

        self.play(
            FadeOut(*self.mobjects, shift=DOWN*0.1)
        )

        self.play(
            FadeIn(data_graphic, data_txt)
        )
        self.play(
            Write(VGroup(probability_eq[0], probability_eq[2])),
            FadeIn(probability_eq[1])
        )

        self.wait()

        self.play(
            FadeOut(*self.mobjects, shift=DOWN*0.1)
        )

        self.wait()

