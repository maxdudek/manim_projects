from manim import *
from probability_mobjects import *
from dudek_utils import *

class MinecraftExplanation(Scene):
    def construct(self):

        steve=GenericImageMobject("assets/steve.png").move_to((-5,0,0))
        steve.height=3.5

        blaze_pos=(-1.5,0,0)
        blaze=GenericImageMobject("assets/blaze.webp").move_to(blaze_pos)
        blaze.height=3.8

        spinner = Spinner(0.5).scale(2).move_to((4,0,0))
        spinner.add_image(GenericImageMobject("assets/rod.png").scale(1.75))
        spinner_text = Text("50/50 chance", color=BLUE, font_size=32).move_to(spinner.get_edge_center(UP)).shift(UP*0.5)

        arrow=Arrow(start=blaze.get_edge_center(RIGHT), end=spinner.get_edge_center(LEFT)+LEFT*0.1)

        skull=GenericImageMobject("assets/skull.png").move_to(arrow).shift(UP*0.5)
        skull.height=0.5

        dropped_rod = GenericImageMobject("assets/rod.png").move_to((-2.5,-3,0))
        dropped_rod.height=1

        dropped_x = GenericImageMobject("assets/red_x.png").move_to((-0.5,-3,0))
        dropped_x.height=1

        #################################################################
        # Animation (1)                                                 #
        #################################################################

        # self.add(steve, blaze, arrow, skull, spinner, spinner_text)

        self.play(
            FadeIn(steve, shift=DOWN*0.1)
        )

        self.wait()

        self.play(
            FadeIn(blaze, shift=DOWN*1)
        )

        self.wait()

        self.play(
            FadeIn(skull, shift=DOWN*0.1),
            Create(arrow)
        )

        self.play(
            FadeIn(spinner.circle, spinner.arrow, spinner.image),
            Create(spinner.sector),
            Write(spinner_text)
        )

        self.wait()

        self.play(
            spinner.spin(2),
            run_time=2
        )
        self.play(
            FadeOut(blaze, target_position=dropped_rod),
            FadeIn(dropped_rod, target_position=blaze)
        )

        self.wait()

        self.play(
            FadeIn(blaze.move_to(blaze_pos), shift=DOWN*1)
        )
        self.play(
            spinner.spin(-2.2),
            run_time=2.2
        )
        self.play(
            FadeOut(blaze, target_position=dropped_x),
            FadeIn(dropped_x, target_position=blaze)
        )

        self.wait()

        self.play(
            FadeOut(*self.mobjects, shift=DOWN*0.1)
        )

        self.wait()
        
