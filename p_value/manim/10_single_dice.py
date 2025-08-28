from manim import *
from probability_mobjects import *
from dudek_utils import *

class SingleDice(Scene):
    def construct(self):
        probability_distributions_txt = Text("Probability distributions", font_size=60)

        pmf_plot = PMFBarPlot(
            list(range(1,7)), [1/6]*6, 
            width=7, height=4, gap=0.1, max_y=3/8,
            x_label=Tex("$x$ (number on die)", font_size = 48)
        ).align_on_border(DOWN)

        dice = [GenericImageMobject(f"assets/die{i}.png") for i in range(1,7)]

        for i in range(6):
            dice[i].move_to(pmf_plot.x_num_labels[i])

        pmf_txt = Text("Probability mass function", font_size=48, slant=ITALIC).move_to((0,2.5,0))

        dice2 = [die.copy() for die in dice]
        prob_eq = Group(
            MathTex("P(", font_size=36), dice2[0], MathTex(r") = \frac{1}{6}", font_size=36)
        ).arrange(RIGHT, buff=0.1).move_to((0,1,0))

        #################################################################
        # Animation (1)                                                 #
        #################################################################
        # Testing
        # self.add(NumberPlane(), Dot(ORIGIN))
        # self.add(pmf_plot.axes, pmf_plot.x_label, pmf_plot.y_label, *dice, pmf_txt, prob_eq)
        # self.add(pmf_plot.bars)

        self.play(
            Write(probability_distributions_txt)
        )

        self.wait()

        self.play(
            Unwrite(probability_distributions_txt, reverse=False)
        )

        self.wait()

        self.play(
            Create(pmf_plot.axes),
            AnimationGroup(*[FadeIn(dice[i], shift=UP*0.1) for i in range(6)], lag_ratio=0.25),
            Write(pmf_plot.x_label),
            Write(pmf_plot.y_label),
        )

        self.add(*pmf_plot.bars)
        self.play(
            pmf_plot.create_bars(lag_ratio = 0.25)
        )

        self.wait()

        self.play(
            Circumscribe(Group(*dice), time_width=0.5)
        )

        self.wait()

        self.play(
            Circumscribe(pmf_plot.y_label, time_width=0.5)
        )

        self.wait()

        self.play(
            Circumscribe(pmf_plot.bars[0])
        )

        self.wait()

        self.play(
            Write(pmf_txt)
        )

        self.wait()

        self.play(
            Write(VGroup(prob_eq[0], prob_eq[2])),
            FadeIn(dice2[0], shift=DOWN*0.5)
        )

        self.wait()

        self.play(
            FadeOut(dice2[0], shift=DOWN*0.5),
            FadeIn(dice2[2].move_to(dice2[0]), shift=DOWN*0.5)
        )

        self.play(
            FadeOut(dice2[2], shift=DOWN*0.5),
            FadeIn(dice2[4].move_to(dice2[2]), shift=DOWN*0.5)
        )

        self.play(
            FadeOut(dice2[4], shift=DOWN*0.5),
            FadeIn(dice2[5].move_to(dice2[4]), shift=DOWN*0.5)
        )

        self.wait()

        self.play(
            pmf_plot.change_y_values([1/8]*5 + [3/8]),
            Transform(prob_eq[2], MathTex(r") = \frac{3}{8}", font_size=36).move_to(prob_eq[2]))
        )

        self.wait()

        self.play(
            FadeOut(*self.mobjects)
        )

        self.wait()

       