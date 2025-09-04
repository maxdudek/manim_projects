from manim import *
from data_frame import *

class pivot_wider(Scene):
    def construct(self):

        Text.set_default(font="sans-serif")

        col_names = ["country", "year", "cases"]
        entries = [
            ["A", "1999", "0.7K"],
            ["A", "2000", "2K"],
            ["B", "1999", "37K"],
            ["B", "2000", "80K"],
            ["C", "1999", "212K"],
            ["C", "2000", "213K"],
        ]
        df1 = DataFrame(
            [[Text(t, weight=BOLD) for t in col_names]] +
            [[Text(t) for t in row] for row in entries],
            include_outer_lines=True,
        ).scale(0.5).align_on_border(UL, buff=1).shift(DOWN*0.7)

        col_names = ["country", "1999", "2000"]
        entries = [
            ["A", "0.7K", "2K"],
            ["B", "37K", "80K"],
            ["C", "212K", "213K"],
        ]
        df2 = DataFrame(
            [[Text(t, weight=BOLD) for t in col_names]] +
            [[Text(t) for t in row] for row in entries],
            include_outer_lines=True,
        ).scale(0.5).align_on_border(UR, buff=1).shift(DOWN*0.7)

        df1_txt = Text("df1", font_size=32).next_to(df1, UP, buff=0.3)
        df2_txt = Text("df2", font_size=32).next_to(df2, UP, buff=0.3)
        pivot_wider_txt = Text("pivot_wider", weight=BOLD, font_size=36).align_on_border(UP, buff=0.6)

        arrow = Arrow(
            df1.get_cell((3,3)).get_edge_center(RIGHT),
            df2.get_cell((3,1)).get_edge_center(LEFT),
        )

        df1.get_vertical_lines().set_z_index(1)
        df1.get_horizontal_lines().set_z_index(1)

        for i in range(1,4):
            df1.add_bg_rectangle((1,i), color="#808080")
        
        for i in range(2,8):
            df1.add_bg_rectangle((i,1), color=BLACK)
            df1.add_bg_rectangle((i,2), color="#6CCB40" if i%2==0 else "#3D7225")
            df1.add_bg_rectangle((i,3), color="#939000" if i%2==0 else "#934500")
            

        code_txt = Text(
            """
            df2 <- df1 %>% \n
                pivot_wider(\n
                    names_from="year",\n
                    values_from="cases"\n
                )
            """,
            font="Consolas",
            font_size=22,
            line_spacing=0.1
        ).align_on_border(DOWN, buff=0.7).align_to(df2, LEFT)

        VGroup(
            code_txt[3:5],
            code_txt[8:11],
            code_txt[22],
            code_txt[33],
            code_txt[52],
            code_txt[-1],
        ).set_color(BLUE_B)

        names_rect = SurroundingRectangle(code_txt[23:40])
        values_rect = SurroundingRectangle(code_txt[41:-1])


        #################################################################
        # Animation                                                     #
        #################################################################
        # self.add(df1, df1_txt, df2_txt, code_txt, pivot_wider_txt, arrow, names_rect, values_rect)

        # self.add(
        #     df2
        # )

        self.play(
            Write(pivot_wider_txt),
            run_time=0.5
        )

        self.play(
            Write(df1_txt),
            Create(df1.get_horizontal_lines()),
            Create(df1.get_vertical_lines()),
            Write(df1.get_entries()),
            *[FadeIn(df1.bg_rectangles[(1,i)].copy()) for i in [1,2,3]],
            Succession(*[FadeIn(df1.bg_rectangles[(pos)].copy()) for pos in sorted(df1.bg_rectangles.keys())[3:]], lag_ratio=1),
            run_time=0.5
        )

        self.wait(1)

        self.play(
            AddTextLetterByLetter(code_txt),
            run_time=2.5
        )

        self.wait()

        self.play(
            Create(arrow),
            Write(df2_txt),
            run_time=0.5
        )

        self.wait(0.5)

        self.play(
            df1.animate_cell_movement((1,1), df2, (1,1))
        )

        self.play(
            Create(names_rect)
        )

        self.wait(0.5)

        self.play(
            *[df1.animate_cell_movement((2*i,2), df2, (1,2)) for i in range(1,4)]
        )

        self.play(
            *[df1.animate_cell_movement((2*i+1,2), df2, (1,3)) for i in range(1,4)]
        )

        self.play(
            Uncreate(names_rect)
        )

        self.play(
            Create(values_rect)
        )

        self.wait(0.5)

        for i in range(1,4):
            self.play(
                df1.animate_cell_movement((2*i,1), df2, (i+1,1)),
                df1.animate_cell_movement((2*i+1,1), df2, (i+1,1)),
                df1.animate_cell_movement((2*i,3), df2, (i+1,2)),
                df1.animate_cell_movement((2*i+1,3), df2, (i+1,3)),
                run_time=1
            )

        self.play(
            Uncreate(values_rect)
        )

        self.wait(3)

        self.play(
            FadeOut(*self.mobjects, shift=DOWN*0.1)
        )

