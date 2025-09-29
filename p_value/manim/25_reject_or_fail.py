from manim import *
from probability_mobjects import *
from dudek_utils import *

class _25_reject_or_fail(Scene):
    def construct(self):

        ST_FPR_txt = Text("Significance threshold =\nFalse Positive Rate", font_size=72, line_spacing=0.5)

        alex=GenericImageMobject("assets/alex.webp").scale_to_fit_height(3.5).align_on_border(DL).shift(RIGHT*0.3)

        big_bubble = GenericImageMobject("assets/thought_bubble_big.png").scale_to_fit_height(3.9).move_to((0,1.9,0)).stretch(1.17, dim=0)

        or_txt = Text("or", font_size=36).move_to(big_bubble).shift(UP*0.3)

        null_world = GenericImageMobject("assets/null_world.png").scale(0.5).next_to(or_txt, LEFT)
        alt_world = GenericImageMobject("assets/alt_world.png").scale(0.5).next_to(or_txt, RIGHT)

        p_def = Tex("$p = P$(result at least as extreme) if $H_0$ is true").next_to(big_bubble, DOWN).shift(RIGHT*0.9)
        p_def[0][0].set_color(BLUE_TXT)

        null_eq = MathTex(r"\mu = 0.5", font_size=36).next_to(null_world, DOWN, buff=0.15)
        alt_eq = MathTex(r"\mu > 0.5", color=YELLOW, font_size=36).next_to(alt_world, DOWN, buff=0.15)

        # Reject H0
        h0_reject = GenericImageMobject("assets/null_world.png").scale(0.5).move_to((-2.5,-2.8,0))
        h1_reject = GenericImageMobject("assets/alt_world.png").scale(0.5).next_to(h0_reject, RIGHT, buff=0.1)
        reject_txt = Tex("Reject $H_0$").next_to(Group(h0_reject, h1_reject), UP)
        X_SIZE=-0.1
        x_reject = VGroup(
            Line(h0_reject.get_corner(UR)+UR*X_SIZE, h0_reject.get_corner(DL)+DL*X_SIZE, color=RED, stroke_width=10),
            Line(h0_reject.get_corner(UL)+UL*X_SIZE, h0_reject.get_corner(DR)+DR*X_SIZE, color=RED, stroke_width=10),
        )
        arrow_reject = Arrow(
            (0,0.5,0),
            reject_txt.get_edge_center(UP)+UP*0.2,
            stroke_width=8,
            buff=0
        )
        p_reject_txt = MathTex("p \leq 0.05").move_to((-2.3,-0.3,0))
        p_reject_txt[0][0].set_color(BLUE_TXT)

        # Fail to reject
        h0_fail = GenericImageMobject("assets/null_world.png").scale(0.5).move_to((2.8,-2.8,0))
        or_fail_txt = Text("or", font_size=36).next_to(h0_fail, RIGHT, buff=0.1)
        h1_fail = GenericImageMobject("assets/alt_world.png").scale(0.5).next_to(or_fail_txt, RIGHT, buff=0.2)
        fail_txt = Tex(r"\textit{Fail to reject} $H_0$").next_to(Group(h0_fail, h1_fail), UP)
        arrow_fail = Arrow(
            (0,0.5,0),
            fail_txt.get_edge_center(UP)+UP*0.2,
            stroke_width=8,
            buff=0
        )
        p_fail_txt = MathTex("p > 0.05").move_to((4,0,0))
        p_fail_txt[0][0].set_color(BLUE_TXT)

        accept_txt = Tex("accept $H_0$?", font_size=36).next_to(fail_txt, UP).align_to(fail_txt, RIGHT).shift(RIGHT*0.2)

        accept_cross = Line(
            accept_txt.get_edge_center(LEFT)+LEFT*0.1,
            accept_txt.get_edge_center(RIGHT)+RIGHT*0.1,
            color=RED,
            stroke_width = 5,
        )

        #################################################################
        # Animation (1)                                                 #
        #################################################################
        # self.add(NumberPlane(
        #     background_line_style={
        #         "stroke_width": 2,
        #         "stroke_opacity": 0.6
        #     }))
        # self.add(alex, big_bubble, or_txt, null_world, alt_world, h0_reject, h1_reject, reject_txt, x_reject,
        #          h0_fail, h1_fail, or_fail_txt, h1_fail, fail_txt, arrow_reject, arrow_fail, p_reject_txt, p_fail_txt, 
        #          accept_txt, accept_cross, null_eq, alt_eq)
        
        self.play(
            Write(ST_FPR_txt)
        )

        self.wait()

        self.play(
            Unwrite(ST_FPR_txt, reverse=False)
        )

        self.play(
            FadeIn(alex)
        )

        self.wait()

        self.play(
            FadeIn(big_bubble, null_world, alt_world, or_txt, alt_eq, null_eq, shift=UP*0.5)
        )

        self.wait()

        self.play(
            Write(p_def),
            run_time=1
        )

        self.wait()

        self.play(
            AnimationGroup(
                FadeOut(p_def),
                AnimationGroup(
                    GrowArrow(arrow_reject),
                    Write(p_reject_txt)
                ),
                lag_ratio=0.5
            ),
            run_time=1
        )

        self.wait()

        self.play(
            Write(reject_txt),
            FadeIn(h0_reject, h1_reject),
            run_time=0.8
        )

        self.play(
            Create(x_reject)
        )

        self.wait()

        self.play(
            GrowArrow(arrow_fail),
            Write(p_fail_txt),
            run_time=0.8
        )

        self.wait(0.5)

        self.play(
            Write(fail_txt),
            FadeIn(h0_fail, or_fail_txt, h1_fail),
            run_time=0.8
        )
        
        self.wait()

        self.play(
            Write(accept_txt),
            run_time=0.6
        )

        self.play(
            Create(accept_cross)
        )

        self.wait()

        self.play(
            Circumscribe(null_eq)
        )

        self.wait()
    
        self.play(
            FadeOut(*self.mobjects, shift=DOWN*0.2)
        )

        self.wait(0.1)





