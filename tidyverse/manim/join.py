from manim import *
from data_frame import *

class join(Scene):
    def mobjects_near(self, point, radius):
        if isinstance(point, Mobject):
            point = point.get_center()

        mobjects_in_radius = []
        for m in self.mobjects:
            if np.linalg.norm(m.get_center() - point) <= radius:
                mobjects_in_radius.append(m)

        return mobjects_in_radius

    def construct(self):

        Text.set_default(font="sans-serif")

        TABLE_SCALE=0.37

        col_names = ["sample", "exp", "gene_id"]
        entries = [
            ["A", "7", "1"],
            ["A", "0.1", "2"],
            ["B", "2.4", "2"],
            ["B", "5", "4"],
        ]
        df = DataFrame(
            [[Text(t, weight=BOLD) for t in col_names]] +
            [[Text(t) for t in row] for row in entries],
            include_outer_lines=True,
        ).scale(TABLE_SCALE).align_on_border(UL, buff=1).shift(DOWN*0.7)

        col_names = ["gene_id", "name"]
        entries = [
            ["1", "SOX6"],
            ["2", "BRCA2"],
            ["3", "TP53"],
        ]
        gene_names = DataFrame(
            [[Text(t, weight=BOLD) for t in col_names]] +
            [[Text(t) for t in row] for row in entries],
            include_outer_lines=True,
        ).scale(TABLE_SCALE).align_on_border(UR, buff=1).shift(DOWN*0.7)

        df.set_z_index(1)
        gene_names.set_z_index(1)

        # Join tables
        col_names = ["sample", "exp", "gene_id", "name"]
        entries = [
            ["A", "7", "1", "SOX6"],
            ["A", "0.1", "2", "BRCA2"],
            ["B", "2.4", "2", "BRCA2"],
        ]
        df_inner = DataFrame(
            [[Text(t, weight=BOLD) for t in col_names]] +
            [[Text(t) for t in row] for row in entries],
            include_outer_lines=True,
        ).scale(TABLE_SCALE).next_to(df, DOWN, buff=0.5).set_x(0.55)

        entries = [
            ["A", "7", "1", "SOX6"],
            ["A", "0.1", "2", "BRCA2"],
            ["B", "2.4", "2", "BRCA2"],
            ["B", "5", "4", "NA"],
        ]
        df_left = DataFrame(
            [[Text(t, weight=BOLD) for t in col_names]] +
            [[Text(t) for t in row] for row in entries],
            include_outer_lines=True,
        ).scale(TABLE_SCALE).next_to(df, DOWN, buff=0.5).set_x(0.55)

        entries = [
            ["A", "7", "1", "SOX6"],
            ["A", "0.1", "2", "BRCA2"],
            ["B", "2.4", "2", "BRCA2"],
            ["NA", "NA", "3", "TP53"],
        ]
        df_right = DataFrame(
            [[Text(t, weight=BOLD) for t in col_names]] +
            [[Text(t) for t in row] for row in entries],
            include_outer_lines=True,
        ).scale(TABLE_SCALE).next_to(df, DOWN, buff=0.5).set_x(0.55)

        entries = [
            ["A", "7", "1", "SOX6"],
            ["A", "0.1", "2", "BRCA2"],
            ["B", "2.4", "2", "BRCA2"],
            ["B", "5", "4", "NA"],
            ["NA", "NA", "3", "TP53"],
        ]
        df_full = DataFrame(
            [[Text(t, weight=BOLD) for t in col_names]] +
            [[Text(t) for t in row] for row in entries],
            include_outer_lines=True,
        ).scale(TABLE_SCALE).next_to(df, DOWN, buff=0.5).set_x(0.55)

        # Text

        df_txt = Text("df", font_size=32).next_to(df, UP, buff=0.2)
        gene_names_txt = Text("gene_names", font_size=32).next_to(gene_names, UP, buff=0.2)
        df_inner_txt = Text("df_inner", font_size=32).next_to(df_inner, UP, buff=0.2)
        df_left_txt = Text("df_left", font_size=32).next_to(df_left, UP, buff=0.2)
        df_right_txt = Text("df_right", font_size=32).next_to(df_right, UP, buff=0.2)
        df_full_txt = Text("df_full", font_size=32).next_to(df_full, UP, buff=0.2)

        inner_join_txt = Text("inner_join", weight=BOLD, font_size=36).align_on_border(UP, buff=0.6)
        left_join_txt = Text("left_join", weight=BOLD, font_size=36).align_on_border(UP, buff=0.6)
        right_join_txt = Text("right_join", weight=BOLD, font_size=36).align_on_border(UP, buff=0.6)
        full_join_txt = Text("full_join", weight=BOLD, font_size=36).align_on_border(UP, buff=0.6)
    

        # bg rectangles

        for i in [1,2,3]:
            df.add_bg_rectangle((1,i), color="#808080")

        for i in [1,2]:
            gene_names.add_bg_rectangle((1,i), color="#808080")

        for i in [1,2,3,4]:
            df_inner.add_bg_rectangle((1,i), color="#808080")
            df_left.add_bg_rectangle((1,i), color="#808080")
            df_right.add_bg_rectangle((1,i), color="#808080")
            df_full.add_bg_rectangle((1,i), color="#808080")

        # NA color
        VGroup(
            df_left.get_entries((5,4)),
            df_right.get_entries((5,1)),
            df_right.get_entries((5,2)),
            df_full.get_entries((5,4)),
            df_full.get_entries((6,1)),
            df_full.get_entries((6,2)),
        ).set_color(RED)
        

        # Code
        code_inner_txt = Text(
            """
            df_inner <- df %>% \n
                inner_join(\n
                    gene_names,\n
                    by="gene_id"\n
                )
            """,
            font="Consolas",
            font_size=22,
            line_spacing=0
        ).align_on_border(DOWN, buff=0.7).align_to(df, UP)

        VGroup(
            code_inner_txt[8:10],
            code_inner_txt[12:15],
            code_inner_txt[25],
            code_inner_txt[39],
            code_inner_txt[-1],
        ).set_color(BLUE_B)

        

        by_rect = SurroundingRectangle(code_inner_txt[37:-1])

        code_left_txt = Text(
            """
            df_left <- df %>% \n
                left_join(\n
                    gene_names,\n
                    by="gene_id"\n
                )
            """,
            font="Consolas",
            font_size=22,
            line_spacing=0
        ).align_on_border(DOWN, buff=0.7).align_to(df, UP)

        VGroup(
            code_left_txt[7:9],
            code_left_txt[11:14],
            code_left_txt[23],
            code_left_txt[37],
            code_left_txt[-1],
        ).set_color(BLUE_B)

        code_right_txt = Text(
            """
            df_right <- df %>% \n
                right_join(\n
                    gene_names,\n
                    by="gene_id"\n
                )
            """,
            font="Consolas",
            font_size=22,
            line_spacing=0
        ).align_on_border(DOWN, buff=0.7).align_to(df, UP)

        VGroup(
            code_right_txt[8:10],
            code_right_txt[12:15],
            code_right_txt[25],
            code_right_txt[39],
            code_right_txt[-1],
        ).set_color(BLUE_B)

        code_full_txt = Text(
            """
            df_full <- df %>% \n
                full_join(\n
                    gene_names,\n
                    by="gene_id"\n
                )
            """,
            font="Consolas",
            font_size=22,
            line_spacing=0
        ).align_on_border(DOWN, buff=0.7).align_to(df, UP)

        VGroup(
            code_full_txt[7:9],
            code_full_txt[11:14],
            code_full_txt[23],
            code_full_txt[37],
            code_full_txt[-1],
        ).set_color(BLUE_B)


        # Arrows
        arrow_left = CurvedArrow(
            df.get_edge_center(DOWN) + DOWN*0.3, 
            df_right.get_edge_center(LEFT) + LEFT*0.7,
            angle=1.4
        )

        arrow_right = CurvedArrow(
            gene_names.get_edge_center(DOWN) + DOWN*0.4, 
            df_right.get_edge_center(RIGHT) + RIGHT*0.7,
            angle=-1.4,
        ).rotate(-0.15).shift(DOWN*0.1)

        #################################################################
        # Animation (inner)                                             #
        #################################################################

        # Testing
        # self.add(df, gene_names, df_txt, gene_names_txt, arrow_left, arrow_right)
        # self.add(inner_join_txt, code_inner_txt, df_inner, df_inner_txt)
        # self.add(full_join_txt, code_full_txt, df_full, df_full_txt)

        self.play(
            Write(inner_join_txt),
            run_time=0.5
        )

        self.play(
            Write(df_txt),
            Create(df.get_horizontal_lines()),
            Create(df.get_vertical_lines()),
            Write(df.get_entries()),
            *[FadeIn(df.bg_rectangles[(pos)].copy()) for pos in sorted(df.bg_rectangles.keys())],
            run_time=1
        )

        self.wait(1)

        self.play(
            Write(gene_names_txt),
            Create(gene_names.get_horizontal_lines()),
            Create(gene_names.get_vertical_lines()),
            Write(gene_names.get_entries()),
            *[FadeIn(gene_names.bg_rectangles[(pos)].copy()) for pos in sorted(gene_names.bg_rectangles.keys())],
            run_time=1
        )

        self.wait(1)

        self.play(
            AddTextLetterByLetter(code_inner_txt),
            run_time=2.5
        )

        self.wait(1)

        self.play(
            Create(arrow_left),
            Create(arrow_right),
            Write(df_inner_txt),
            run_time=0.5
        )

        self.play(
            Create(by_rect)
        )

        self.play(
            FadeIn(
                *[df.add_bg_rectangle((i,3), color="#4A2A57") for i in [2,3,4,5]],
                *[gene_names.add_bg_rectangle((i,1), color="#4A2A57") for i in [2,3,4]],
            )
        )

        self.play(
            Uncreate(by_rect)
        )

        self.wait()

        self.play(
            *[df.animate_cell_movement((1,i), df_inner, (1,i)) for i in [1,2,3]],
        )

        self.play(
            *[gene_names.animate_cell_movement((1,i), df_inner, (1,i+2)) for i in [1,2]]
        )

        self.wait()

        self.play(
            *[df.animate_cell_movement((2,i), df_inner, (2,i)) for i in [1,2,3]],
        )

        self.play(
            *[gene_names.animate_cell_movement((2,i), df_inner, (2,i+2)) for i in [1,2]]
        )

        self.play(
            *[df.animate_cell_movement((3,i), df_inner, (3,i)) for i in [1,2,3]],
        )

        self.play(
            *[gene_names.animate_cell_movement((3,i), df_inner, (3,i+2)) for i in [1,2]]
        )

        self.play(
            *[df.animate_cell_movement((4,i), df_inner, (4,i)) for i in [1,2,3]],
        )

        self.play(
            *[gene_names.animate_cell_movement((3,i), df_inner, (4,i+2)) for i in [1,2]]
        )

        self.wait(3)

        self.play(
            FadeOut(inner_join_txt, code_inner_txt, arrow_left, arrow_right, df_inner_txt, 
                    *[df.bg_rectangles[(i,3)] for i in [2,3,4,5]],
                    *[gene_names.bg_rectangles[(i,1)] for i in [2,3,4]],
                    *self.mobjects_near(df_inner, radius=2.5), shift=DOWN*0.1)
        )

        self.wait()

        #################################################################
        # Animation (left)                                              #
        #################################################################

        # self.add(df, gene_names, df_txt, gene_names_txt)

        self.play(
            Write(left_join_txt),
            run_time=0.5
        )

        self.wait(1)

        self.play(
            AddTextLetterByLetter(code_left_txt),
            run_time=1.5
        )

        self.wait(1)

        self.play(
            Create(arrow_left),
            Create(arrow_right),
            Write(df_left_txt),
            FadeIn(
                *[df.add_bg_rectangle((i,3), color="#4A2A57") for i in [2,3,4,5]],
                *[gene_names.add_bg_rectangle((i,1), color="#4A2A57") for i in [2,3,4]],
            ),
            run_time=0.5
        )

        self.play(
            *[df.animate_cell_movement((i,j), df_left, (i,j)) for i in [1,2,3,4,5] for j in [1,2,3]]
        )

        self.wait()

        self.play(
            *[gene_names.animate_cell_movement((i,j), df_left, (i,j+2)) for i in [1,2,3] for j in [1,2]],
            *[gene_names.animate_cell_movement((3,j), df_left, (4,j+2)) for j in [1,2]]
        )

        self.play(
            Create(df_left.get_cell((5,4), color=WHITE)),
            Write(df_left.get_entries((5,4)))
        )

        self.wait(3)

        self.play(
            FadeOut(left_join_txt, code_left_txt, arrow_left, arrow_right, df_left_txt, 
                    *[df.bg_rectangles[(i,3)] for i in [2,3,4,5]],
                    *[gene_names.bg_rectangles[(i,1)] for i in [2,3,4]],
                    *self.mobjects_near(df_left, radius=2.5), shift=DOWN*0.1)
        )

        #################################################################
        # Animation (right)                                             #
        #################################################################

        # self.add(df, gene_names, df_txt, gene_names_txt)

        self.play(
            Write(right_join_txt),
            run_time=0.5
        )

        self.wait(1)

        self.play(
            AddTextLetterByLetter(code_right_txt),
            run_time=1.5
        )

        self.wait(1)

        self.play(
            Create(arrow_left),
            Create(arrow_right),
            Write(df_right_txt),
            FadeIn(
                *[df.add_bg_rectangle((i,3), color="#4A2A57") for i in [2,3,4,5]],
                *[gene_names.add_bg_rectangle((i,1), color="#4A2A57") for i in [2,3,4]],
            ),
            run_time=0.5
        )

        self.wait(1)

        self.play(
            *[gene_names.animate_cell_movement((i,j), df_right, (i,j+2)) for i in [1,2,3] for j in [1,2]],
            *[gene_names.animate_cell_movement((3,j), df_right, (4,j+2)) for j in [1,2]],
            *[gene_names.animate_cell_movement((4,j), df_right, (5,j+2)) for j in [1,2]]
        )

        self.wait()

        self.play(
            *[df.animate_cell_movement((i,j), df_right, (i,j)) for i in [1,2,3,4] for j in [1,2,3]]
        )

        self.play(
            Create(df_right.get_cell((5,1), color=WHITE)),
            Write(df_right.get_entries((5,1))),
            Create(df_right.get_cell((5,2), color=WHITE)),
            Write(df_right.get_entries((5,2))),
        )

        self.wait(3)

        self.play(
            FadeOut(right_join_txt, code_right_txt, arrow_left, arrow_right, df_right_txt, 
                    *[df.bg_rectangles[(i,3)] for i in [2,3,4,5]],
                    *[gene_names.bg_rectangles[(i,1)] for i in [2,3,4]],
                    *self.mobjects_near(df_right, radius=2.5), shift=DOWN*0.1)
        )


        #################################################################
        # Animation (full)                                              #
        #################################################################

        self.add(df, gene_names, df_txt, gene_names_txt)

        self.play(
            Write(full_join_txt),
            run_time=0.5
        )

        self.wait(1)

        self.play(
            AddTextLetterByLetter(code_full_txt),
            run_time=1.5
        )

        self.wait(1)

        self.play(
            Create(arrow_left),
            Create(arrow_right),
            Write(df_full_txt),
            FadeIn(
                *[df.add_bg_rectangle((i,3), color="#4A2A57") for i in [2,3,4,5]],
                *[gene_names.add_bg_rectangle((i,1), color="#4A2A57") for i in [2,3,4]],
            ),
            run_time=0.5
        )

        self.wait(1)

        self.play(
            *[df.animate_cell_movement((i,j), df_full, (i,j)) for i in [1,2,3,4,5] for j in [1,2,3]],
            *[gene_names.animate_cell_movement((i,j), df_full, (i,j+2)) for i in [1,2,3] for j in [1,2]],
            *[gene_names.animate_cell_movement((3,j), df_full, (4,j+2)) for j in [1,2]],
            *[gene_names.animate_cell_movement((4,j), df_full, (6,j+2)) for j in [1,2]]
        )

        self.play(
            Create(df_full.get_cell((5,4), color=WHITE)),
            Write(df_full.get_entries((5,4))),
            Create(df_full.get_cell((6,1), color=WHITE)),
            Write(df_full.get_entries((6,1))),
            Create(df_full.get_cell((6,2), color=WHITE)),
            Write(df_full.get_entries((6,2))),
        )

        self.wait(3)

        self.play(
            FadeOut(*self.mobjects, shift=DOWN*0.1)
        )

        self.wait()
