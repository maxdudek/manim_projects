from manim import *
from probability_mobjects import *
from dudek_utils import *

class AltProblems(Scene):
    def construct(self):
        alt_world = GenericImageMobject("assets/alt_world.png").scale(0.5).align_on_border(UP)

        steve_devil = GenericImageMobject("assets/steve_devil.png").scale(0.4).next_to(alt_world, LEFT, buff=1)

        alt_hypothesis_txt = Tex(r"alternate hypothesis").next_to(alt_world, RIGHT, buff=0.5)
        alt_hypothesis_txt[0][0:9].set_color(YELLOW)

        alt_spinner = Spinner(0.6).scale(1.6).next_to(alt_hypothesis_txt, DOWN, buff=2.2)
        alt_spinner.add_image(GenericImageMobject("assets/rod.png").scale(1.6))

        mu_variable = Variable(alt_spinner.probability.get_value(), MathTex("\mu"))
        mu_variable.add_updater(lambda v: v.tracker.set_value(alt_spinner.probability.get_value()))
        mu_equation = VGroup(
            mu_variable, Tex("?")
        ).arrange(RIGHT, buff=0.1).next_to(alt_spinner, UP, buff=0.1)

        brace = BraceBetweenPoints((-4,1,0), (4,1,0), direction=UP, sharpness=1).scale(1.5)


        x_values = np.array(list(range(30,100)))
        y_values = np.array([0.01]*len(x_values))
        pmf_plot = PMFBarPlot(
            x_values, y_values,
            width=6.8, height=2.8, gap=0.05, max_y=0.1,
            x_label=Tex("$x$ (number of blaze rods)", font_size = 40)
        ).next_to(alt_spinner, LEFT, buff=0.5)

        # Create dynamic bars
        def draw_bar(k):
            y_value = binom.pmf(k, 100, p=alt_spinner.probability.get_value()).item()
            height = abs(pmf_plot.axes.c2p(0, y_value)[1] - pmf_plot.axes.c2p(0, 0)[1])
            bar = Rectangle(
                width=pmf_plot.bar_width,
                height=height,
                color=pmf_plot.color1,
                fill_opacity=0.7,
                stroke_width=1
            ).move_to(pmf_plot.axes.c2p(k+1, y_value/2)).align_to(pmf_plot.axes.c2p(k+1, 0), DOWN)

            return bar
        
        bars = list()
        for k in list(x_values):
            bar = always_redraw( lambda k=k: draw_bar(k))
            bars.append(bar)

        #################################################################
        # Animation (1)                                                 #
        #################################################################
        # Testing
        # self.add(NumberPlane(), Dot(ORIGIN))
        # self.add(alt_world, alt_spinner, steve_devil, alt_hypothesis_txt, 
        #          brace, mu_equation)
        
        self.play(
            FadeIn(steve_devil, alt_world, alt_hypothesis_txt, shift=DOWN*0.1),
            FadeIn(brace,shift=DOWN*0.1)
        )

        self.wait()

        self.play(
            Write(mu_equation),
            FadeIn(alt_spinner, shift=DOWN*0.1),
            FadeIn(pmf_plot.axes, pmf_plot.x_label, pmf_plot.x_num_labels, pmf_plot.y_label, *bars, shift=DOWN*0.1)
        )

        self.wait()

        self.play(
            alt_spinner.probability.animate.set_value(0.85),
            run_time = 3
        )

        self.play(
            alt_spinner.probability.animate.set_value(0.51),
            run_time = 3
        )

        self.wait()

        self.play(
            FadeOut(*self.mobjects, shift=DOWN*0.1)
        )

        self.wait()

