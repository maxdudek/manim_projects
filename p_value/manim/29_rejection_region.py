from manim import *
from probability_mobjects import *
from dudek_utils import *

class _29_rejection_region(Scene):
    def construct(self):

        pmf_plot = PMFBarPlot.binom(
            n=1000, p=0.5, width=5.5, height=3, 
            gap=0.01, alpha=5e-7, min_prob=0,
            x_label=Tex("$x$", font_size = 40), x_labels_font_size = 0,
            x_label_offset=UP*0.5, coloring_mode = "rejection_region", x_prime=490,
            color2 = BLUE
        ).align_on_border(DL).shift(DOWN*0.2)
        pmf_plot.x_prime_line.resume_updating()
        
        pmf_plot_alt = PMFBarPlot.binom(
            n=1000, p=0.6, width=5.5, height=3, 
            gap=0.01, alpha=1e-9, min_prob=0,
            x_label=Tex("$x$", font_size = 40), x_labels_font_size = 0,
            x_label_offset=UP*0.5, show_y_label = False
        ).align_on_border(DR).shift(DOWN*0.2)
        pmf_plot_alt.x_prime_line.resume_updating()

        null_world = GenericImageMobject("assets/null_world.png").scale(0.5).move_to((pmf_plot.axes.c2p(500,0)[0], 2.5, 0))
        alt_world = GenericImageMobject("assets/alt_world.png").scale(0.5).move_to((pmf_plot_alt.axes.c2p(600,0)[0], 2.5, 0))

        null_brace = BraceBetweenPoints(
            null_world.get_center() + LEFT*2.5,
            null_world.get_center() + RIGHT*2.5,
            UP, sharpness=0.7, stroke_width=2
        ).set_y(1)

        alt_brace = BraceBetweenPoints(
            alt_world.get_center() + LEFT*2.5,
            alt_world.get_center() + RIGHT*2.5,
            UP, sharpness=0.7, stroke_width=2
        ).set_y(1)
        
        mu_eq_null = MathTex(r"\mu = 0.50").next_to(null_brace, DOWN, buff=0.3)

        mu_variable = Variable(0.6, MathTex("\mu", color=YELLOW))
        mu_variable.set_color(YELLOW)
        mu_variable.label[0][0].shift(DOWN*0.05)
        mu_eq_alt = VGroup(
            mu_variable, Tex("?")
        ).arrange(RIGHT, buff=0.1).next_to(alt_brace, DOWN, buff=0.3)

        def draw_bar(k):
            y_value = binom.pmf(k, 1000, p=mu_variable.tracker.get_value()).item()
            height = abs(pmf_plot_alt.axes.c2p(0, y_value)[1] - pmf_plot_alt.axes.c2p(0, 0)[1])
            bar = Rectangle(
                width=pmf_plot_alt.bar_width,
                height=height,
                color=pmf_plot_alt.color1,
                fill_opacity=0.7,
                stroke_width=1
            ).move_to(pmf_plot_alt.axes.c2p(k+1, y_value/2)).align_to(pmf_plot_alt.axes.c2p(k+1, 0), DOWN)

            return bar
        
        bars = VGroup()
        for k in list(pmf_plot_alt.x_values):
            bar = always_redraw( lambda k=k: draw_bar(k))
            bars.add(bar)

        x_prime_label = Text("x'", font_size=32, color=ORANGE).next_to(pmf_plot.x_prime_line, UP, buff=0.1)
        x_prime_label.add_updater(lambda v: v.next_to(pmf_plot.x_prime_line, UP, buff=0.1))
        pmf_plot.x_prime_line.set_z_index(1)

        r_txt = MathTex("R", color=PROB_PINK, font_size=70).move_to((-4,-1,0))

        def x_prime_in_rejection_region(x_prime, start, size):
            x_prime = int(round(x_prime))
            start = int(round(start))
            if x_prime < start: return False

            y_vals = [binom_pmf(x,1000,0.5) for x in range(start, x_prime+1)]

            print(sum(y_vals))

            return sum(y_vals) < size
        
        reject_h0_txt = MarkupText("Reject H<sub>0</sub>!", font_size=40, color=PROB_PINK).next_to(null_world, LEFT, buff=1)
        reject_h0_txt.add_updater(lambda v: v.set_opacity(x_prime_in_rejection_region(pmf_plot.x_prime.get_value(), 
                                                                                      pmf_plot.rejection_region_start.get_value(),
                                                                                      pmf_plot.rejection_region_size.get_value())))

        how_big_txt = Text("1. How big should R be?", font_size=42).move_to((3.6,3,0))
        how_big_txt[-4].set_color(PROB_PINK)
        how_big_rect = SurroundingRectangle(how_big_txt)

        null_eq = VGroup()
        null_eq.add( # 0
            MarkupText("Given H<sub>0</sub>:", font_size=36).next_to(how_big_txt, DOWN).align_to(how_big_txt, LEFT)
        )

        null_eq.add( # 1
            Text("Size of R", font_size=36, color=PROB_PINK).next_to(null_eq[-1], DOWN).align_to(null_eq[-1], LEFT)
        )

        null_eq.add( # 2
            Text("= P(x' in R)", font_size=36, color=PROB_PINK).next_to(null_eq[-1], RIGHT, buff=0.15).align_to(null_eq[-1], UP)
        )
        null_eq[-1][3:5].set_color(ORANGE)

        null_eq.add( # 3
            MarkupText("= P(reject H<sub>0</sub>)", font_size=36, color=PROB_PINK).next_to(null_eq[-1], DOWN).align_to(null_eq[-1], LEFT)
        )

        null_eq.add( # 4
            Text("= P(FP)", font_size=36, color=PROB_PINK).next_to(null_eq[-1], DOWN).align_to(null_eq[-1], LEFT)
        )
        null_eq[-1][3:5].set_color(RED)

        null_eq.add( # 5
            Text("= Type I error rate", font_size=36, color=PROB_PINK).next_to(null_eq[-1], DOWN).align_to(null_eq[-1], LEFT)
        )

        null_eq.add( # 6
            Text("smaller R", font_size=28).next_to(null_eq[-1], DOWN, buff=0.6).align_to(null_eq[1], LEFT).shift(LEFT*0.5)
        )
        null_eq[-1][-1].set_color(PROB_PINK)

        null_eq.add( # 7
            Text("higher Type II error rate", font_size=28).next_to(null_eq[-1], RIGHT, buff=1)
        )

        null_eq.add( # 8
            DoubleArrow(null_eq[-1].get_edge_center(LEFT), null_eq[-2].get_edge_center(RIGHT), buff=0.1)
        )

        null_eq[-1] = separate_double_arrow(null_eq[-1])

        null_eq.add( # 9
            Text("= α", font_size=36, color=PROB_PINK).next_to(null_eq[2], DOWN).align_to(null_eq[2], LEFT).shift(DOWN*0.1)
        )

        null_eq.add( # 10
            Text("sig. threshold", font_size=24).next_to(null_eq[-1], RIGHT, buff=0.7)
        )

        null_eq.add( # 11
            Arrow(null_eq[-1].get_edge_center(LEFT), null_eq[-2].get_edge_center(RIGHT), buff=0.1)
        )

        null_eq.add( #12
            Text("lower Type I error rate", font_size=28).align_to(null_eq[7], UP).align_to(null_eq[7], LEFT)
        )

        where_txt = Text("2. Where should R be?", font_size=42).align_to(how_big_txt, LEFT).set_y(0)
        where_txt[-4].set_color(PROB_PINK)
        

        alt_eq = VGroup()
        alt_eq.add( # 0
            MarkupText('Given <span foreground="yellow">H<sub>1</sub></span>:', font_size=36).next_to(where_txt, DOWN).align_to(where_txt, LEFT)
        )

        where_txt.set_y(-2.3) # Original position

        PALE_YELLOW="#FFEC82"

        alt_eq.add( # 1
            Text("Maximize P(x' in R)", font_size=36, color=PALE_YELLOW).next_to(alt_eq[-1], DOWN).align_to(alt_eq[-1], LEFT)
        )
        alt_eq[-1][10:12].set_color(ORANGE)
        alt_eq[-1][-2].set_color(PROB_PINK)

        pink_arrow = Arrow(
            alt_eq[-1].get_edge_center(LEFT) + LEFT*2,
            alt_eq[-1].get_edge_center(LEFT),
            color=PROB_PINK
        )
        pink_arrow.set_z_index(2)

        alt_eq.add( # 2
            Text("Minimize P(x' not in R)", font_size=36, color=PALE_YELLOW).next_to(alt_eq[-2], DOWN).align_to(alt_eq[-2], LEFT)
        )
        alt_eq[-1][10:12].set_color(ORANGE)
        alt_eq[-1][-2].set_color(PROB_PINK)

        alt_eq.add( # 3
            MarkupText("= P(fail to reject H<sub>0</sub>)", font_size=36, color=PALE_YELLOW).next_to(alt_eq[-1], DOWN).align_to(alt_eq[-1], LEFT).shift(RIGHT*1)
        )

        alt_eq.add( # 4
            Text("= P(FN)", font_size=36, color=PALE_YELLOW).next_to(alt_eq[-1], DOWN).align_to(alt_eq[-1], LEFT)
        )
        alt_eq[-1][3:5].set_color(RED)

        alt_eq.add( # 5
            Text("= Type II error rate", font_size=36, color=PALE_YELLOW).next_to(alt_eq[-1], DOWN).align_to(alt_eq[-1], LEFT)
        )

        mu_eq_alt2 = MathTex(r"\mu > 0.5", color=YELLOW).set_y(r_txt.get_y()).set_x(pmf_plot.axes.c2p(545,0)[0])

        correspondence_eq = MathTex(r"\text{x' in } R \longleftrightarrow p \leq \alpha").move_to(alt_eq[-1]).shift(UP*0.5)
        correspondence_eq[0][:2].set_color(ORANGE)
        correspondence_eq[0][4].set_color(PROB_PINK)
        correspondence_eq[0][7].set_color(BLUE_TXT)
        correspondence_eq[0][-1].set_color(PROB_PINK)

        #################################################################
        # Animation (1)                                                 #
        #################################################################
        # self.add(NumberPlane(
        #     background_line_style={
        #         "stroke_width": 2,
        #         "stroke_opacity": 0.6
        #     }).set_z_index(-2))
        
        # self.add(pmf_plot, null_brace, null_world, mu_eq_null )
        # self.add(alt_brace, alt_world, mu_eq_alt, pmf_plot_alt.axes, pmf_plot_alt.x_label, pmf_plot_alt.x_num_labels, *bars,)
        
        # self.add(pmf_plot.x_prime_line, x_prime_label, reject_h0_txt, where_txt)
        # self.add( how_big_txt, null_eq, how_big_rect)
        # self.add(where_txt, alt_eq)
        # self.add(correspondence_eq)

        self.play(
            FadeIn(null_world)
        )

        self.play(
            FadeIn(alt_world)
        )

        self.wait()

        self.play(
            FadeIn(null_brace, pmf_plot, mu_eq_null)
        )

        self.play(
            FadeIn(alt_brace, mu_eq_alt, pmf_plot_alt.axes, pmf_plot_alt.x_label, pmf_plot_alt.x_num_labels, bars),
        )

        self.play(
            mu_variable.tracker.animate.set_value(0.65),
            run_time = 1.5
        )

        self.play(
            mu_variable.tracker.animate.set_value(0.55),
            run_time = 1.5
        )

        self.wait()

        self.play(
            FadeOut(alt_world, alt_brace, mu_eq_alt, pmf_plot_alt.axes, pmf_plot_alt.x_label, pmf_plot_alt.x_num_labels, *bars,)
        )

        self.wait()

        self.play(
            Create(pmf_plot.x_prime_line),
            FadeIn(x_prime_label)
        )

        self.wait()

        # Restore colors
        self.play(
            AnimationGroup([
                pmf_plot.bars[i].animate.set_color(PROB_PINK if pmf_plot.i2x(i) in [500, 501, 502] else DARK_BLUE)
                for i in range(len(pmf_plot.bars))
            ]),
            Write(r_txt)
        )

        pmf_plot.color2 = DARK_BLUE
        pmf_plot.rejection_region_start.set_value(500)
        pmf_plot.rejection_region_size.set_value(0.1)
        pmf_plot.resume_updating()
        reject_h0_txt.resume_updating()
        self.add(reject_h0_txt)

        self.wait()

        self.play(
            pmf_plot.x_prime.animate.set_value(505),
            run_time=3
        )

        self.play(
            pmf_plot.x_prime.animate.set_value(497),
            run_time=2
        )

        self.wait()

        self.play(
            Write(how_big_txt),
            pmf_plot.rejection_region_size.animate.set_value(0.6),
            pmf_plot.rejection_region_start.animate.set_value(493),
            run_time=1
        )

        self.play(
            pmf_plot.rejection_region_size.animate.set_value(0.1),
            pmf_plot.rejection_region_start.animate.set_value(500),
        )

        self.wait()

        self.play(
            Write(where_txt),
            pmf_plot.rejection_region_start.animate.set_value(470),
            run_time=1
        )

        self.play(
            pmf_plot.rejection_region_start.animate.set_value(520),
        )

        self.play(
            pmf_plot.rejection_region_start.animate.set_value(500),
        )

        self.wait()

        self.play(
            Create(how_big_rect)
        )

        self.play(
            Write(null_eq[0]),
            run_time=0.7
        )

        self.play(
            Write(null_eq[2][1:]),
            run_time=0.7
        )

        self.wait()

        self.play(
            Write(VGroup(null_eq[1], null_eq[2][0])),
            run_time=0.7
        )

        self.wait()

        self.play(
            Write(null_eq[3:5]),
            run_time=1.2
        )

        self.wait()

        self.play(
            Write(null_eq[5]),
            run_time=0.8
        )

        self.wait()

        self.play(
            Succession(
                Write(null_eq[6]),
                GrowDoubleArrow(null_eq[8]),
                Write(null_eq[12])
            ),
            run_time=2
        )

        self.wait()

        self.play(
            FadeOut(null_eq[12]),
            FadeIn(null_eq[7])
        )

        self.wait()

        self.play(
            FadeOut(null_eq[2:5], null_eq[6:9]),
            null_eq[5].animate.align_to(null_eq[1], UP),
            where_txt.animate.set_y(0),
            Uncreate(how_big_rect)
        )

        self.wait()

        where_rect = SurroundingRectangle(where_txt)

        self.play(Create(where_rect))

        self.wait()

        self.play(
            FadeIn(mu_eq_alt2)
        )

        self.wait()

        self.play(
            Write(alt_eq[0])
        )

        self.play(
            pmf_plot.x_prime.animate.set_value(560),
            FadeOut(mu_eq_alt2)
        )

        self.play(
            pmf_plot.x_prime.animate.set_value(526)
        )

        self.play(
            pmf_plot.x_prime.animate.set_value(540)
        )

        self.wait()

        self.play(
            pmf_plot.rejection_region_size.animate.set_value(0.06),
            pmf_plot.rejection_region_start.animate.set_value(527),
            GrowArrow(pink_arrow),
            run_time=1.8
        )

        self.play(
            Write(alt_eq[1]),
            run_time=0.9
        )

        self.wait()

        self.play(
            FadeOut(alt_eq[1]),
            FadeIn(alt_eq[2])
        )

        self.wait()

        self.play(
            Write(alt_eq[3:5]),
            run_time=1.2
        )

        self.wait()

        self.play(
            Write(alt_eq[5]),
            run_time=0.8
        )

        self.wait()

        self.play(
            FadeOut(alt_eq[3:5]),
            alt_eq[5].animate.align_to(alt_eq[3], UP),
            Uncreate(where_rect)
        )

        self.wait()

        self.play(
            Circumscribe(how_big_txt[5:8])
        )

        self.play(
            Circumscribe(null_eq[5])
        )

        self.wait()

        self.play(
            Circumscribe(where_txt[2:7])
        )

        self.play(
            Circumscribe(alt_eq[5])
        )

        self.wait()

        self.play(
            Write(null_eq[9:11]),
            GrowArrow(null_eq[11]),
            run_time=0.8
        )
        
        self.wait()

        self.play(
            Write(correspondence_eq),
            run_time=1
        )

        self.wait()

        reject_h0_txt.clear_updaters()

        self.play(
            FadeOut(*self.mobjects, shift=DOWN*0.2)
        )

        self.wait(0.1)





