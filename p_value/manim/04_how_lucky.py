from manim import *
from probability_mobjects import *
from dudek_utils import *

class HowLucky(Scene):
    def construct(self):

        rod = GenericImageMobject("assets/rod.png")
        red_x = GenericImageMobject("assets/red_x.png")

        
        # data_graphic = BinomDataGraphic(67, 100, rod, red_x, width=3, nrow=10).move_to((0,1,0))
        png67 = GenericImageMobject("assets/rod_67.png").scale_to_fit_width(3-0.3).move_to((0,1,0))
        data_graphic = Group(png67, SurroundingRectangle(png67, color = WHITE, buff=0.2))
        
        data_txt = Text("Data (67/100)", color=WHITE, font_size=36).next_to(data_graphic, UP)
        data_txt[:4].set_color(ORANGE)
        data_txt[5:7].set_color(ORANGE)

        alex=GenericImageMobject("assets/alex.webp").move_to((-5.5,1,0))
        alex.scale_to_fit_height(3.5)

        bubble=GenericImageMobject("assets/thought_bubble_down.png").move_to((-3.5,-1.5,0))
        bubble.scale_to_fit_width(4)

        cheating_lucky_txt = Text("Cheating?\nLucky?", font_size=38)
        cheating_lucky_txt.move_to((-3.4,-1.9,0))

        bubble2 = GenericImageMobject("assets/thought_bubble_right.png"
                             ).scale_to_fit_width(4.5).next_to(bubble, RIGHT).shift(DOWN*0.5)

        how_lucky_txt = MarkupText("<i>How lucky</i>\nwould they\nhave to be?", font_size=32).move_to((1.3,-1.9,0))

        p_value_txt = Tex("$p$-value", color = BLUE, font_size=60).next_to(how_lucky_txt, RIGHT).shift(RIGHT*2)

        double_arrow = DoubleArrow(start = how_lucky_txt.get_edge_center(RIGHT),
                            end = p_value_txt.get_edge_center(LEFT))
        
        steve_angel = GenericImageMobject("assets/steve_angel.png"
        ).scale_to_fit_height(3).next_to(data_graphic, RIGHT, buff=1).shift(UP*1)

        possible_txt = Text("possible").next_to(steve_angel, DOWN)

        arrow = Arrow(
            steve_angel.get_edge_center(LEFT),
            data_graphic.get_edge_center(RIGHT),
            buff=0.1
        )

        #################################################################
        # Animation (1)                                                 #
        #################################################################
        # Testing
        # self.add(NumberPlane(), Dot(ORIGIN))
        # self.add(data_graphic, data_txt, alex, bubble, cheating_lucky_txt, bubble2, 
        #          how_lucky_txt, p_value_txt, double_arrow)
        # self.wait()

        self.play(
            FadeIn(alex, bubble, cheating_lucky_txt, shift=DOWN*0.3),
            FadeIn(png67, data_txt),
            Create(data_graphic[1])
        )

        self.wait()

        self.play(
            FadeIn(steve_angel, possible_txt, shift=DOWN*0.3),
            Create(arrow)
        )

        self.wait()

        self.play(
            FadeOut(steve_angel, possible_txt, arrow, shift=DOWN*0.1)
        )

        self.wait()

        self.play(
            FadeIn(bubble2, shift=RIGHT*0.1),
            Write(how_lucky_txt)
        )

        self.wait()

        self.play(
            FadeIn(double_arrow, shift=DOWN*0.1),
            Write(p_value_txt)
        )
        self.wait()

        self.play(
            FadeOut(data_graphic, data_txt, bubble, cheating_lucky_txt, bubble2, 
                    how_lucky_txt, p_value_txt, double_arrow, shift=DOWN*0.5),
            alex.animate.move_to((-4.5,-2,0))
        )

        #################################################################
        # Slide 2                                                       #
        #################################################################

        # For testing
        alex.move_to((-4.5,-2,0))

        person_green = GenericImageMobject("assets/person_green.png")
        person_white = GenericImageMobject("assets/person_white.png")

        drug_data = BinomDataGraphic(38, 48, person_white.copy(), person_white.copy(), 
                                     width=3.5, ncol=10).move_to((0,0.5,0))
        pill = GenericImageMobject("assets/pill.png").scale(2).next_to(drug_data, UP)
        
        no_drug_data = BinomDataGraphic(21, 48, person_white.copy(), person_white.copy(), 
                                        width=3.5, ncol=10).next_to(drug_data, RIGHT)
        no_pill = Group(
            GenericImageMobject("assets/pill.png").scale(2),
            GenericImageMobject("assets/dont.png").scale(0.4)
        ).next_to(no_drug_data, UP).set_y(pill.get_y())

        legend = Group(
            person_green.copy().scale_to_fit_height(drug_data[1].height),
            Text("= recovered", font_size=32)
        ).arrange(RIGHT, buff=0.2).next_to(Group(drug_data, no_drug_data), DOWN)
        

        bubble_up = GenericImageMobject("assets/thought_bubble_up.png"
                               ).scale_to_fit_height(2).next_to(alex, UP).shift(RIGHT*0.3)
        
        lucky_txt = Text("Lucky?", font_size=36).move_to((-4.2,1.2,0))

        p_value_txt2 = p_value_txt.copy().move_to((-1,-3,0))

        how_lucky_txt = Text('"How lucky"?', font_size=32).move_to((4,-3,0))

        double_arrow = DoubleArrow(start = p_value_txt2.get_edge_center(RIGHT),
                            end = how_lucky_txt.get_edge_center(LEFT))

        #################################################################
        # Animation (2)                                                 #
        #################################################################

        # Testing
        # self.add(NumberPlane(), Dot(ORIGIN))
        # self.add(alex, bubble_up, lucky_txt, drug_data, no_drug_data, pill, no_pill, legend,
        #          p_value_txt2, how_lucky_txt, double_arrow)
        # self.wait()

        self.wait()

        self.play(
            FadeIn(pill, drug_data)
        )

        self.wait()

        self.play(
            FadeIn(no_pill, no_drug_data)
        )

        self.wait()

        self.remove(drug_data)
        drug_data = BinomDataGraphic(38, 48, person_green.copy(), person_white.copy(), 
                                     width=drug_data.width, ncol=10).move_to(drug_data)
        self.add(drug_data)

        self.remove(no_drug_data)
        no_drug_data = BinomDataGraphic(21, 48, person_green.copy(), person_white.copy(), 
                                     width=no_drug_data.width, ncol=10).move_to(no_drug_data)
        self.add(no_drug_data)
        self.add(legend)

        self.wait()

        self.play(
            Circumscribe(drug_data, time_width=0.5)
        )

        self.wait()

        self.play(
            FadeIn(bubble_up, shift=UP*0.2),
            Write(lucky_txt)
        )

        self.wait()

        self.play(
            Write(p_value_txt2)
        )

        self.wait()

        self.play(
            Create(double_arrow),
            Write(how_lucky_txt)
        )

        self.wait()

        self.play(
            FadeOut(*self.mobjects, shift=DOWN*0.1)
        )

        self.wait()
