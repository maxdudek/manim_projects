from manim import *
from probability_mobjects import *
from dudek_utils import *

class _26_fail_to_reject(Scene):
    def construct(self):

        
        steve_devil = GenericImageMobject("assets/steve_devil.png").scale_to_fit_height(3).set_x(-3)
        alt_world = GenericImageMobject("assets/alt_world.png").scale(0.5).move_to(steve_devil).shift(LEFT*1.7)

        spinner = Spinner(0.6).scale(1.5).next_to(steve_devil, RIGHT, buff=0.5)
        spinner.add_image(GenericImageMobject("assets/rod.png").scale(1.5))

        mu_variable = Variable(0.6, MathTex(r"\mu", color=YELLOW)).next_to(spinner, UP)
        mu_variable.set_color(YELLOW)
        mu_variable.add_updater(lambda v: v.tracker.set_value(spinner.probability.get_value()))
        mu_variable.label[0][0].shift(DOWN*0.05)


        png51 = GenericImageMobject("assets/rod_51.png", scale_to_resolution=2160).set_x(4.5)
        data_graphic = Group(png51, SurroundingRectangle(png51, color = WHITE, buff=0.1))
        data_txt = Text("Data (51/100)", color=WHITE, font_size=36).next_to(data_graphic, UP)
        data_txt[:4].set_color(ORANGE)
        data_txt[5:7].set_color(ORANGE)

        pmf_plot = PMFBarPlot.binom(
            n=100, p=0.5, width=7, height=3, 
            gap=0.05, alpha=1e-7, min_prob=0, x_prime=51, x_prime_height_scale=1.1,
            x_label=Tex("$x$ (number of blaze rods)", font_size = 40)
        ).align_on_border(DL).shift(RIGHT*0.4)

        BLUE_TXT="#76C9DC"
        prob_eq = Variable(pbinom(51,n=100,p=0.5), label="p", num_decimal_places=3).move_to((1.1,-0.5,0))
        prob_eq.set_color(BLUE_TXT)

        alex=GenericImageMobject("assets/alex.webp").scale_to_fit_height(3.5).align_on_border(LEFT).shift(RIGHT*0.3).shift(DOWN*0.5)

        extreme_data_txt = Tex("Data = 500,001 / 1,000,000 rods = 0.500001").set_y(2)
        extreme_data_txt[0][5:12].set_color(ORANGE)
        what_if_txt = Tex(r"``But what if $\mu$ = 0.5000000001?''").set_y(-1)
        what_if_txt[0][10:24].set_color(YELLOW)

        #################################################################
        # Animation (1)                                                 #
        #################################################################
        # self.add(NumberPlane(
        #     background_line_style={
        #         "stroke_width": 2,
        #         "stroke_opacity": 0.6
        #     }))
        # self.add(alt_world, steve_devil, spinner, mu_variable)
        # self.add(data_graphic, data_txt)
        # self.add(pmf_plot, prob_eq)
        # self.add(alex, extreme_data_txt, what_if_txt)

        self.play(
            FadeIn(alt_world, steve_devil)
        )

        self.play(
            FadeIn(spinner),
            Write(mu_variable)
        )

        self.wait(0.5)

        self.play(
            spinner.probability.animate.set_value(0.51)
        )

        self.wait()

        self.play(
            FadeIn(data_graphic, data_txt)
        )

        self.wait()

        self.play(
            AnimationGroup(
                Group(alt_world, steve_devil, spinner, mu_variable).animate.scale(0.7).align_on_border(UP),
                FadeIn(pmf_plot),
                lag_ratio=0.5
            )
        )

        pmf_plot.x_prime_line.resume_updating()

        self.play(
            Create(pmf_plot.x_prime_line.reverse_points()),
            Write(prob_eq),
            run_time=0.8
        )

        self.play(
            FadeIn(pmf_plot.x_prime_label, shift=UP*0.5),
            run_time=0.1
        )

        self.wait()

        self.play(
            FadeOut(*self.mobjects, shift=DOWN*0.2)
        )

        self.play(
            FadeIn(alex),
            Write(extreme_data_txt),
            run_time=1
        )

        self.wait()

        self.play(
            Write(what_if_txt),
            run_time=1
        )

        self.wait()

        self.play(
            FadeOut(*self.mobjects, shift=DOWN*0.2)
        )

        self.wait(0.1)





