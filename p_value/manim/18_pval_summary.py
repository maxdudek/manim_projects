from manim import *
from probability_mobjects import *
from dudek_utils import *

class PvalSummary(Scene):
    def construct(self):
        alex=GenericImageMobject("assets/alex.webp").move_to((-5.3,-2,0)).scale_to_fit_height(3)

        how_lucky_txt = MarkupText("<i>How lucky</i>\nwould they\nhave to be?", font_size=42).move_to((-2,0,0))

        p_value_txt = Tex("$p$-value", color = BLUE, font_size=72).next_to(how_lucky_txt, RIGHT).shift(RIGHT*3)

        lucky_double_arrow = DoubleArrow(
            start = how_lucky_txt.get_edge_center(RIGHT),
            end = p_value_txt.get_edge_center(LEFT)
        )

        p_value_header = Text("p-value:", weight = BOLD, font_size=48, color = BLUE).move_to((0,3,0))

        p_value_definition = Tex(
            r"""
            \begin{flushleft}
            The probability of getting a result \textit{at least}\\
            as extreme as the data that we see,\\
            given that the null hypothesis ($H_0$) is true.
            \end{flushleft}
            """,
            font_size = 55
        ).next_to(p_value_header, DOWN, buff=0.5)

        low_p_value_txt = Tex("Low $p$-value").move_to((-2.5,-0.5,0))

        result_unlikely_txt = Tex("Result unlikely in $H_0$").move_to((3,-0.5,0))

        double_arrow = DoubleArrow(
            low_p_value_txt.get_edge_center(RIGHT),
            result_unlikely_txt.get_edge_center(LEFT),
            max_tip_length_to_length_ratio = 0.15
        )

        alpha = DecimalNumber(0.05)
        p_ineq = VGroup(
            MathTex("p < "), alpha
        ).arrange(RIGHT, buff=0.1).next_to(low_p_value_txt, DOWN, buff=1)

        q_txt = Text("?", font_size=30).next_to(alpha, UP)

        null_world = GenericImageMobject("assets/null_world.png").scale(0.4).set_y(p_ineq.get_y()).set_x(0.3)

        x_mark = VGroup(
            Line(null_world.get_corner(UL), null_world.get_corner(DR), color=RED, stroke_width=8),
            Line(null_world.get_corner(UR), null_world.get_corner(DL), color=RED, stroke_width=8)
        )

        reject_txt = Text("Reject", font_size=36).next_to(null_world, RIGHT)

        significant_txt = Text("Statistically significant", font_size=30, slant=ITALIC).set_y(-3).align_to(reject_txt, LEFT)

        threshold_txt = Text("Significance threshold", font_size=30, slant=ITALIC).next_to(p_ineq, DOWN).set_y(-3)

        p_arrow = Arrow(
            p_ineq.get_edge_center(RIGHT),
            null_world.get_edge_center(LEFT)
        )

        threshold_arrow = Arrow(
            threshold_txt.get_edge_center(UP),
            alpha.get_edge_center(DOWN),
            buff=0.1
        )

        p_eq = MathTex("p = 0.0004").move_to((-2,-1.5,0))

        steve_devil = GenericImageMobject("assets/steve_devil.png").scale(0.4).next_to(p_eq, RIGHT, buff=1.5)

        devil_arrow = Arrow(
            p_eq.get_edge_center(RIGHT),
            steve_devil.get_edge_center(LEFT),
            buff=0.2
        )

        p_eq_wrong = MathTex(r"p = 0.0004 \neq P(\text{friend didn't cheat})").align_on_border(DOWN)
        p_eq_wrong[0][8:].set_color(RED)

        correct_eq = MathTex(r"p = P(X \mathbf{\geq}~ 67)", font_size = 60).move_to((0,1.5,0))
        correct_eq[0][5].set_color(GREEN)

        why_not_txt = Text("Why not:").next_to(correct_eq, DOWN, buff=1)

        incorrect_eq = MathTex(r"p = P(X \mathbf{=}~ 67) \text{?}", font_size = 60).next_to(why_not_txt, DOWN, buff=0.5)
        incorrect_eq[0][5].set_color(RED)

        #################################################################
        # Animation (1)                                                 #
        #################################################################
        # Testing
        # self.add(NumberPlane(), Dot(ORIGIN))
        # self.add(alex, p_value_header, p_value_definition)
        # self.add(low_p_value_txt, result_unlikely_txt, double_arrow,
        #          p_ineq, p_arrow, q_txt, null_world, x_mark, reject_txt,
        #          significant_txt, threshold_txt, threshold_arrow)

        self.play(
            FadeIn(alex, shift=DOWN*0.2),
            Write(how_lucky_txt),
            Write(VGroup(p_value_txt, lucky_double_arrow))
        )

        self.wait()

        self.play(
            FadeOut(how_lucky_txt, p_value_txt, lucky_double_arrow, shift=DOWN*0.1)
        )

        self.wait()

        self.play(
            FadeIn(p_value_header, shift=DOWN*0.2, run_time=0.5),
            Write(p_value_definition, run_time=3),
            run_time=3
        )
        
        self.wait()

        self.play(
            Write(low_p_value_txt)
        )

        self.wait()

        self.play(
            Write(result_unlikely_txt),
            Create(double_arrow)
        )

        self.wait()

        self.play(
            FadeIn(null_world, shift=DOWN*0.1),
            Create(x_mark),
            Write(reject_txt)
        )

        self.wait()

        self.play(
            Create(p_arrow),
            Write(p_ineq)
        )

        self.wait()

        self.play(
            Write(q_txt),
            Circumscribe(alpha)
        )

        self.wait()

        self.play(
            alpha.animate.set_value(0.01)
        )

        self.wait()

        self.play(
             alpha.animate.set_value(0.05),
             FadeOut(q_txt)
        )

        self.wait()

        self.play(
            Write(threshold_txt),
            Create(threshold_arrow),
            Circumscribe(alpha)
        )

        self.wait()

        self.play(
            Write(significant_txt)
        )

        self.wait()

        self.play(
            FadeOut(p_value_header, p_value_definition, shift=UP*0.1),
            Group(
                alex, low_p_value_txt, result_unlikely_txt, double_arrow,
                p_ineq, p_arrow, null_world, x_mark, reject_txt,
                significant_txt, threshold_txt, threshold_arrow
            ).animate.shift(UP*3.5)
        )

        self.wait()

        self.play(
            Write(p_eq)
        )

        self.wait()

        self.play(
            FadeIn(steve_devil, shift=DOWN*0.1),
            Create(devil_arrow)
        )

        self.wait()

        self.play(
            Write(p_eq_wrong)
        )

        self.wait()

        self.play(
            FadeOut(
                low_p_value_txt, result_unlikely_txt, double_arrow,
                p_ineq, p_arrow, null_world, x_mark, reject_txt,
                significant_txt, threshold_txt, threshold_arrow,
                p_eq, steve_devil, devil_arrow, p_eq_wrong,
                shift=DOWN*0.1
            ),
            alex.animate.move_to((-4.5,0,0))
        )

        self.wait()

        self.play(
            Write(correct_eq)
        )

        self.wait()

        self.play(
            Write(VGroup(why_not_txt, incorrect_eq))
        )

        self.wait()

        self.play(
            FadeOut(*self.mobjects, shift=DOWN*0.1)
        )

        self.wait()

        