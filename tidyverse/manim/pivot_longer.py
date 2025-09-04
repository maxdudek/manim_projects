from manim import *
from data_frame import *
# import sys
# sys.setrecursionlimit(200)

class pivot_longer(Scene):
    def construct(self):

        Text.set_default(font="sans-serif")

        col_names = ["country", "1999", "2000"]
        entries = [
            ["A", "0.7K", "2K"],
            ["B", "37K", "80K"],
            ["C", "212K", "213K"],
        ]
        df1 = DataFrame(
            [[Text(t, weight=BOLD) for t in col_names]] +
            [[Text(t) for t in row] for row in entries],
            include_outer_lines=True,
        ).scale(0.5).align_on_border(UL, buff=1).shift(DOWN*0.7)

        col_names = ["country", "year", "cases"]
        entries = [
            ["A", "1999", "0.7K"],
            ["A", "2000", "2K"],
            ["B", "1999", "37K"],
            ["B", "2000", "80K"],
            ["C", "1999", "212K"],
            ["C", "2000", "213K"],
        ]
        df2 = DataFrame(
            [[Text(t, weight=BOLD) for t in col_names]] +
            [[Text(t) for t in row] for row in entries],
            include_outer_lines=True,
        ).scale(0.5).align_on_border(UR, buff=1).shift(DOWN*0.7)

        df1_txt = Text("df1", font_size=32).next_to(df1, UP, buff=0.3)
        df2_txt = Text("df2", font_size=32).next_to(df2, UP, buff=0.3)
        pivot_longer_txt = Text("pivot_longer", weight=BOLD, font_size=36).align_on_border(UP, buff=0.6)

        arrow = Arrow(
            df1.get_cell((3,3)).get_edge_center(RIGHT),
            df2.get_cell((3,1)).get_edge_center(LEFT),
        )

        df2.get_vertical_lines().set_z_index(1)
        df2.get_horizontal_lines().set_z_index(1)

        df1.add_bg_rectangle((1,1), color="#808080")
        df1.add_bg_rectangle((1,2), color="#6CCB40")
        df1.add_bg_rectangle((1,3), color="#3D7225")

        for i in range(1,4):
            df2.add_bg_rectangle((1,i), color="#808080")
        
        for i in range(2,5):
            df1.add_bg_rectangle((i,1), color=BLACK)
            df1.add_bg_rectangle((i,2), color="#939000")
            df1.add_bg_rectangle((i,3), color="#934500")

        for i in [2,4,6]:
            df2.add_bg_rectangle((i,2), color="#6CCB40")
            df2.add_bg_rectangle((i,3), color="#939000")

        for i in [3,5,7]:
            df2.add_bg_rectangle((i,2), color="#3D7225")
            df2.add_bg_rectangle((i,3), color="#934500")


        code_txt = Text(
            """
            df2 <- df1 %>% \n
                pivot_longer(\n
                    cols=c("1999", "2000"),\n
                    names_to="year", values_to="cases"\n
                )
            """,
            font="Consolas",
            font_size=22,
            line_spacing=0.1
        ).align_on_border(DOWN, buff=0.7).align_to(df1, LEFT)

        code_txt[31:37].set_color("#83D060")
        code_txt[38:44].set_color("#61904B")

        VGroup(
            code_txt[3:5],
            code_txt[8:11],
            code_txt[23],
            code_txt[28],
            code_txt[30],
            code_txt[44],
            code_txt[54],
            code_txt[71],
            code_txt[-1],
        ).set_color(BLUE_B)

        year_txt = code_txt[56:60]
        cases_txt = code_txt[73:78]

        year_rect = SurroundingRectangle(year_txt, color=WHITE)
        cases_rect = SurroundingRectangle(cases_txt, color=WHITE)

        year_bg_rect = year_rect.copy().set_fill("#808080").set_z_index(-1)
        cases_bg_rect = cases_rect.copy().set_fill("#808080").set_z_index(-1)
        
        # cursor = Rectangle(
        #     color = GREY_A,
        #     fill_color = GREY_A,
        #     fill_opacity = 1.0,
        #     height = 0.4,
        #     width = 0.15,
        # ).move_to(code_txt[0])

        print(sorted(df1.bg_rectangles.keys()))

        #################################################################
        # Animation                                                     #
        #################################################################
        # self.add(df1, df1_txt, df2_txt, code_txt, pivot_longer_txt, arrow)
        # self.add(df2)

        self.add(
            *[df2.get_entries((1,i)) for i in range(1,4)],
            *[df2.get_cell((1,i), color = WHITE) for i in range(1,4)],
            *[df2.bg_rectangles[(1,i)] for i in range(1,4)]
        )

        self.play(
            Write(pivot_longer_txt),
            run_time=0.5
        )

        self.play(
            Write(df1_txt),
            Create(df1.get_horizontal_lines()),
            Create(df1.get_vertical_lines()),
            Write(df1.get_entries()),
            FadeIn(df1.bg_rectangles[(1,1)]),
            Succession(*[FadeIn(df1.bg_rectangles[(pos)]) for pos in sorted(df1.bg_rectangles.keys())[1:]]),
            run_time=0.5
        )

        self.wait(2)

        self.play(
            AddTextLetterByLetter(code_txt),
            run_time=2.5
        )

        self.wait(2)

        self.play(
            Create(arrow),
            Write(df2_txt),
            run_time=0.5
        )

        self.play(
            Create(year_rect),
            Create(cases_rect),
            FadeIn(year_bg_rect, cases_bg_rect)
        )

        self.wait(0.5)

        self.play(
            df1.animate_cell_movement((1,1), df2, (1,1)),
            Transform(year_txt.copy(), df2.get_entries((1,2))),
            Transform(cases_txt.copy(), df2.get_entries((1,3))),
            Transform(year_rect, df2.get_cell((1,2), color=WHITE).flip()),
            Transform(cases_rect, df2.get_cell((1,3), color=WHITE).flip()),
            Transform(year_bg_rect, df2.bg_rectangles[(1,2)]),
            Transform(cases_bg_rect, df2.bg_rectangles[(1,3)]),
            run_time=2
        )

        self.wait(1)

        for r in range(1,4):
            self.play(
                df1.animate_cell_movement((r+1,1), df2, (2*r,1)),
                df1.animate_cell_movement((1,2), df2, (2*r,2)),
                df1.animate_cell_movement((r+1,2), df2, (2*r,3)),
                run_time=1.5,
            )
            self.play(
                df1.animate_cell_movement((r+1,1), df2, (2*r+1,1)),
                df1.animate_cell_movement((1,3), df2, (2*r+1,2)),
                df1.animate_cell_movement((r+1,3), df2, (2*r+1,3)),
                run_time=1.5
            )
            self.wait(0.5)

        self.wait(3)

        self.play(
            FadeOut(*self.mobjects, shift=DOWN*0.1)
        )

