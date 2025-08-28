from manim import *
from probability_mobjects import *
from dudek_utils import *

class CollectSomeData(Scene):
    def construct(self):

        rod = GenericImageMobject("assets/rod.png")
        red_x = GenericImageMobject("assets/red_x.png")        

        png67 = GenericImageMobject("assets/rod_67.png").scale_to_fit_width(3-0.3).move_to((0,1,0))
        data_graphic = Group(png67, SurroundingRectangle(png67, color = WHITE, buff=0.2))
        data_txt = Text("Data (67/100)", color=WHITE, font_size=36).next_to(data_graphic, UP)
        data_txt[:4].set_color(ORANGE)
        data_txt[5:7].set_color(ORANGE)


        data_txt.add_updater(lambda d: d.next_to(data_graphic, UP))

        alex=GenericImageMobject("assets/alex.webp").move_to((-5.5,1,0))
        alex.scale_to_fit_height(3.5)

        bubble=GenericImageMobject("assets/thought_bubble_down_long.png").move_to((-3.5,-1.5,0))
        bubble.scale_to_fit_width(4)

        cheating_txt = Text("Cheating?", font_size=38).move_to((-3.45,-2.15,0))
        lucky_txt = Text("Lucky?", font_size=38).next_to(cheating_txt, DOWN, buff=0.2).align_to(cheating_txt, LEFT)

        #################################################################
        # Animation (1)                                                 #
        #################################################################
        # Testing
        # self.add(data_graphic, data_txt, alex, bubble, cheating_txt, lucky_txt)
        # self.wait()

        # Animation
        self.play(
            FadeIn(alex, shift=DOWN*0.5)
        )
        self.wait()
        self.play(
            Create(data_graphic[1]),
            FadeIn(png67),
            Write(data_txt)
        )
        self.wait()

        self.play(
            Circumscribe(data_txt[8:11], time_width=0.5)
        )

        self.wait()

        self.play(
            Circumscribe(data_txt[5:7], time_width=0.5)
        )

        self.wait()
        self.play(
            FadeIn(bubble, shift=DOWN*0.5),
            Write(cheating_txt)
        )
        self.wait()

        self.play(
            Write(lucky_txt)
        )
        self.wait()

        self.play(
            FadeOut(bubble, cheating_txt, lucky_txt, alex, shift=DOWN*0.5)
        )
        self.play(
            data_graphic.animate.move_to((0,-1.2,0)).scale(0.9)
        )
        self.wait()

        #################################################################
        # Slide 2                                                       #
        #################################################################

        # For testing
        # data_graphic.move_to((0,-1,0)).scale(0.5)
        # data_txt.next_to(data_graphic, UP)

        null_earth = GenericImageMobject("assets/earth.png").scale(2).move_to((-3.5, 2.5, 0))
        alt_earth = null_earth.copy().move_to((3.5, 2.5, 0))

        steve_angel = GenericImageMobject("assets/steve_angel.png").scale(0.5).next_to(null_earth, LEFT)
        steve_devil = GenericImageMobject("assets/steve_devil.png").scale(0.5).next_to(alt_earth, RIGHT)

        lucky_txt = Text("Lucky", font_size=36).next_to(Group(null_earth, steve_angel), DOWN)
        cheating_txt = Text("Cheating", font_size=36, color=YELLOW).next_to(Group(alt_earth, steve_devil), DOWN)

        null_spinner = Spinner(0.5).next_to(lucky_txt, DOWN).set_y(data_graphic.get_y()).scale(1.2)
        null_spinner.add_image(GenericImageMobject("assets/rod.png").scale(1.2))

        null_equation = Group(
            MathTex("P(", color=BLUE), GenericImageMobject("assets/rod.png").scale(1), MathTex(") = 0.5", color=BLUE)
        ).arrange(RIGHT, buff=0.1).next_to(null_spinner, DOWN)

        alt_spinner = Spinner(0.5).next_to(cheating_txt, DOWN).set_y(data_graphic.get_y()).scale(1.2)
        alt_spinner.add_image(GenericImageMobject("assets/rod.png").scale(1.2))

        alt_equation = Group(
            MathTex("P(", color=BLUE), GenericImageMobject("assets/rod.png").scale(1), MathTex(") > 0.5", color=BLUE)
        ).arrange(RIGHT, buff=0.1).next_to(alt_spinner, DOWN)

        null_arrow = Arrow(start = null_spinner.get_edge_center(RIGHT), 
                           end = data_graphic.get_edge_center(LEFT))
        null_q = Text("?", font_size=36).next_to(null_arrow, UP).shift(DOWN*0.2)

        alt_arrow = Arrow(start = alt_spinner.get_edge_center(LEFT), 
                           end = data_graphic.get_edge_center(RIGHT))
        alt_q = Text("?", font_size=36).next_to(alt_arrow, UP).shift(DOWN*0.2)

        hypothesis_txt = Text("Hypothesis", font_size=48).next_to(null_earth, RIGHT).set_x(0)
        testing_txt = Text("testing", font_size=48).next_to(hypothesis_txt, DOWN)

        hypotheses_arrows = VGroup(
            Arrow(start=hypothesis_txt.get_edge_center(LEFT), end = null_earth.get_edge_center(RIGHT)),
            Arrow(start=hypothesis_txt.get_edge_center(RIGHT), end = alt_earth.get_edge_center(LEFT))
        )

        #################################################################
        # Animation (2)                                                 #
        #################################################################

        # Testing
        # self.add(data_graphic, data_txt)
        # self.add(NumberPlane(), Dot(ORIGIN))
        # self.add(null_earth, alt_earth, steve_angel, steve_devil,
        #          lucky_txt, cheating_txt, null_spinner, null_equation, alt_spinner, alt_equation,
        #          null_arrow, null_q, alt_arrow, alt_q, hypothesis_txt, testing_txt, hypotheses_arrows)
        # self.wait()

        # Animation

        self.play(
            FadeIn(steve_devil, alt_earth, shift=DOWN*0.1),
            Write(cheating_txt)
        )

        self.wait()

        self.play(
            FadeIn(steve_angel, null_earth, shift=DOWN*0.1),
            Write(lucky_txt)
        )
        
        self.wait()

        self.play(
            FadeIn(null_spinner.circle, null_spinner.arrow, null_spinner.image, null_equation),
            Create(null_spinner.sector)
        )

        self.wait()

        self.play(
            Circumscribe(null_equation[2][0][-4:], time_width=0.5)
        )

        self.wait()

        self.play(
            FadeIn(alt_spinner.circle, alt_spinner.arrow, alt_spinner.image, alt_equation),
            Create(alt_spinner.sector)
        )

        self.play(
            alt_spinner.probability.animate.set_value(0.67)
        )
        self.wait()

        self.play(
            Circumscribe(alt_equation[2][0][-4:], time_width=0.5)
        )

        self.wait()

        self.play(
            Create(null_arrow),
            Write(null_q)
        )

        self.play(
            Create(alt_arrow),
            Write(alt_q)
        )

        self.wait()
        self.play(
            Write(hypothesis_txt),
            Create(hypotheses_arrows)
        )
        self.wait()
        self.play(
            Circumscribe(data_graphic[1], time_width=0.5)
        )

        self.wait()

        self.play(
            Write(testing_txt)
        )
        self.play(
            Circumscribe(Group(hypothesis_txt, testing_txt), time_width=0.5)
        )

        self.wait()

        self.play(
            FadeOut(*self.mobjects, shift=DOWN*0.1)
        )

        self.wait()

        
