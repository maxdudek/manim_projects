from manim import *
from probability_mobjects import *
from dudek_utils import *

class NullVsAlt(Scene):
    def construct(self):
        dividing_line = Line(
            start=self.camera.frame_center + UP*self.camera.frame_height/2, 
            end = self.camera.frame_center + DOWN*self.camera.frame_height/2
        )

        null_hypothesis_txt = Tex(
            r"null hypothesis ($H_0$)"
        ).move_to(self.camera.frame_center + LEFT*self.camera.frame_width/4).align_on_border(UP)

        alt_hypothesis_txt = Tex(
            r"alternative hypothesis ($H_1$)"
        ).move_to(self.camera.frame_center + RIGHT*self.camera.frame_width/4).align_on_border(UP)
        alt_hypothesis_txt[0][0:11].set_color(YELLOW)
        alt_hypothesis_txt[0][22:24].set_color(YELLOW)

        null_spinner = Spinner(0.5).next_to(null_hypothesis_txt, DOWN).scale(1.7).set_x(null_hypothesis_txt.get_x()).set_y(1)
        null_spinner.add_image(GenericImageMobject("assets/rod.png").scale(1.7))

        null_equation = Group(
            MathTex("P(", color=BLUE), GenericImageMobject("assets/rod.png").scale(1), MathTex(") = \mu = 0.5", color=BLUE)
        ).arrange(RIGHT, buff=0.1).next_to(null_spinner, DOWN)

        alt_spinner = Spinner(0.6).next_to(alt_hypothesis_txt, DOWN).scale(1.7).set_x(alt_hypothesis_txt.get_x()).set_y(1)
        alt_spinner.add_image(GenericImageMobject("assets/rod.png").scale(1.7))

        steve_angel = GenericImageMobject("assets/steve_angel.png").scale(0.4).next_to(null_spinner, LEFT, buff=0)
        steve_devil = GenericImageMobject("assets/steve_devil.png").scale(0.4).next_to(alt_spinner, LEFT, buff=0)

        alt_equation = Group(
            MathTex("P(", color=BLUE), GenericImageMobject("assets/rod.png").scale(1), MathTex(") = \mu > 0.5", color=BLUE)
        ).arrange(RIGHT, buff=0.1).next_to(alt_spinner, DOWN)

        two_rod_equation = Group(
            MathTex("P(", color=BLUE), 
            BinomDataGraphic(2, 2, GenericImageMobject("assets/rod.png"), GenericImageMobject("assets/red_x.png"), buffer_ratio=0.001, width=1.2, ncol=2),
            MathTex(r") = \mu \times \mu = 0.25", color = BLUE)
        ).arrange(RIGHT, buff=0.1).next_to(null_spinner, DOWN).set_y(-3)

        mu_variable = Variable(0.6, MathTex("\mu"))
        mu_variable.add_updater(lambda v: v.tracker.set_value(alt_spinner.probability.get_value()))
        mu_equation = VGroup(
            mu_variable, Tex("?")
        ).arrange(RIGHT, buff=0.1).set_x(alt_spinner.get_x()+1.3).set_y(two_rod_equation.get_y())

        mu_arrow = Arrow(
            start = mu_variable.label[0][0].get_edge_center(UP),
            end = alt_equation[2][0][2].get_edge_center(DOWN)
        )

        #################################################################
        # Animation (1)                                                 #
        #################################################################
        # Testing
        # self.add(NumberPlane(), Dot(ORIGIN))
        # self.add(dividing_line, steve_angel, steve_devil,
        #          null_spinner, null_equation, alt_spinner, alt_equation,
        #          null_hypothesis_txt, alt_hypothesis_txt, two_rod_equation, mu_equation, mu_arrow)
        
        self.play(
            Create(dividing_line),
            Write(null_hypothesis_txt),
            Write(alt_hypothesis_txt),
            FadeIn(steve_angel, steve_devil, shift=DOWN*0.1)
        )

        self.play(
            FadeIn(null_spinner.circle, null_spinner.arrow, null_spinner.image, null_equation),
            Create(null_spinner.sector),
            FadeIn(alt_spinner.circle, alt_spinner.arrow, alt_spinner.image, alt_equation),
            Create(alt_spinner.sector),
            run_time=2
        )

        self.wait()

        self.play(
            Circumscribe(alt_hypothesis_txt, time_width=0.5)
        )

        self.wait()

        self.play(
            Circumscribe(alt_equation[2][0][2:], time_width=0.5)
        )

        self.wait()

        self.play(
            Write(mu_equation),
            Create(mu_arrow)
        )

        self.wait()

        self.play(
            alt_spinner.probability.animate.set_value(0.85),
            run_time=2
        )

        self.wait()

        self.play(
            Circumscribe(null_hypothesis_txt, time_width=0.5)
        )

        self.wait()

        self.play(
            Circumscribe(null_equation[2][0][2:], time_width=0.5)
        )

        self.wait()

        self.play(
            FadeIn(two_rod_equation[1]),
            Write(VGroup(two_rod_equation[0], two_rod_equation[2]))
        )

        self.wait()

        self.play(
            Circumscribe(two_rod_equation[2][0][-4:], time_width=0.5)
        )

        self.wait()

        self.play(
            Circumscribe(null_hypothesis_txt, time_width=0.5)
        )

        self.wait()

        self.play(
            FadeOut(*self.mobjects, shift=DOWN*0.1)
        )

        self.wait()
        


