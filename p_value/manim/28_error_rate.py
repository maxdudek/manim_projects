from manim import *
from probability_mobjects import *
from dudek_utils import *
confusion_table = __import__('27_confusion_table')

class _28_error_rate(Scene):
    def construct(self):

        table, null_world_table, alt_world_table, reject_txt, fail_txt = confusion_table.get_table_mobjects()

        Group(table, null_world_table, alt_world_table, reject_txt, fail_txt).scale(0.5).align_on_border(UR)

        h0_rect = SurroundingRectangle(Group(null_world_table, table.get_entries((2,1)))).stretch(1.3, dim=0).stretch(1.05, dim=1).shift(DOWN*0.1)
        
        null_world = GenericImageMobject("assets/null_world.png").scale(0.5).align_on_border(LEFT).set_y(2)
        alt_world = GenericImageMobject("assets/alt_world.png").scale(0.5).align_on_border(LEFT).set_y(-2)

        PROB_PINK="#F799E9"
        spinner_FP = Spinner(0.1, PROB_PINK, clockwise=True).scale(1.5).next_to(null_world, buff=0.5)
        brace_FP = Brace(spinner_FP, LEFT, sharpness=0.7).next_to(null_world, buff=0)
        spinner_FP.add_image(Text("TN", color=GREEN, font_size=36), angle=210*DEGREES)
        spinner_FP.add_image(Text("FP", color=RED_E, font_size=36), angle="prob", r=0.35)

        spinner_FN = Spinner(0.2, PROB_PINK, clockwise=True).scale(1.5).next_to(alt_world, buff=0.5)
        brace_FN = Brace(spinner_FN, LEFT, sharpness=0.7).next_to(alt_world, buff=0)
        spinner_FN.add_image(Text("TP", color=GREEN, font_size=36), angle=210*DEGREES)
        spinner_FN.add_image(Text("FN", color=RED_E, font_size=36), angle="prob", r=0.3)

        txt_PFP = Text("P(FP)", font_size=32, color=PROB_PINK).align_to(spinner_FP, UP).set_x(-1.1)
        txt_PFP[2:4].set_color(RED)
        FP_eq1 = MarkupText("= P(Reject H<sub>0</sub>)", font_size=32, color=PROB_PINK).next_to(txt_PFP, buff=0.15)
        FP_eq2 = Text('= "Type I error rate" (FPR)', font_size=32, color=PROB_PINK).next_to(FP_eq1, DOWN).align_to(FP_eq1, LEFT)
        FP_eq3 = Text('= P(a non-cheater gets lucky)', font_size=32, color=PROB_PINK).next_to(FP_eq2, DOWN).align_to(FP_eq2, LEFT)
        FP_eq4 = Text('= P(wrongly conclude cheating)', font_size=32, color=PROB_PINK).next_to(FP_eq3, DOWN).align_to(FP_eq3, LEFT)
        FP_eq5 = Text('= P(p ≤ 0.05)', font_size=32, color=PROB_PINK).next_to(FP_eq4, DOWN).align_to(FP_eq4, LEFT)
        FP_eq5[3].set_color(BLUE_TXT)
        FP_eq5_alt = Text('= P(p ≤ α)', font_size=32, color=PROB_PINK).next_to(FP_eq4, DOWN).align_to(FP_eq4, LEFT)
        FP_eq5_alt[3].set_color(BLUE_TXT)
        FP_eq6 = MarkupText("= P(x' ≥ x<sub>α</sub>)", font_size=32, color=PROB_PINK).next_to(FP_eq5, DOWN).align_to(FP_eq5, LEFT)
        FP_eq6[3:5].set_color(ORANGE)
        FP_eq6[6:8].set_color(RED)
        approx_txt = Text('≈', font_size=32, color=PROB_PINK).next_to(FP_eq6, RIGHT, buff=0.15)
        eq_txt = Text('=', font_size=32, color=PROB_PINK).next_to(FP_eq6, RIGHT, buff=0.15)
        leq_txt = Text('≤', font_size=32, color=PROB_PINK).next_to(FP_eq6, RIGHT, buff=0.15)
        alpha_txt = Text('α', font_size=32, color=PROB_PINK).next_to(approx_txt, RIGHT, buff=0.15)

        txt_PFN = Text("P(FN)", font_size=32, color=PROB_PINK).align_to(spinner_FN, UP).set_x(-1.1)
        txt_PFN[2:4].set_color(RED)
        FN_eq1 = MarkupText("= P(Fail to reject)", font_size=32, color=PROB_PINK).next_to(txt_PFN, buff=0.15)
        FN_eq2 = Text('= "Type II error rate" (FNR)', font_size=32, color=PROB_PINK).next_to(FN_eq1, DOWN).align_to(FN_eq1, LEFT)
        FN_eq1.set_z_index(1)

        mu_variable = Variable(0.6, MathTex("\mu", color=YELLOW))
        mu_variable.set_color(YELLOW)
        mu_equation = VGroup(
            mu_variable, Tex("?")
        ).arrange(RIGHT, buff=0.1).next_to(FN_eq2, DOWN, buff=0.5)
        mu_variable.label[0][0].shift(DOWN*0.05)

        power_eq = Text('P(TP) = 1 - P(FN) = "Power"', font_size=32, color=PROB_PINK).next_to(mu_equation, DOWN, buff=0.5).align_to(FN_eq1, LEFT)
        power_eq[2:4].set_color(GREEN)
        power_eq[10:12].set_color(RED)

        ####################################
        # Error rate calculation
        data_txt = Text("Data (x'/n)", font_size=50).move_to((-4.5,-3,0))
        data_txt[:4].set_color(ORANGE)
        data_txt[5:7].set_color(ORANGE)

        pmf_plot = PMFBarPlot.binom(
            n=100, p=0.5, width=7, height=2.7, 
            gap=0.03, alpha=1e-7, min_prob=0, x_prime = 59,
            x_label=Tex("$x$", font_size = 40), x_labels_font_size = 0,
            x_label_offset=UP*0.5,
        ).align_on_border(DR).shift(DOWN*0.2)

        pmf_plot.x_prime_line.set_z_index(1)
        pmf_plot.resume_updating()
        pmf_plot.x_prime_line.resume_updating()

        x_prime_label = Text("x'", font_size=32, color=ORANGE).next_to(pmf_plot.x_prime_line, UP)
        x_prime_label.add_updater(lambda v: v.next_to(pmf_plot.x_prime_line, UP))

        p_eq = Variable(0.044, "p", num_decimal_places=3).move_to((5.5,0.5,0))
        p_eq.set_color(BLUE).scale(0.8)
        p_eq.add_updater(lambda v: v.tracker.set_value(pbinom(
            round(pmf_plot.x_prime.get_value()),
            n=100,
            p=0.5
        )))
        p_eq.resume_updating()

        approx_alpha_txt = MathTex(r"\approx \alpha", font_size=40, color=PROB_PINK).move_to((5.8,-2.4,0))

        red_brace = BraceBetweenPoints(
            pmf_plot.x2bar(59).get_corner(UR),
            pmf_plot.x2bar(73).get_corner(UR),
            direction=UP, sharpness=1, color = PROB_PINK
        )
        
        red_brace.rotate(-13*DEGREES, about_point=red_brace.get_edge_center(LEFT)).shift(DOWN*0.1)

        x_alpha_x = pmf_plot.x2bar(59).get_x()
        x_alpha_y = pmf_plot.get_edge_center(UP)[1]-0.1
        x_alpha_line = Line(
            (x_alpha_x, x_alpha_y, 0),
            pmf_plot.x2bar(59).get_edge_center(DOWN)+DOWN*0.1,
            color=RED
        ).set_z_index(1)
        x_alpha_txt = MarkupText("x<sub>α</sub>", font_size=32, color=RED).next_to(x_alpha_line, DOWN, buff=0.1)

        rejection_region_txt = Text("rejection\nregion", slant=ITALIC, font_size=32, color=PROB_PINK).move_to((5.8,-1.4,0))

        reject_h0_txt = MarkupText("Reject H<sub>0</sub>!", font_size=40, color=PROB_PINK).next_to(data_txt, UP, buff=1)
        reject_h0_txt.add_updater(lambda v: v.set_opacity(1 if pmf_plot.x_prime.get_value() > 59 else 0))

        pmf_plot_1000 = PMFBarPlot.binom(
            n=1000, p=0.5, width=7, height=2.7, 
            gap=0.01, alpha=5e-7, min_prob=0, x_prime = 527,
            x_label=Tex("$x$", font_size = 40), x_labels_font_size = 0,
            x_label_offset=UP*0.5,
        ).align_on_border(DR).shift(DOWN*0.2)
        pmf_plot_1000.x_prime_line.resume_updating()

        # Set and freeze colors
        pmf_plot_1000.freeze_bars()
        for i in range(len(pmf_plot_1000.bars)):
            pmf_plot_1000.bars[i].set_color(PROB_PINK if pmf_plot_1000.i2x(i) >= 527 else pmf_plot_1000.color2)

        significance_threshold_txt = Text("significance threshold", font_size=48, slant=ITALIC).set_y(-2.2)

        #################################################################
        # Animation (1)                                                 #
        #################################################################
        # self.add(NumberPlane(
        #     background_line_style={
        #         "stroke_width": 2,
        #         "stroke_opacity": 0.6
        #     }).set_z_index(-2))
       
        # self.add(h0_rect)
        # self.add(alt_world, spinner_FN, brace_FN, txt_PFN, FN_eq1, FN_eq2, mu_equation, power_eq)
        # self.add(spinner_FP, null_world, brace_FP, txt_PFP, 
        #          FP_eq1, FP_eq2, FP_eq3, FP_eq4, FP_eq5, FP_eq6, eq_txt, alpha_txt)
        # self.add(data_txt, pmf_plot, pmf_plot.x_prime_line, x_prime_label, p_eq, approx_alpha_txt, 
        #          red_brace, x_alpha_line, x_alpha_txt, rejection_region_txt, reject_h0_txt, significance_threshold_txt)

        self.add(table, null_world_table, alt_world_table, reject_txt, fail_txt)

        self.wait()

        self.play(
            Create(h0_rect)
        )

        self.wait()

        self.play(
            FadeIn(spinner_FP, null_world, brace_FP),
            run_time=0.5
        )

        self.play(
            Write(VGroup(txt_PFP, FP_eq1)),
            run_time=1
        )

        self.wait(0.1)

        self.play(
            Uncreate(h0_rect)
        )

        self.play(
            Group(table, null_world_table, alt_world_table, reject_txt, fail_txt).animate.align_on_border(DR)
        )

        h1_rect = SurroundingRectangle(Group(alt_world_table, table.get_entries((2,2)))).stretch(1.3, dim=0).stretch(1.05, dim=1).shift(DOWN*0.1)

        self.play(
            Create(h1_rect)
        )

        self.wait()

        self.play(
            FadeIn(spinner_FN, alt_world, brace_FN),
            run_time=0.5
        )

        self.play(
            Write(VGroup(txt_PFN, FN_eq1)),
            run_time=1
        )

        self.wait()

        self.play(
            FadeOut(table, null_world_table, alt_world_table, reject_txt, fail_txt, h1_rect),
            Write(FP_eq2),
            run_time=0.8
        )

        self.wait()

        self.play(
            Write(FN_eq2),
            run_time=0.8
        )

        self.wait()

        self.play(
            Write(mu_equation),
            run_time=0.8
        )

        self.play(
            mu_variable.tracker.animate.set_value(0.85),
            spinner_FN.probability.animate.set_value(0.1),
            run_time=1
        )

        self.play(
            mu_variable.tracker.animate.set_value(0.6),
            spinner_FN.probability.animate.set_value(0.2),
            run_time=1
        )

        self.wait()

        self.play(
            Write(power_eq),
            run_time=1
        )

        self.wait()

        self.play(
            FadeOut(mu_equation, spinner_FN, alt_world, brace_FN, txt_PFN, FN_eq1, FN_eq2, power_eq)
        )

        self.wait()

        self.play(
            Circumscribe(null_world, shape=Circle, buff=-0.3)
        )

        self.wait()

        self.play(
            Write(FP_eq3),
            run_time=0.8
        )

        self.play(
            Write(FP_eq4),
            run_time=0.8
        )

        self.wait()

        self.play(
            Write(FP_eq5)
        )

        self.wait()

        self.play(
            ReplacementTransform(FP_eq5[5:-1], FP_eq5_alt[-2]),
            ReplacementTransform(FP_eq5[-1], FP_eq5_alt[-1])
        )

        self.wait()

        self.play(
            Indicate(VGroup(FP_eq5[3:5], FP_eq5_alt[-2]), scale_factor=1.4),
            run_time=1.5
        )

        self.wait()

        self.play(
            Write(data_txt)
        )

        self.wait()

        self.play(
            FadeIn(pmf_plot, pmf_plot.x_prime_line, x_prime_label)
        )

        self.play(
            Write(p_eq),
            run_time=0.6
        )

        self.wait()

        self.play(
            pmf_plot.x_prime.animate.set_value(66),
            run_time=2
        )

        self.play(
            pmf_plot.x_prime.animate.set_value(42),
            run_time=2.5
        )

        self.wait(0.5)

        self.play(
            pmf_plot.x_prime.animate.set_value(59),
            run_time=3
        )

        self.wait()

        self.play(
            Circumscribe(p_eq)
        )

        self.wait()

        self.play(
            Uncreate(pmf_plot.x_prime_line),
            FadeOut(x_prime_label)
        )

        self.play(
            Create(x_alpha_line),
            Write(x_alpha_txt)
        )
        
        pmf_plot.freeze_bars()

        self.wait()

        self.add(reject_h0_txt)

        pmf_plot.x_prime.set_value(52)
        pmf_plot.x_prime_line.resume_updating()
        x_prime_label.resume_updating()

        self.play(
            Create(pmf_plot.x_prime_line.reverse_points()),
            Write(x_prime_label)
        )

        self.play(
            pmf_plot.x_prime.animate.set_value(64),
            run_time=2
        )

        self.play(
            pmf_plot.x_prime.animate.set_value(52),
            run_time=2
        )

        self.wait()

        # Recolor bars
        self.play(
            AnimationGroup([
                pmf_plot.bars[i].animate.set_color(PROB_PINK if pmf_plot.i2x(i) >= 59 else pmf_plot.color2)
                for i in range(len(pmf_plot.bars))
            ]),
            Write(rejection_region_txt),
            run_time=0.8
        )

        self.play(
            pmf_plot.x_prime.animate.set_value(64),
            run_time=1.5
        )

        self.play(
            pmf_plot.x_prime.animate.set_value(53),
            run_time=1.5
        )

        self.wait()

        self.play(
            Create(red_brace),
            Write(approx_alpha_txt)
        )

        p_eq_pink = MathTex("p = 0.044", color=PROB_PINK).move_to(rejection_region_txt)
        p_eq_pink2 = MathTex("p = 0.047", color=PROB_PINK).move_to(rejection_region_txt)

        self.wait(0.5)

        self.play(
            pmf_plot.x_prime.animate.set_value(64),
            run_time=1.5
        )

        self.play(
            pmf_plot.x_prime.animate.set_value(53),
            run_time=1.5
        )

        self.wait(0.5)

        self.play(
            Write(FP_eq6),
            run_time=0.7
        )

        self.wait()

        self.play(
            Indicate(
                VGroup([
                    pmf_plot.bars[i] for i in range(len(pmf_plot.bars))
                ]),
                scale_factor=1.05
            ),
            run_time=1.5
        )

        self.wait()

        self.play(
            Indicate(
                VGroup([
                    pmf_plot.bars[i] for i in range(len(pmf_plot.bars)) if pmf_plot.i2x(i) >= 59
                ]),
                scale_factor=1.05
            ),
            run_time=1.5
        )

        self.wait()

        self.play(
            FadeOut(rejection_region_txt, p_eq)
        )

        self.play(
            Circumscribe(approx_alpha_txt),
            Write(p_eq_pink),
            run_time=0.7
        )

        self.wait()

        self.play(
            Write(VGroup(approx_txt, alpha_txt)),
            run_time=0.7
        )

        self.wait()

        self.play(
            ReplacementTransform(pmf_plot, pmf_plot_1000),
            # FadeOut(pmf_plot.x_prime_line, x_prime_label, shift=np.array([0,0,0])),
            Group(x_alpha_line, x_alpha_txt).animate.set_x(pmf_plot_1000.x2bar(527).get_x()),
            ReplacementTransform(p_eq_pink, p_eq_pink2)
        )

        self.wait()

        self.play(
            Circumscribe(x_alpha_txt)
        )

        self.wait()

        self.play(
            FadeOut(approx_txt),
            FadeIn(eq_txt),
        )        

        self.wait()

        self.play(
            FadeOut(eq_txt),
            FadeIn(leq_txt),
        ) 

        self.wait(0.1)

        self.play(
            FadeOut(leq_txt),
            FadeIn(eq_txt),
        )       

        self.wait()

        x_prime_label.clear_updaters()

        self.play(
            FadeOut(pmf_plot_1000, red_brace, approx_alpha_txt, data_txt, reject_h0_txt, x_alpha_line, x_alpha_txt,
                    FP_eq1, FP_eq2, FP_eq3, FP_eq4, FP_eq5, FP_eq5_alt, FP_eq6, p_eq_pink2, pmf_plot.x_prime_line, x_prime_label),
            txt_PFP.animate.set_y(-0.5).scale(1.5),
            Group(eq_txt, alpha_txt).animate.next_to(txt_PFP, RIGHT, buff=0.6).set_y(-0.5).scale(1.5),
        )

        self.play(
            Circumscribe(Group(txt_PFP, alpha_txt))
        )

        arrow = Arrow(
            significance_threshold_txt.get_edge_center(UP),
            alpha_txt.get_edge_center(DOWN)
        )

        self.play(
            Write(significance_threshold_txt),
            GrowArrow(arrow),
            run_time=1
        )

        self.wait()

        reject_h0_txt.clear_updaters()

        self.play(
            FadeOut(*self.mobjects, shift=DOWN*0.2)
        )

        self.wait(0.1)





