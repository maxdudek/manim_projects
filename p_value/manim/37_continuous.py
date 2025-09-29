from manim import *
from probability_mobjects import *
from dudek_utils import *
from scipy.stats import t, chi2
footnote = __import__('34_footnote_two_sided')

class _37_continuous(Scene):
    def construct(self):

        footnote_sector, footnote_angle, footnote_border, footnote_txt = footnote.get_footnote(2, redraw=False)

        H_GREEN="#4ea72e"
        H_PINK="#d86ecc"
        z_eq = MathTex(r"z = \frac{\bar{x}-\bar{y}}{\frac{\sigma_x}{\sqrt{n}} + \frac{\sigma_y}{\sqrt{m}}}").move_to((-4,-1,0))
        z_eq[0][0].set_color(ORANGE)
        z_eq[0][2:4].set_color(H_GREEN)
        z_eq[0][8:10].set_color(H_GREEN)
        z_eq[0][13].set_color(H_GREEN)
        z_eq[0][5:7].set_color(H_PINK)
        z_eq[0][15:17].set_color(H_PINK)
        z_eq[0][20].set_color(H_PINK)
        two_sample_txt = Text('(ex. two-sample z-test):', font_size=28).next_to(z_eq, UP, buff=0.5)

        sigma_txt = MathTex(r"(\sigma)").next_to(z_eq[0][0], DOWN)
        sigma_txt[0][1].set_color(ORANGE)

        # Normal distribution
        normal_grid, normal_density, z_score, normal_area, z_line, z_label = pdf_plot(
            dnorm, xmin=-3.5, xmax=3.5, ymax=0.45, x_length=7, y_length=3.5
        )

        ########################## t and chi-sq distributions
        def dt(x):
            return t.pdf(x, df=3).item()
        
        def dchisq(x):
            return chi2.pdf(x, df=10).item()
        
        t_grid, t_density, t_score, t_area, t_line, t_label = pdf_plot(
            dt, xmin=-3.5, xmax=3.5, ymax=0.45, x_length=6, y_length=3, 
            where=(-3.5,-1,0), label="t"
        )

        chi_grid, chi_density, chi_score, chi_area, chi_line, chi_label = pdf_plot(
            dchisq, xmin=0, xmax=30, ymax=0.11, x_length=6, y_length=3, stat_start=18,
            where=(3.5,-1,0), label=r"\chi^2", x_inc=5, y_inc=0.05,
        )
        chi_label.shift(RIGHT*0.1)

        t_txt = Tex(r"$t$-statistic \\($t$)").next_to(t_grid, UP, buff=1)
        chisq_txt = Tex(r"$\chi^2$ value\\(chi-squared)").next_to(chi_grid, UP, buff=1)

        ########################## discrete vs. continuous
        pmf_plot = PMFBarPlot.binom(
            n=100, p=0.5, width=6, height=2.9, 
            gap=0.03, alpha=1e-7, min_prob=0, x_prime = 59, x_prime_height_scale = 1.1,
            x_label=Tex("$x$", font_size = 40), x_labels_font_size = 0,
            x_label_offset=UP*0.5, y_nums=False, show_y_label=False,
        ).align_on_border(LEFT, buff=0.7).shift(DOWN*1.3)

        pmf_plot.x_prime_line.set_z_index(1)
        pmf_plot.resume_updating()
        pmf_plot.x_prime_line.resume_updating()

        x_prime_label = Text("x' (whole number)", font_size=32, color=ORANGE).next_to(pmf_plot.x_prime_line, UP)
        x_prime_label.add_updater(lambda v: v.next_to(pmf_plot.x_prime_line, UP))

        normal_grid2, normal_density2, z_score2, normal_area2, z_line2, z_label2 = pdf_plot(
            dnorm, xmin=-3.5, xmax=3.5, ymax=0.45, x_length=6, y_length=2.9, where=(3.5,-1.35,0), stat_start=0.9
        )

        discrete_txt = Text("Discrete", slant=ITALIC).next_to(pmf_plot, UP, buff=1)
        continuous_txt = Text("Continuous", slant=ITALIC).next_to(normal_grid2, UP, buff=1)

        p_eq = MathTex(r"p &= P(X \geq z)\\ &= \int_z^\infty f(x) dx", color=BLUE, font_size = 32).move_to((5.6,-1,0))
        p_arrow = Arrow(
            p_eq.get_edge_center(DOWN),
            (4.5,-2.6,0),
            stroke_width=6
        )

        average_eq = MathTex(r"\bar{x} = \frac{1}{n}\sum_{i=1}^n x_i").set_y(-0.7)

        #################################################################
        # Animation (1)                                                 #
        #################################################################
        # self.add(NumberPlane(
        #     background_line_style={
        #         "stroke_width": 2,
        #         "stroke_opacity": 0.6
        #     }).set_z_index(-1))
        # self.add(z_eq, two_sample_txt, normal_grid, 
        #          normal_area, normal_density, z_line, z_label)
        # self.add(t_grid, t_area, t_density, t_line, t_label,
        #          chi_grid, chi_area, chi_density, chi_line, chi_label, t_txt, chisq_txt)
        # self.add(pmf_plot, pmf_plot.x_prime_line, x_prime_label,
        #          normal_grid2, normal_area2, normal_density2, z_line2, z_label2,
        #          discrete_txt, continuous_txt, p_eq, p_arrow)
        # self.add(average_eq)

        self.add(footnote_sector, footnote_txt, footnote_border)

        self.play(
            Write(z_eq),
            run_time=1
        )

        self.play(
            FadeIn(two_sample_txt)
        )

        self.play(
            FadeIn(sigma_txt, shift=DOWN*0.5)
        )

        self.wait()

        self.play(
            FadeIn(normal_grid, normal_area, normal_density, z_line, z_label)
        )

        self.play(
            z_score.animate.set_value(-2)
        )

        self.play(
            z_score.animate.set_value(2)
        )

        self.wait(0.1)

        self.play(
            FadeOut(*[m for m in self.mobjects if m not in [footnote_sector, footnote_border, footnote_txt]]),
            FadeIn(t_txt)
        )

        self.wait(0.5)

        self.play(
            FadeIn(t_grid, t_area, t_density, t_line, t_label)
        )

        self.wait(0.5)

        self.play(
            FadeIn(chisq_txt)
        )

        self.wait(0.5)

        self.play(
            FadeIn(chi_grid, chi_area, chi_density, chi_line, chi_label)
        )

        self.wait()

        self.play(
            AnimationGroup(
                FadeOut(*[m for m in self.mobjects if m not in [footnote_sector, footnote_border, footnote_txt]]),
                FadeIn(pmf_plot, pmf_plot.x_prime_line, x_prime_label,),
                lag_ratio=0.5
            )
        )

        self.wait()

        self.play(
            Write(discrete_txt),
            run_time=0.8
        )

        self.wait()

        pmf_plot.freeze_bars()
        for x in range(40,61):
            for i in range(len(pmf_plot.bars)):
                pmf_plot.bars[i].set_color(pmf_plot.color1 if pmf_plot.i2x(i) == x else pmf_plot.color2)
            self.wait(0.15)

        self.wait()

        self.play(
            FadeIn(average_eq)
        )

        self.wait()

        self.play(
            FadeOut(average_eq)
        )

        self.play(
            Write(continuous_txt),
            run_time=0.8
        )

        self.wait()

        self.play(
            FadeIn(normal_grid2, normal_area2, normal_density2, z_line2, z_label2,)
        )

        self.wait()

        self.play(
            z_score2.animate.set_value(-0.3)
        )

        self.play(
            z_score2.animate.set_value(0.8)
        )

        self.play(
            GrowArrow(p_arrow)
        )

        self.wait()

        self.play(
            Write(p_eq),
            run_time=1
        )

        self.wait()

        self.play(
            FadeOut(*self.mobjects, shift=DOWN*0.2)
        )

        self.wait(0.1)






