from manim import *
from probability_mobjects import *
from dudek_utils import *

class _30_false_positives(Scene):
    def construct(self):

        steve_angel = GenericImageMobject("assets/steve_angel.png")
        steve_20 = BinomDataGraphic(20, 20, steve_angel, steve_angel, width=8, nrow=4, 
                                    border = False, buffer_ratio=0.04).align_on_border(LEFT, buff=0.7)

        alex = GenericImageMobject("assets/alex_flipped.png").scale_to_fit_height(3).move_to((3.5,-2.2,0))

        red_circle = Circle(0.8, color=RED).move_to(steve_20.coord2image(2,4))

        cheater_txt = Text("Cheater!\n(False Positive)", color=RED, font_size=24, line_spacing=0.5).next_to(red_circle).shift(DOWN*0.2)

        eq = VGroup()

        eq.add( # 0
            MathTex(r"P(\text{FP}) = P(p \leq \alpha) = \alpha").move_to((3,2.8,0))
        )
        eq[-1][0][2:4].set_color(RED)
        eq[-1][0][8].set_color(BLUE_TXT)
        eq[-1][0][10].set_color(PROB_PINK)
        eq[-1][0][-1].set_color(PROB_PINK)

        eq.add( # 1
            MathTex(r"P(p \leq 0.05) = 0.05 ~(1 \text{ in } 20)").next_to(eq[-1], DOWN, buff=0.3).align_to(eq[-1], LEFT)
        )
        eq[-1][0][2].set_color(BLUE_TXT)
        eq[-1][0][4:8].set_color(PROB_PINK)
        eq[-1][0][10:14].set_color(PROB_PINK)

        eq.add( # 2
            Tex(r"$m$ independent tests in $H_0$:").next_to(eq[-1], DOWN, buff=0.6).align_to(eq[-1], LEFT)
        )

        eq.add( # 3
            Tex(r"E[\#FP] $= m \alpha$").next_to(eq[-1], DOWN, buff=0.3)
        )
        eq[-1][0][3:5].set_color(RED)
        eq[-1][0][-1].set_color(PROB_PINK)

        #################################################################
        # Animation (1)                                                 #
        #################################################################
        # self.add(NumberPlane(
        #     background_line_style={
        #         "stroke_width": 2,
        #         "stroke_opacity": 0.6
        #     }).set_z_index(-1))
        
        # self.add(steve_20, alex, red_circle, cheater_txt, eq)

        self.play(
            FadeIn(alex),
            Write(eq[:2])
        )

        self.play(
            steve_20.create_by_index(lag_ratio = 0.03),
            run_time=1
        )

        self.play(
            Create(red_circle),
            AddTextLetterByLetter(cheater_txt),
            run_time=0.8
        )

        self.wait()

        self.play(
            Write(eq[2])
        )

        self.play(
            Write(eq[3])
        )

        self.wait()

        self.play(
            FadeOut(*self.mobjects, shift=DOWN*0.2)
        )

        self.wait(0.1)





