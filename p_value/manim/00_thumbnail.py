from manim import *
from probability_mobjects import *
from dudek_utils import *

class Thumbnail(Scene):
    def construct(self):

        
        steve_angel = GenericImageMobject("assets/steve_angel.png").scale_to_fit_width(3.2).move_to((-4.3,-1.5,0)).rotate(-15*DEGREES)
        steve_devil = GenericImageMobject("assets/steve_devil_flipped.png").scale_to_fit_width(3.2).move_to((4.3,-1.5,0)).rotate(15*DEGREES)

        p_txt = Tex("$p = $ ?", font_size = 96).set_y(2)
        rectangle = SurroundingRectangle(p_txt, color=RED, stroke_width = 10, buff=0.4)

        lucky_txt = Text(
            "Lucky?", font_size=72
        ).next_to(steve_angel, UP, buff=0.8)
        cheating_txt = Text(
            "Cheating?", font_size=72, color=YELLOW
        ).next_to(steve_devil, UP, buff=0.8)

        pmf_plot = PMFBarPlot.binom(
            n=100, p=0.5, width=9, height=3, 
            gap=0.05, alpha=1e-8, min_prob=0, x_prime=57, y_nums=False,
            x_label=Tex("", font_size = 40)
        ).align_on_border(DOWN, buff=0)

        arrow = Arrow(
            pmf_plot.x2bar(50).get_edge_center(UP),
            rectangle.get_edge_center(DOWN),
            buff = 0.1,
            color = RED,
            stroke_width=20,
            max_tip_length_to_length_ratio=0.3
        )


        rod = GenericImageMobject("assets/rod.png").next_to(pmf_plot.x_prime_line, UP, buff=0)


        self.add(pmf_plot.axes, pmf_plot.bars, pmf_plot.x_prime_line,
                 lucky_txt, cheating_txt, steve_angel, steve_devil, 
                 p_txt, rectangle, arrow, rod)

        