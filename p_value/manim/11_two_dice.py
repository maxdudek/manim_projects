from manim import *
from probability_mobjects import *
from dudek_utils import *

class TwoDice(Scene):
    def construct(self):

        entries = [
            [2,3,4, 5, 6, 7],
            [3,4,5, 6, 7, 8],
            [4,5,6, 7, 8, 9],
            [5,6,7, 8, 9,10],
            [6,7,8, 9,10,11],
            [7,8,9,10,11,12],
        ]

        table = IntegerTable(
            entries, 
            # [[0]*6]*6,
            include_outer_lines = True,
            h_buff = 0.9,
            v_buff = 0.8,
        ).scale(0.8).shift(DOWN*0.3)

        # Add numbers and colors
        colors = color_gradient((BLUE_A, BLUE_E), length_of_output=11)
        bg_rectangle_groups = {k: VGroup() for k in range(2,13)}
        entry_groups = {k: VGroup() for k in range(2,13)}
        bg_and_entry_groups = {k: VGroup() for k in range(2,13)}
        for i in range(1,7):
            for j in range(1,7):
                bg_rectangle = table.get_highlighted_cell((i,j), color=colors[i+j-2])
                table.add_to_back(bg_rectangle)
                bg_and_entry_groups[i+j].add(bg_rectangle)
                bg_rectangle_groups[i+j].add(bg_rectangle)
                entry = table.get_entries(pos=(i,j))
                entry.become(Integer(entries[i-1][j-1]).move_to(table.get_cell((i,j))))
                bg_and_entry_groups[i+j].add(entry)
                entry_groups[i+j].add(entry)

        table.get_vertical_lines().set_z_index(1)
        table.get_horizontal_lines().set_z_index(1)
        table.get_entries().set_z_index(1)
                

        # Add column and row labels
        row_dice = Group()
        col_dice = Group()
        for i in range(1,7):
            row_dice.add(GenericImageMobject(f"assets/die{i}.png").next_to(table.get_cell((1,i)), UP))
            col_dice.add(GenericImageMobject(f"assets/die{i}.png").next_to(table.get_cell((i,1)), LEFT))

        p_6_txt = MathTex(r"P(\text{sum}=6)=\frac{5}{36}", font_size=38).next_to(table.get_cell((2,6)), RIGHT)
        p_2_txt = MathTex(r"P(\text{sum}=2)=\frac{1}{36}", font_size=38).next_to(table.get_cell((4,6)), RIGHT)


        pmf_plot = PMFBarPlot(
            list(range(2,13)),
            [i/36 for i in [1,2,3,4,5,6,5,4,3,2,1]],
            width=7, height=4, gap=0.1,
            x_label=Tex("$x$ (sum of two dice)", font_size = 48)
        )

        # for i in range(len(colors)):
        #     pmf_plot.bars[i].set_color(colors[i])

        
        prob_eq = MathTex(
            r"""
            P(X \geq 9) &= P(X=9) + P(X=10) + \\
                        &~~~~ P(X=11) + P(X=12) + \\
                        &= \frac{4}{36} + \frac{3}{36} + \frac{2}{36} + \frac{1}{36} \\
                        &= \frac{10}{36} \approx 28\%
            """,
            color = BLUE,
            font_size = 36
        ).move_to((3.5,0,0))

        rectangles6 = [SurroundingRectangle(entry) for entry in entry_groups[6]]
        rectangle2 = SurroundingRectangle(table.get_entries((1,1)))


        #################################################################
        # Animation (1)                                                 #
        #################################################################
        # Testing
        # self.add(NumberPlane(), Dot(ORIGIN))
        # self.add(table, row_dice, col_dice, p_6_txt, p_2_txt)
        # self.add(pmf_plot, prob_eq)
        # self.remove(pmf_plot.x_prime_line)

        self.play(
            Create(table.get_vertical_lines()),
            Create(table.get_horizontal_lines()),
            AnimationGroup(
                [
                    AnimationGroup(FadeIn(row_dice[i], shift=DOWN*0.1), 
                                FadeIn(col_dice[i], shift=RIGHT*0.1))
                    for i in range(6)
                ],
                lag_ratio = 0.1
            )
        )

        self.wait()

        self.play(
            Succession(
                [
                    Write(entry_groups[k])
                    for k in range(2,13)
                ]
            ),
            Succession(
                [
                    FadeIn(bg_rectangle_groups[k])
                    for k in range(2,13)
                ]
            ),
            run_time=3
        )

        self.wait()

        self.play(
            *[Create(rect) for rect in rectangles6]
        )

        self.wait()

        self.play(
            Write(p_6_txt)
        )

        self.play(
            *[Uncreate(rect) for rect in rectangles6]
        )

        self.wait()

        self.play(
            Create(rectangle2)
        )

        self.wait()

        self.play(
            Write(p_2_txt)
        )

        self.play(
            Uncreate(rectangle2)
        )

        self.wait()


        self.play(
            AnimationGroup(
                FadeOut(p_6_txt, p_2_txt, shift=DOWN*0.1),
                FadeOut(row_dice, col_dice),
                table.animate.scale(0.6).shift(UP*2).rotate(45*DEGREES),
                AnimationGroup(
                    Create(pmf_plot.axes),
                    Write(pmf_plot.x_num_labels),
                    Write(pmf_plot.x_label),
                    Write(pmf_plot.y_label)
                ),
                lag_ratio=0.25
            )
        )

        self.play(
            FadeOut(table.get_horizontal_lines()),
            FadeOut(table.get_vertical_lines()),
            run_time=0.1
        )

        self.play(
            AnimationGroup([
                ReplacementTransform(bg_and_entry_groups[i], pmf_plot.bars[i-2])
                for i in range(2,13)
            ]),
            run_time = 2
        )

        self.wait()

        self.play(
            Circumscribe(pmf_plot.x2bar(6), time_width=0.5)
        )

        self.wait()

        # Restore colors
        self.play(
            AnimationGroup([
                pmf_plot.bars[i].animate.set_color(pmf_plot.color1 if i >= 7 else pmf_plot.color2)
                for i in range(len(pmf_plot.bars))
            ])
        )

        pmf_plot.x_prime.set_value(9)
        pmf_plot.resume_updating()

        self.play(
            Create(pmf_plot.x_prime_line.reverse_points()),
            Write(pmf_plot.x_prime_label)
        )

        self.play(
            pmf_plot.animate.shift(LEFT*1.5)
        )

        self.play(
            Write(prob_eq)
        )

        self.wait()

        self.play(
            FadeOut(*self.mobjects, shift=DOWN*0.1)
        )

        self.wait()
