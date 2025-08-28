from manim import *
from probability_mobjects import *
from dudek_utils import *

class CalcPval(Scene):
    def construct(self):
        null_world = GenericImageMobject("assets/null_world.png").scale(0.5).align_on_border(UP)

        steve_angel = GenericImageMobject("assets/steve_angel.png").scale(0.4).next_to(null_world, LEFT, buff=1)

        null_hypothesis_txt = Tex(r"null hypothesis").next_to(null_world, RIGHT, buff=1)

        brace = BraceBetweenPoints((-4,1,0), (4,1,0), direction=UP, sharpness=1).scale(1.5)

        null_spinner = Spinner(0.5).scale(1.6).next_to(null_hypothesis_txt, DOWN, buff=2.2)
        null_spinner.add_image(GenericImageMobject("assets/rod.png").scale(1.7))

        blaze = GenericImageMobject("assets/blaze.png").scale_to_fit_height(1.5).move_to((5.5,0,0))

        mu_equation = MathTex(r"\mu = 0.5").arrange(RIGHT, buff=0.1).next_to(null_spinner, UP, buff=0.1)

        pmf_plot = PMFBarPlot.binom(
            n=100, p=0.5, width=6.5, height=2.7, 
            gap=0.05, alpha=1e-8, min_prob=0,
            x_label=Tex("$x$ (number of blaze rods)", font_size = 40)
        ).next_to(null_spinner, LEFT, buff=0.5).shift(DOWN*0.3)

        n_txt = Tex("$n = $ number of blazes killed = 100", font_size = 36).move_to((-2,0.8,0))

        rod = GenericImageMobject("assets/rod.png")
        red_x = GenericImageMobject("assets/red_x.png")

        data_graphic = BinomDataGraphic(67, 100, rod, red_x, width=3, nrow=10).next_to(null_hypothesis_txt, DOWN, buff=2.2).shift(RIGHT*0.7)
        data_txt = Text("Data (67/100)", color=WHITE, font_size=36).next_to(data_graphic, UP)
        data_txt[:4].set_color(ORANGE)
        data_txt[5:7].set_color(ORANGE)

        x_values = np.arange(66, 77)
        y_values = binom.pmf(x_values, n=100, p=0.5)
        pmf_plot_zoomed = PMFBarPlot(
            x_values, y_values,
            width=6.5, height=2.7, gap=0.05, x_prime=67,
            x_label=Tex("$x$ (number of blaze rods)", font_size = 40)
        ).next_to(null_spinner, LEFT, buff=0.5).shift(DOWN*0.3)

        pmf_plot_zoomed.add(pmf_plot_zoomed.x_prime_label)
        pmf_plot_zoomed.x_prime_line.set_z_index(1)
        pmf_plot_zoomed.x_prime_label.set_z_index(1)

        x = pmf_plot.axes.c2p((77.5+66.5)/2, 0)[0]
        y0 = pmf_plot.axes.c2p(0, 0)[1]
        y1 = pmf_plot.axes.c2p(0, 0.01)[1]
        y = (y0+y1)/2
        small_rectangle = Rectangle(
            width = (77.5-66.5)*pmf_plot.axes.get_x_unit_size(),
            height=y1-y0
        ).move_to((x,y,0))

        
        x0 = pmf_plot_zoomed.axes.c2p(min(pmf_plot_zoomed.x_values)+0.5, 0)[0]
        x1 = pmf_plot_zoomed.axes.c2p(max(pmf_plot_zoomed.x_values)+1.5, 0)[0]
        x = (x0+x1)/2
        y0 = pmf_plot.axes.c2p(0, 0)[1]
        y1 = pmf_plot.axes.c2p(0, max(pmf_plot.y_values)*1.1)[1] + 0.1
        y = (y0+y1)/2
        large_rectangle = Rectangle(
            width = x1-x0,
            height=y1-y0
        ).move_to((x,y,0))

        prob_eq = MathTex(
            r"""
            p &= P(X \geq 67) = \sum_{k=67}^{100} P(X=k) \\
             &\approx 0.0004 = \frac{1}{2500}
            """,
            color = BLUE, font_size = 36,
        ).move_to((-0.5,-0.8,0))

        blue_brace = BraceBetweenPoints(
            pmf_plot_zoomed.x2bar(67).get_corner(UR),
            pmf_plot_zoomed.x2bar(76).get_corner(UR),
            direction=UP, sharpness=1, color = BLUE
        )
        
        blue_brace.rotate(-13*DEGREES, about_point=blue_brace.get_edge_center(LEFT)).shift(DOWN*0.1)

        eq_rectangle = SurroundingRectangle(prob_eq[0][25:])

        #################################################################
        # Animation (1)                                                 #
        #################################################################
        # Testing
        # self.add(NumberPlane(), Dot(ORIGIN))
        # self.add(null_spinner, blaze, mu_equation)
        # self.add(data_graphic, data_txt)
        # self.add(null_world, steve_angel, null_hypothesis_txt,
        #          brace, n_txt)
        # self.add(small_rectangle, pmf_plot.bars,
        #          pmf_plot.axes, pmf_plot.x_label, pmf_plot.x_num_labels, pmf_plot.y_label)
        # self.add(pmf_plot_zoomed, prob_eq, blue_brace, eq_rectangle)

        self.play(
            FadeIn(steve_angel, null_world, null_hypothesis_txt, brace, shift=DOWN*0.1),
        )

        self.wait()

        self.play(
            Write(n_txt)
        )

        self.play(
            Circumscribe(n_txt[0][-3:], time_width=0.5)
        )

        self.wait()

        self.add(*pmf_plot.bars)
        self.play(
            FadeIn(null_spinner, blaze, shift=DOWN*0.1),
            Write(mu_equation),
            Create(pmf_plot.axes),
            Create(pmf_plot.x_label), 
            Create(pmf_plot.x_num_labels), 
            Create(pmf_plot.y_label),
            pmf_plot.create_bars(lag_ratio = 0.01),
        )

        self.wait()

        self.play(
            FadeOut(null_spinner, mu_equation, blaze, shift=DOWN*0.1)
        )

        self.play(
            FadeIn(data_graphic, data_txt, shift=DOWN*0.1)
        )

        self.wait()

        # Restore colors
        self.play(
            AnimationGroup([
                pmf_plot.bars[i].animate.set_color(pmf_plot.color1 if pmf_plot.i2x(i) >= 56 else pmf_plot.color2)
                for i in range(len(pmf_plot.bars))
            ])
        )

        pmf_plot.x_prime.set_value(56)
        pmf_plot.resume_updating()

        self.play(
            Create(pmf_plot.x_prime_line.reverse_points()),
        )
        self.play(
            FadeIn(pmf_plot.x_prime_label, shift=UP*0.1),
            run_time=0.1
        )

        self.wait()

        self.play(
            pmf_plot.x_prime.animate.set_value(67)
        )

        self.wait()

        self.play(
            Create(small_rectangle)
        )

        self.wait()

        self.play(
            ReplacementTransform(pmf_plot.axes, pmf_plot_zoomed.axes),
            ReplacementTransform(pmf_plot.x_label, pmf_plot_zoomed.x_label),
            ReplacementTransform(pmf_plot.x_num_labels, pmf_plot_zoomed.x_num_labels),
            ReplacementTransform(pmf_plot.bars, pmf_plot_zoomed.bars),
            ReplacementTransform(pmf_plot.x_prime_line, pmf_plot_zoomed.x_prime_line),
            ReplacementTransform(pmf_plot.x_prime_label, pmf_plot_zoomed.x_prime_label),
            ReplacementTransform(small_rectangle, large_rectangle)
        )

        self.play(
            Uncreate(large_rectangle)
        )

        self.wait()

        self.play(
            Create(blue_brace)
        )

        self.wait()

        self.play(
            Uncreate(blue_brace),
            Write(prob_eq)
        )

        self.play(
            Create(eq_rectangle)
        )

        self.wait()

        self.play(
            FadeOut(*self.mobjects, shift=DOWN*0.1)
        )

        self.wait()
