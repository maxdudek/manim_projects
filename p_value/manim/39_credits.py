from manim import *
from probability_mobjects import *
from dudek_utils import *
from random import random, seed

class _39_credits(Scene):
    def construct(self):
        music_by_txt = Text("Music by Vincent Rubinetti", font_size=24).align_on_border(DL, buff=0.8)

        video_by_txt = Text("Video by Max Dudek", font_size=36, color=PURPLE_A).next_to(music_by_txt, UP, buff=0.3).align_on_border(LEFT, buff=0.8)

        alex_devil = GenericImageMobject("assets/alex_devil.png").scale_to_fit_height(2.8).move_to((0,0,0))

        spinner_FP = Spinner(0.1, PROB_PINK, clockwise=True).scale(1.5).next_to(alex_devil, RIGHT, buff=2.3)
        spinner_FP.add_image(Text("TN", color=GREEN, font_size=36), angle=210*DEGREES)
        spinner_FP.add_image(Text("FP", color=RED_E, font_size=36), angle="prob", r=0.35)

        x = (alex_devil.get_edge_center(RIGHT)[0] + spinner_FP.get_edge_center(LEFT)[0]) / 2
        steve_spot = (x,0,0)

        steve_angel = GenericImageMobject("assets/steve_angel.png").scale_to_fit_height(2.3).move_to(steve_spot)

        bubble = SVGMobject("assets/speech_bubble_left.svg", stroke_width=4).scale_to_fit_width(5.5).next_to(alex_devil, LEFT).shift(UP*1.4+RIGHT*0.8)
        cheater_txt = Text("Significant, cheater!", font_size=24, color=RED).move_to(bubble).shift(UP*0.1)

        links_txt = Text("Links to further viewing and\nanimation code in the description!", font_size=32).align_on_border(UL, buff=0.8)

        def perform_test():
            significant = (spinner_FP.angle/TAU)>=0.9 # current

            spin = 3 + random()

            steve_angel.set_y(6)
            self.add(steve_angel)

            if (significant):
                self.play(
                    steve_angel.animate.move_to(steve_spot),
                    FadeOut(bubble, cheater_txt)
                )
            else:
                self.play(
                    steve_angel.animate.move_to(steve_spot)
                )
            
            self.play(
                spinner_FP.spin(spin),
                run_time = spin
            )
            self.wait(0.5)

            significant = (spinner_FP.angle/TAU)>=0.9
            
            if significant:
                self.play(
                    FadeOut(steve_angel),
                    Write(cheater_txt),
                    Create(bubble),
                    run_time=0.8
                )
                self.wait(1)
            else:
                self.play(
                    FadeOut(steve_angel),
                )


        #################################################################
        # Animation (1)                                                 #
        #################################################################
        # Testing
        # self.add(NumberPlane(), Dot(ORIGIN))
        # self.add(music_by_txt, video_by_txt, links_txt)
        # self.add(alex_devil, spinner_FP, bubble, cheater_txt)

        self.play(
            FadeIn(alex_devil, spinner_FP, shift=DOWN*0.1),
            Write(VGroup(video_by_txt, music_by_txt)),
        )

        self.play(
            Write(links_txt),
            run_time=1.4
        )

        self.wait()

        seed(1)
        for i in range(10):        
            perform_test()






