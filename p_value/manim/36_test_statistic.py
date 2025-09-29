from manim import *
from probability_mobjects import *
from dudek_utils import *
footnote = __import__('34_footnote_two_sided')

class _36_test_statistic(Scene):
    def construct(self):

        footnote_sector, footnote_angle, footnote_border, footnote_txt = footnote.get_footnote(2)

        #################### rods
        png67 = GenericImageMobject("assets/rod_67.png").scale_to_fit_width(3-0.3).move_to((0,-1,0))
        data_graphic = Group(png67, SurroundingRectangle(png67, color = WHITE, buff=0.2))
        data_txt = Text("Data (67/100)", color=WHITE, font_size=36).next_to(data_graphic, UP)
        data_txt[:4].set_color(ORANGE)
        data_txt[5:7].set_color(ORANGE)

        how_extreme_txt = Text("how extreme", font_size=40).set_y(2.5).set_x(data_txt[5:7].get_x())
        how_extreme_arrow = Arrow(
            how_extreme_txt.get_edge_center(DOWN),
            data_txt[5:7].get_edge_center(UP),
            stroke_width=8,
            buff=0.15
        )

        #################### heights
        heights_png = GenericImageMobject("assets/heights.png").scale(0.6).move_to((-3.5,-1,0))
        heights_graphic = Group(heights_png, SurroundingRectangle(heights_png, color = WHITE, buff=0.2))
        heights_txt = Text("Data (heights)", color=ORANGE, font_size=36).next_to(heights_graphic, UP)

        H_GREEN="#4ea72e"
        H_PINK="#d86ecc"
        x_data = MathTex(r"x_1, x_2, \cdots, x_n,", color=H_GREEN).move_to((1,1.6,0))
        y_data = MathTex(r"y_1, y_2, \cdots, y_m,", color=H_PINK).next_to(x_data, RIGHT)

        averages = MathTex(r"\bar{x} - \bar{y}").scale(1.1).next_to(Group(x_data, y_data), DOWN, buff=0.5)
        averages[0][:2].set_color(H_GREEN)
        averages[0][-2:].set_color(H_PINK)

        data_brace = Brace(heights_graphic, RIGHT, sharpness=1, stroke_width=1)

        how_unexpected_txt = Text("How extreme/unexpected?", font_size=42, slant=ITALIC).next_to(data_brace, RIGHT, buff=0.3)

        test_statistic_txt = Text('"Test statistic"', font_size=42, color=ORANGE).next_to(how_unexpected_txt, DOWN, buff=1.4)
        test_statistic_arrow = Arrow(
            how_unexpected_txt.get_edge_center(DOWN),
            test_statistic_txt.get_edge_center(UP),
            stroke_width=8,
            buff=0.1
        )

        #################### x_prime
        data_txt2 = Text("Data (x'/n)", font_size=50).move_to((-4.5,-2,0))
        data_txt2[:4].set_color(ORANGE)
        data_txt2[5:7].set_color(ORANGE)

        test_statistic_txt2 = Text('"Test statistic"', font_size=42, color=ORANGE).next_to(data_txt2[5:7], UP, buff=1.4)
        test_statistic_arrow2 = Arrow(
            test_statistic_txt2.get_edge_center(DOWN),
            data_txt2[5:7].get_edge_center(UP),
            stroke_width=8,
            buff=0.15
        )

        pmf_plot = PMFBarPlot.binom(
            n=100, p=0.5, width=7, height=3.2, 
            gap=0.03, alpha=1e-7, min_prob=0, x_prime = 59, x_prime_height_scale = 1.1,
            x_label=Tex("$x$", font_size = 40), x_labels_font_size = 0,
            x_label_offset=UP*0.5,
        ).align_on_border(DR).shift(DOWN*0.2)

        pmf_plot.x_prime_line.set_z_index(1)
        pmf_plot.resume_updating()
        pmf_plot.x_prime_line.resume_updating()

        x_prime_label = Text("x'", font_size=32, color=ORANGE).next_to(pmf_plot.x_prime_line, UP)
        x_prime_label.add_updater(lambda v: v.next_to(pmf_plot.x_prime_line, UP))

        brace_null = BraceBetweenPoints((1,0.8,0), (5.2,0.8,0), direction=UP, sharpness=0.7).scale(1.6)
        null_world = GenericImageMobject("assets/null_world.png").scale(0.5).next_to(brace_null, UP)

        binomial_txt = Text("binomial\ndistribution", font_size=30).move_to((1.1,-0.5,0))
        

        #################################################################
        # Animation (1)                                                 #
        #################################################################
        # self.add(NumberPlane(
        #     background_line_style={
        #         "stroke_width": 2,
        #         "stroke_opacity": 0.6
        #     }).set_z_index(-1))
        # self.add(footnote_sector, footnote_border, footnote_txt)
        # self.add(data_graphic, data_txt, how_extreme_arrow, how_extreme_txt)
        # self.add(heights_graphic, heights_txt, x_data, y_data, data_brace, 
        #          how_unexpected_txt, test_statistic_arrow, test_statistic_txt, averages)
        # self.add(data_txt2, pmf_plot, pmf_plot.x_prime_line, x_prime_label, test_statistic_txt2, test_statistic_arrow2,
        #          brace_null, null_world, binomial_txt)
        

        self.add(footnote_sector)
        self.play(
            footnote_angle.animate.set_value(TAU),
            Create(footnote_border),
            run_time=0.5
        )
        self.play(
            Write(footnote_txt),
            FadeIn(data_graphic, data_txt),
            run_time=0.6
        )

        self.wait()

        self.play(
            Write(how_extreme_txt),
            GrowArrow(how_extreme_arrow),
            run_time=0.8
        )

        self.wait()

        self.play(
            AnimationGroup(
                FadeOut(data_graphic, data_txt, how_extreme_arrow, how_extreme_txt),
                FadeIn(heights_graphic, heights_txt),
                FadeIn(x_data),
                FadeIn(y_data),
                lag_ratio=0.7
            ),
            run_time=2
        )

        self.wait()

        self.play(
            Create(data_brace),
            Write(how_unexpected_txt),
            run_time=0.8
        )

        self.wait()

        self.play(
            Write(test_statistic_txt),
            GrowArrow(test_statistic_arrow),
            run_time=0.8
        )

        self.wait()

        self.play(
            Transform(x_data.copy(), averages[0][:2]),
            Transform(y_data.copy(), averages[0][-2:]),
            FadeIn(averages[0][2])
        )

        self.wait()

        self.play(
            FadeOut(*[m for m in self.mobjects if m not in [footnote_sector, footnote_border, footnote_txt]]),
            FadeIn(data_txt2)
        )

        self.wait()

        self.play(
            Write(test_statistic_txt2),
            GrowArrow(test_statistic_arrow2),
            run_time=0.8
        )

        self.wait()

        self.play(
            FadeIn(null_world, brace_null)
        )

        self.play(
            FadeIn(pmf_plot, pmf_plot.x_prime_line, x_prime_label)
        )

        self.play(
            Write(binomial_txt),
            run_time=0.8
        )

        self.wait()

        self.play(
            FadeOut(*[m for m in self.mobjects if m not in [footnote_sector, footnote_border, footnote_txt]])
        )

        self.wait(0.1)






