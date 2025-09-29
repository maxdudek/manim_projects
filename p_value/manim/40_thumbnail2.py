from manim import *
from probability_mobjects import *
from dudek_utils import *

class _40_thumbnail(Scene):
    def construct(self):
        
        part2_txt = Tex(r"\textbf{Part 2}", color=RED, font_size=124)

        p_value_txt = Tex("$p$-value", font_size=78, color=BLUE_TXT).next_to(part2_txt, UP, buff=0.7)

        steve_48 = GenericImageMobject("assets/steve_48.png", scale_to_resolution=2160).scale(1.2).align_on_border(UR, buff=0.8).shift(UP*0.3)

        alex_devil = GenericImageMobject("assets/alex_devil.png").scale_to_fit_height(3).align_on_border(DL, buff=0.5).shift(RIGHT*0.1)

        spinner_FP = Spinner(0.1, PROB_PINK, clockwise=True).scale(1.2).next_to(alex_devil, RIGHT, buff=0.2)
        spinner_FP.add_image(Text("TN", color=GREEN, font_size=32), angle=210*DEGREES)
        spinner_FP.add_image(Text("FP", color=RED_E, font_size=32), angle="prob", r=0.35)

        fp_eq = MathTex(r"P(\text{FP}) = P(p \leq \alpha) = \alpha", font_size=38).next_to(part2_txt, LEFT).align_on_border(LEFT,buff=0.4).shift(UP*0.5)

        normal_grid, normal_density, z_score, normal_area, z_line, z_label = pdf_plot(
            dnorm, xmin=-3.5, xmax=3.5, ymax=0.45, x_length=4.1, y_length=2.1, where=(-4.7,2.2,0)
        )
        z_label.shift(DOWN*0.15)

        pmf_plot = PMFBarPlot.binom(
            n=100, p=0.5, width=5.5, height=2.3, 
            gap=0.03, alpha=1e-6, min_prob=0, x_prime = 54,
            x_label=None, x_labels_font_size = 0,
            x_label_offset=UP*0.5, show_y_label=False, y_nums=False,
        ).align_on_border(DR)

        pmf_plot.x_prime_line.set_z_index(1)
        pmf_plot.resume_updating()
        pmf_plot.x_prime_line.resume_updating()

        x_prime_label = Text("x'", font_size=32, color=ORANGE).next_to(pmf_plot.x_prime_line, UP, buff=0.1)

        for i in range(len(pmf_plot.bars)):
            pmf_plot.bars[i].set_color(PROB_PINK if pmf_plot.i2x(i) >= 58 else pmf_plot.color2)
                
        EFP_txt = Tex(r"E[\#FP] $= m \alpha$", font_size = 40).next_to(steve_48, DOWN)

        red_circle = Circle(0.28, color=RED).move_to((3.2, 2.77,0))

        black_rect = Rectangle(color=BLACK, height=0.4, width=part2_txt.width, fill_opacity=1).next_to(part2_txt, DOWN, buff=0.05)

        #################################################################
        # Animation (1)                                                 #
        #################################################################
        # Testing
        # self.add(NumberPlane(
        #     background_line_style={
        #         "stroke_width": 2,
        #         "stroke_opacity": 0.6
        #     }).set_z_index(-2))
        self.add(
            part2_txt, p_value_txt, steve_48, alex_devil, spinner_FP, fp_eq,
            normal_grid, normal_density, normal_area, z_line, z_label, 
            pmf_plot, pmf_plot.x_prime_line, x_prime_label, EFP_txt, red_circle, black_rect
        )
        

        






