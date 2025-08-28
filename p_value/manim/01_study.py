from manim import *
# import numpy as np
from math import *
# from scipy.stats import binom
from dudek_utils import *

class Study(Scene):
    def construct(self):

        # Alex
        alex=GenericImageMobject("assets/alex.webp").move_to((-5,-0.5,0))
        alex.height=3.5

        # Thought bubble
        pie=GenericImageMobject("assets/pie.png").scale(2)
        pill=GenericImageMobject("assets/pill.png").scale(2)

        bubble = GenericImageMobject("assets/thought_bubble.png").scale_to_fit_height(2.8).move_to((-2.8,2.4,0))
        equation = Group(pie, MathTex("="), pill).arrange(RIGHT, buff=0.2).move_to(bubble).shift(UP*0.2)

        # Paper
        paper_border = Rectangle(width=4, height=5.5, color=WHITE).move_to((3,0,0))
        
        paper_title = Paragraph("Super Legit\nMedical Journal", 
                           font_size=28, color=PINK, alignment="center")
        paper_title.move_to(paper_border.get_top() + DOWN * 0.8)
        
        # Paper text
        p_text = "p = 0.049"
        statement = f"we find that eating pie is \nsignificantly associated with\ncancer remission ({p_text})"
        MARGIN = 0.2
        paper_text = Paragraph(("."*45 + "\n")*3 + "."*8 + statement + "."*2 + "\n" + ("."*45 + "\n")*3, 
                              color=WHITE, alignment="left", width=paper_border.width-2*MARGIN, line_spacing=1)
        
        paper_text.align_to(paper_title.get_bottom(), UP).shift(DOWN * 0.5)
        paper_text.align_to(paper_border.get_left(), LEFT).shift(RIGHT * MARGIN)

        p_text = paper_text[5][15:24]

        # P-value number line
        number_line = NumberLine(
            x_range=[0, 1, 0.1],
            length=4,
            include_numbers=True,
            numbers_to_include=[0, 0.5, 1.0]
        ).move_to((-2,-3.2,0)) 

        p_value = 0.05

        p_value_dot = Dot(radius=0.15, color=BLUE)
        p_value_dot.move_to(number_line.n2p(p_value))

        p_label = Variable(p_value, MathTex("p"), num_decimal_places=2)
        p_label.label.set_color(BLUE)
        p_label.value.set_color(BLUE)
        p_label.move_to(number_line.n2p(0.5) + UP*0.7)
        p_label.add_updater(lambda v: v.tracker.set_value(number_line.p2n(p_value_dot.get_center())))
        
        signif_eq = Group(
            pie.copy(), MathTex("="), pill.copy()
        ).arrange(RIGHT, buff=0.1).move_to(number_line.n2p(0)).shift(UP*0.5+LEFT*0.1).scale(0.6)

        non_signif_eq = Group(
            pie.copy(), MathTex(r"\neq"), pill.copy()
        ).arrange(RIGHT, buff=0.1).move_to(number_line.n2p(1)).shift(UP*0.5+LEFT*0.1).scale(0.6)

        pval_number_line_group = Group(number_line, p_value_dot, p_label, signif_eq, non_signif_eq)

        significant_txt = Text("significant", font_size=36).move_to((-1.5,0.5,0))

        confident_txt = Text("confident", font_size=36).next_to(significant_txt, DOWN, buff=1)

        double_arrow = DoubleArrow(
            start=significant_txt.get_edge_center(DOWN),
            end=confident_txt.get_edge_center(UP),
            buff=0.2
        )

        #################################################################
        # Animation (1)                                                 #
        #################################################################
        # Testing
        # self.add(alex, equation, bubble, paper_border, paper_title, paper_text, 
        #          pval_number_line_group, significant_txt, confident_txt, double_arrow)

        self.play(
            FadeIn(alex, shift=DOWN*0.1),
            FadeIn(paper_title, paper_border, shift=DOWN*0.1)
        )
        self.play(Write(paper_text[:3], rate_func=rate_functions.linear), run_time=0.3)
        for i in range(3):  self.play(AddTextLetterByLetter(paper_text[3:6][i]), run_time=0.6)
        self.play(Write(paper_text[6:], rate_func=rate_functions.linear), run_time=0.3)
        self.wait(0.5)
        self.play(Indicate(p_text), run_time=2)

        self.play(LaggedStart(
            FadeIn(bubble), 
            FadeIn(equation),
            lag_ratio=0.25,
            run_time=1
        ))
        self.wait(2)

        self.play(FadeIn(pval_number_line_group, shift=DOWN*0.1))

        self.play(p_value_dot.animate.move_to(number_line.n2p(0.35)), run_time = 2)
        self.wait(0.5)
        self.play(p_value_dot.animate.move_to(number_line.n2p(0.05)), run_time = 2)

        self.wait()

        self.play(
            Write(significant_txt)
        )

        self.wait()

        self.play(
            Create(double_arrow),
            Write(confident_txt)
        )

        # # Transition to next slide
        self.wait()
        self.play(
            FadeOut(alex, equation, bubble, significant_txt, confident_txt, double_arrow,
                    paper_border, paper_title, paper_text, shift=DOWN*0.1),
            pval_number_line_group.animate.move_to((0,2.5,0))
        )

        # #################################################################
        # # Slide 2                                                       #
        # #################################################################

        probability_eq_1 = Group(
            MathTex("p = P("), non_signif_eq.copy(), MathTex(") ?")
        ).arrange(RIGHT, buff=0.1).move_to((0,0,0))

        big_P = probability_eq_1[0][0][2]
        little_p = probability_eq_1[0][0][0]

        probability_eq_2 = Group(
            MathTex("1-p = P("), signif_eq.copy(), MathTex(") ?")
        ).arrange(RIGHT, buff=0.1).move_to(probability_eq_1.get_center() + DOWN*1 + LEFT*0.4)

        one_minus_little_p = probability_eq_2[0][0][0:3]

        x_center = (probability_eq_1.get_center() + probability_eq_2.get_center())/2
        x_height, x_width = 1, 2.5
        x_mark = VGroup(
            Line(x_center+UP*x_height+LEFT*x_width, x_center+DOWN*x_height+RIGHT*x_width, color=RED),
            Line(x_center+UP*x_height+RIGHT*x_width, x_center+DOWN*x_height+LEFT*x_width, color=RED)
        )

        question_mark = Text("?", font_size=96).move_to(x_center)

        p_value_header = Text("p-value:", weight = BOLD, font_size=48, color = BLUE).move_to((0,3,0))
        p_value_definition = Paragraph("The probability of getting a result at \nleast as extreme as the data that we see,\ngiven that the null hypothesis is true.",
                                       alignment="left", font_size = 36).move_to((0,1.5,0))

        alex.move_to((-4,-2,0))

        stats_equations = MathTex(
            r"""
            P(X \geq x) = \sum_{k=x}^n \binom{n}{k} p^k(1-p)^{n-k} \\[0.25em]
            \Phi \left(z = \frac{x-\mu}{\sigma}\right) = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^z e^{-t^2/2} dt
            """,
            font_size = 32
        ).move_to((3.3,-1,0))

        #################################################################
        # Animation (2)                                                 #
        #################################################################

        # Testing
        # self.add(probability_eq_1, probability_eq_2, x_mark)
        # self.add(alex, question_mark, stats_equations)
        # self.add(alex, p_value_header, p_value_definition, stats_equations)

        self.play(FadeIn(probability_eq_1, shift = DOWN*0.3))

        self.wait()

        self.play(
            Indicate(big_P),
            run_time=2
        )
        self.wait()
        self.play(
            Indicate(little_p),
            run_time=2
        )

        self.wait()

        self.play(FadeIn(probability_eq_2, shift = DOWN*0.3))

        self.wait()

        self.play(Transform(little_p, 
                            MathTex("0.05").move_to(probability_eq_1).align_to(little_p, RIGHT)))
        
        self.wait()

        self.play(Transform(one_minus_little_p, 
                            MathTex("0.95").move_to(probability_eq_2).align_to(one_minus_little_p, RIGHT)))
        self.wait()
        self.play(Create(x_mark))

        self.wait()
        self.play(FadeOut(probability_eq_1, probability_eq_2, x_mark, pval_number_line_group))

        self.wait()
        
        self.play(
            FadeIn(alex, shift=UP*0.5),
            Write(question_mark)
        )

        self.wait()

        self.play(
            FadeOut(question_mark), 
            Write(p_value_header),
            Write(p_value_definition, run_time=3)
        )

        self.wait()

        self.play(Write(stats_equations))

        self.wait()

        self.play(
            FadeOut(*self.mobjects, shift=DOWN*0.1)
        )

        self.wait()


