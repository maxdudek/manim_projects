from manim import *
from probability_mobjects import *
from dudek_utils import *

class TestGoal(Scene):
    def construct(self):
        alex=GenericImageMobject("assets/alex.webp")
        alex.scale_to_fit_height(3.5).align_on_border(DL)

        big_bubble = GenericImageMobject("assets/thought_bubble_big.png").scale_to_fit_height(4.5).move_to((0,1.5,0))

        or_txt = Text("or", font_size=36).move_to(big_bubble).shift(UP*0.3)

        null_world = GenericImageMobject("assets/null_world.png").scale(0.5).next_to(or_txt, LEFT)
        alt_world = GenericImageMobject("assets/alt_world.png").scale(0.5).next_to(or_txt, RIGHT)

        steve_angel = GenericImageMobject("assets/steve_angel.png").scale(0.4).next_to(null_world, LEFT, buff=0)
        steve_devil = GenericImageMobject("assets/steve_devil.png").scale(0.4).next_to(alt_world, RIGHT, buff=0)

        null_equation = MathTex(r"\mu = 0.50", color = BLUE).next_to(null_world, DOWN)
        alt_equation = MathTex(r"\mu > 0.50", color = BLUE).next_to(alt_world, DOWN)

        rod = GenericImageMobject("assets/rod.png")
        red_x = GenericImageMobject("assets/red_x.png")

        data_graphic = BinomDataGraphic(67, 100, rod, red_x, width=2.5, nrow=10).move_to((4.5,-2,0))
        data_txt = Text("Data (67/100)", color=WHITE, font_size=36).next_to(data_graphic, UP)
        data_txt[:4].set_color(ORANGE)
        data_txt[5:7].set_color(ORANGE)

        evidence_txt = Text("evidence").next_to(data_graphic, LEFT, buff=2)

        arrow = Arrow(
            evidence_txt.get_edge_center(RIGHT),
            data_graphic.get_edge_center(LEFT),
            buff=0.2
        )

        #################################################################
        # Animation (1)                                                 #
        #################################################################
        # Testing
        # self.add(NumberPlane(), Dot(ORIGIN))
        # self.add(alex, big_bubble, or_txt, null_world, alt_world, steve_angel, steve_devil,
        #          null_equation, alt_equation, data_graphic, data_txt)
        
        self.play(
            FadeIn(alex, shift=DOWN*0.1)
        )

        self.wait()

        self.play(
            FadeIn(big_bubble, shift=UP*0.1),
            FadeIn(steve_angel, null_world, alt_world, steve_devil),
        )
        self.play(
            Write(or_txt)
        )

        self.wait()
        
        self.play(
            Write(null_equation)
        )

        self.wait()

        self.play(
            Write(alt_equation)
        )

        self.wait()

        self.play(
            FadeIn(data_graphic, data_txt)
        )

        self.wait()

        self.play(
            Create(arrow),
            Write(evidence_txt)
        )

        self.wait()

        self.play(
            FadeOut(*self.mobjects, shift=DOWN*0.1)
        )

        self.wait()
    
