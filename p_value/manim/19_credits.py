from manim import *
from probability_mobjects import *
from dudek_utils import *
from random import random, seed

class Credits(Scene):
    def construct(self):
        
        music_by_txt = Text("Music by Vincent Rubinetti", font_size=24).align_on_border(DL, buff=0.8)

        video_by_txt = Text("Video by Max Dudek", font_size=36, color=PURPLE_A).next_to(music_by_txt, UP, buff=0.3).align_on_border(LEFT, buff=0.8)

        part_2_txt = Text("Part 2:", font_size=36).next_to(video_by_txt, UP).align_on_border(UP, buff=0.8)

        rectangle = RoundedRectangle(
            width = video_by_txt.width,
            height = 3,
        ).next_to(part_2_txt, DOWN, buff=0.5)

        TBD_txt = Text("TBD", font_size=24).move_to(rectangle)

        steve_devil = GenericImageMobject("assets/steve_devil.png").scale_to_fit_height(2.8).move_to((0,0,0))

        alt_spinner = Spinner(0.6).scale(1.5).next_to(steve_devil, RIGHT, buff=2.3)
        alt_spinner.add_image(GenericImageMobject("assets/rod.png").scale(1.5))

        x = (steve_devil.get_edge_center(RIGHT)[0] + alt_spinner.get_edge_center(LEFT)[0]) / 2
        blaze_spot = (x,0,0)

        blaze = GenericImageMobject("assets/blaze.png").scale_to_fit_height(2).move_to(blaze_spot)

        rod = GenericImageMobject("assets/rod.png").scale(1.5).move_to(blaze_spot)

        def blaze_kill():
            spin = 3 + random()

            blaze.set_y(6)
            rod.move_to(blaze_spot)
            self.add(blaze)
            self.play(
                blaze.animate.move_to(blaze_spot)
            )
            self.play(
                alt_spinner.spin(spin),
                run_time = spin
            )
            self.wait(0.5)

            drop = (alt_spinner.angle/TAU)<0.6
            
            if drop:
                self.play(
                    FadeOut(blaze, shift=DOWN*0.1, run_time=0.5),
                    Succession(
                        FadeIn(rod, run_time=0.2),
                        rod.animate.shift(DOWN*6)
                    )
                )
                self.remove(rod)
            else:
                self.play(
                    FadeOut(blaze, shift=DOWN*0.1),
                )


        #################################################################
        # Animation (1)                                                 #
        #################################################################
        # Testing
        # self.add(NumberPlane(), Dot(ORIGIN))
        # self.add(music_by_txt, video_by_txt, part_2_txt, rectangle, TBD_txt, 
        #          steve_devil, alt_spinner)

        self.play(
            FadeIn(steve_devil, alt_spinner, shift=DOWN*0.1),
            Write(VGroup(video_by_txt, music_by_txt)),
            Write(VGroup(part_2_txt, TBD_txt)),
            Create(rectangle)
        )

        self.wait()

        seed(1)
        for i in range(10):        
            blaze_kill()

