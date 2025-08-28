from manim import *
from probability_mobjects import *
from dudek_utils import *

class CoinVsBlaze(Scene):
    def construct(self):

        null_world = GenericImageMobject("assets/null_world.png").scale(0.5).align_on_border(UP)

        eq_txt = MathTex("=", font_size = 72).move_to((0,-1,0))

        null_spinner = Spinner(0.5).scale(1.7).next_to(eq_txt, RIGHT, buff=0.5)
        null_spinner.add_image(GenericImageMobject("assets/rod.png").scale(1.7))

        coin_spinner = Spinner(0.5).scale(1.7).next_to(eq_txt, LEFT, buff=0.5)
        coin_spinner.add_image(GenericImageMobject("assets/heads.png").scale(1.7))

        steve_angel = GenericImageMobject("assets/steve_angel.png").scale(0.4).next_to(null_world, LEFT, buff=1)

        null_hypothesis_txt = Tex(r"null hypothesis").next_to(null_world, RIGHT, buff=0.5)

        brace = BraceBetweenPoints((-4,1,0), (4,1,0), direction=UP, sharpness=1).scale(1.5)

        blaze = GenericImageMobject("assets/blaze.png").scale_to_fit_height(1.5).move_to((5,0,0))

        coin_flip = GenericImageMobject("assets/coin_flip.png").scale_to_fit_height(1.5).move_to((-5,0,0))

        pmf_plot =  PMFBarPlot.binom(
            n=100, p=0.5, width=4.8, height=2.8, gap = 0.05,
            alpha=1e-7, min_prob=0,
            x_label=Tex("$x$ (number of heads)", font_size = 48)
        ).next_to(eq_txt, LEFT, buff=0.1).shift(DOWN*0.5)

        #################################################################
        # Animation (1)                                                 #
        #################################################################
        # Testing
        # self.add(NumberPlane(), Dot(ORIGIN))
        # self.add(null_world, eq_txt, null_spinner, steve_angel, null_hypothesis_txt, brace,coin_spinner,
        #          blaze, coin_flip)
        
        self.play(
            FadeIn(coin_flip, coin_spinner, shift=DOWN*0.1),
        )

        self.wait()

        self.play(
            Write(eq_txt),
            FadeIn(blaze, null_spinner, shift=DOWN*0.1),
        )

        self.wait()

        self.play(
            FadeIn(steve_angel, null_world, null_hypothesis_txt, brace, shift=DOWN*0.1),
        )

        self.wait()

        self.play(
            Circumscribe(coin_spinner, shape=Circle, time_width=0.5, buff=-0.6)
        )

        self.wait()

        self.play(
            Circumscribe(null_spinner, shape=Circle, time_width=0.5, buff=-0.6)
        )

        self.wait()

        self.play(
            FadeOut(coin_spinner, coin_flip, shift=DOWN*0.3),
            FadeIn(pmf_plot, shift=DOWN*0.3)
        )

        self.wait()

        self.play(
            FadeOut(*self.mobjects, shift=DOWN*0.1)
        )

        self.wait()
