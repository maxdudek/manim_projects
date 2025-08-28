from manim import *
from probability_mobjects import *
from dudek_utils import *
import PIL

PIL.Image.MAX_IMAGE_PIXELS = 789605001

class AtLeastAsLucky(Scene):
    def construct(self):

        steve_angel_grid = GenericImageMobject("assets/steve_angel_grid.png", scale_to_resolution=2160)

        innocent_players_txt = Text("2500 innocent players", font_size=48).next_to(steve_angel_grid, UP, buff=0.5)

        at_least_as_lucky_txt = Text("At least as lucky as our friend", color=YELLOW, font_size=36).next_to(steve_angel_grid, DOWN, buff=0.5)

        rectangle = Rectangle(width=0.2, height=0.2, color=YELLOW, stroke_width=3).move_to((4.22,-2.09,0))

        arrow = Arrow(
            at_least_as_lucky_txt.get_edge_center(RIGHT),
            rectangle.get_edge_center(DOWN),
            buff=0.1
        )

        #################################################################
        # Animation (1)                                                 #
        #################################################################
        # Testing
        # self.add(NumberPlane(), Dot(ORIGIN))
        # self.add(steve_angel_grid, innocent_players_txt, at_least_as_lucky_txt, rectangle, arrow)

        self.play(
            FadeIn(steve_angel_grid),
            Write(innocent_players_txt)
        )

        self.wait()

        self.play(
            Create(rectangle)
        )

        self.play(
            Write(at_least_as_lucky_txt),
        )

        self.play(
            Create(arrow)
        )

        self.wait()

        self.play(
            FadeOut(*self.mobjects, shift=DOWN*0.1)
        )

        self.wait()



        

        