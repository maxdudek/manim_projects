from manim import *
from data_frame import *
import numpy as np

class summarize(Scene):
    def mobjects_near(self, point, radius):
        mobjects_in_radius = []
        for m in self.mobjects:
            if np.linalg.norm(m.get_center() - point) <= radius:
                mobjects_in_radius.append(m)

        return mobjects_in_radius

    def construct(self):
        
        Text.set_default(font="sans-serif")

        col_names = ["name", "major", "grade", "abscence"]
        entries = [
            ["Alice", "Bio", "87", "3"],
            ["Bob", "Bio", "92", "1"],
            ["Chloe", "Math", "75", "5"],
            ["Dave", "Eng", "71", "6"],
            ["Emma", "Eng", "98", "2"],
            ["Zoey", "Eng", "83", "4"],
        ]
        df_students = DataFrame(
            [[Text(t, weight=BOLD) for t in col_names]] +
            [[Text(t) for t in row] for row in entries],
            include_outer_lines=True,
        ).scale(0.38).align_on_border(UL, buff=1).shift(DOWN*1)

        df_students.set_z_index(1)

        col_names = ["average_grade", "total_abs"]
        entries = [
            ["84.5", "21"]
        ]
        df_summary = DataFrame(
            [[Text(t, weight=BOLD) for t in col_names]] +
            [[Text(t) for t in row] for row in entries],
            include_outer_lines=True,
        ).scale(0.38).align_on_border(UR, buff=1).shift(DOWN*1)

        

        col_names = ["major", "avg_grade", "ttl_abs", "n_stud"]
        entries = [
            ["Bio", "89.5", "4", "2"],
            ["Math", "75", "5", "1"],
            ["Eng", "84.3", "12", "3"],
        ]
        df_sum_by_major = DataFrame(
            [[Text(t, weight=BOLD) for t in col_names]] +
            [[Text(t) for t in row] for row in entries],
            include_outer_lines=True,
        ).scale(0.38).align_on_border(UR, buff=1).shift(DOWN*1)

        # Text
        df_students_txt = Text("df_students", font_size=32).next_to(df_students, UP, buff=0.2)
        df_summary_txt = Text("df_summary", font_size=32).next_to(df_summary, UP, buff=0.2)
        df_sum_by_major_txt = Text("df_sum_by_major", font_size=32).next_to(df_sum_by_major, UP, buff=0.2)

        summarize_txt = Text("summarize", weight=BOLD, font_size=36).align_on_border(UP, buff=0.6)
        group_summarize_txt = Text("group_by + summarize", weight=BOLD, font_size=36).align_on_border(UP, buff=0.6)

        # Arrows
        arrow_sum = Arrow(
            df_students.get_cell((1,4)).get_corner(DR),
            df_summary.get_cell((1,1)).get_corner(DL),
        )

        arrow_group = Arrow(
            df_students.get_cell((3,4)).get_edge_center(RIGHT),
            df_sum_by_major.get_cell((3,1)).get_edge_center(LEFT),
            max_tip_length_to_length_ratio=0.3,
            buff=0.2
        )

        # bg rect colors
        for i in range(1,5):
            df_students.add_bg_rectangle((1,i), color="#808080")

        for i in range(1,3):
            df_summary.add_bg_rectangle((1,i), color="#808080")

        for i in range(1,5):
            df_sum_by_major.add_bg_rectangle((1,i), color="#808080")

        # for i in range(2,8):
        #     df_students.add_bg_rectangle((i,3), color=BLACK)
        #     df_students.add_bg_rectangle((i,4), color=BLACK)
        
        # for i in range(2,5):
        #     df_sum_by_major.add_bg_rectangle((i,2), color=BLACK)
        #     df_sum_by_major.add_bg_rectangle((i,3), color=BLACK)
        #     df_sum_by_major.add_bg_rectangle((i,4), color=BLACK)

        df_sum_by_major.add_bg_rectangle((2,1), color="#3D7225")
        df_sum_by_major.add_bg_rectangle((3,1), color=RED_E)
        df_sum_by_major.add_bg_rectangle((4,1), color=BLUE_E)


        # Code
        code_sum_txt = Text(
            """
            df_summary <- df_students %>% \n
                summarize(\n
                    average_grade=mean(grade),\n
                    total_abs=sum(abscence)\n
                )
            """,
            font="Consolas",
            font_size=22,
            line_spacing=0.1
        ).align_on_border(DOWN, buff=0.7).align_to(df_summary, RIGHT)

        VGroup(
            code_sum_txt[10:12],
            code_sum_txt[23:26],
            code_sum_txt[35],
            code_sum_txt[49],
            code_sum_txt[54],
            code_sum_txt[60],
            code_sum_txt[71],
            code_sum_txt[75],
            code_sum_txt[-2],
            code_sum_txt[-1],
        ).set_color(BLUE_B)

        average_grade_txt = code_sum_txt[36:49]
        total_abs_txt = code_sum_txt[62:71]

        average_grade_rect = SurroundingRectangle(code_sum_txt[36:61])
        total_abs_rect = SurroundingRectangle(code_sum_txt[62:-1])


        code_group_txt = Text(
            """
            df_sum_by_major <- df_students %>% \n
                group_by(major) %>% \n
                summarize(\n
                    avg_grade=mean(grade),\n
                    ttl_abs=sum(abscence),\n
                    n_stud=n()\n
                )
            """,
            font="Consolas",
            font_size=22,
            line_spacing=0
        ).align_on_border(DOWN, buff=0.3).align_to(df_sum_by_major, LEFT)

        VGroup(
            code_group_txt[15:17],
            code_group_txt[28:31],
            code_group_txt[39],
            code_group_txt[45:49],
            code_group_txt[58],
            code_group_txt[68],
            code_group_txt[73],
            code_group_txt[79],
            code_group_txt[88],
            code_group_txt[92],
            code_group_txt[101],
            code_group_txt[-5],
            code_group_txt[-3:],
        ).set_color(BLUE_B)

        avg_grade_txt = code_group_txt[59:68]
        ttl_abs_txt = code_group_txt[81:88]
        n_stud_txt = code_group_txt[103:109]
        
        group_by_rect = SurroundingRectangle(code_group_txt[31:46])
        avg_grade_rect = SurroundingRectangle(code_group_txt[59:80])
        ttl_abs_rect = SurroundingRectangle(code_group_txt[81:102])
        n_stud_rect = SurroundingRectangle(code_group_txt[103:-1])
        

        #################################################################
        # Animation                                                     #
        #################################################################

        # self.add(df_students, code_group_txt)

        # self.add(df_students, df_summary, df_students_txt, df_summary_txt, 
        #          arrow_sum, code_sum_txt, summarize_txt, average_grade_rect, total_abs_rect)

        # self.add(df_students, df_sum_by_major, df_students_txt, df_sum_by_major_txt,
        #          group_summarize_txt, arrow_group, code_group_txt)


        self.play(
            Write(summarize_txt),
            run_time=0.5
        )

        self.play(
            Write(df_students_txt),
            Create(df_students.get_horizontal_lines()),
            Create(df_students.get_vertical_lines()),
            Write(df_students.get_entries()),
            *[FadeIn(df_students.bg_rectangles[(pos)].copy()) for pos in sorted(df_students.bg_rectangles.keys())],
            run_time=1
        )

        self.wait(2)

        self.play(
            AddTextLetterByLetter(code_sum_txt),
            run_time=2.5
        )

        self.wait(1)

        self.play(
            Create(arrow_sum),
            Write(df_summary_txt),
            run_time=0.5
        )

        self.wait(0.5)
        
        self.play(
            Create(average_grade_rect)
        )

        self.wait(0.5)

        self.play(
            Transform(average_grade_txt.copy(), df_summary.get_entries((1,1))),
            FadeIn(df_summary.bg_rectangles[(1,1)], target_position=average_grade_txt),
            FadeIn(df_summary.get_cell((1,1), color=WHITE), target_position=average_grade_txt)
        )

        self.play(
            *[df_students.animate_cell_movement((i,3), df_summary, (2,1), transform_entry=True) for i in range(2,8)],
            run_time=1.5
        )

        self.play(
            Uncreate(average_grade_rect)
        )

        self.play(
            Create(total_abs_rect)
        )

        self.wait(0.5)

        self.play(
            Transform(total_abs_txt.copy(), df_summary.get_entries((1,2))),
            FadeIn(df_summary.bg_rectangles[(1,2)], target_position=total_abs_txt),
            FadeIn(df_summary.get_cell((1,2), color=WHITE), target_position=total_abs_txt)
        )

        self.play(
            *[df_students.animate_cell_movement((i,4), df_summary, (2,2), transform_entry=True) for i in range(2,8)],
            run_time=1.5
        )

        self.play(
            Uncreate(total_abs_rect)
        )

        self.wait(3)

        self.play(
            FadeOut(summarize_txt, arrow_sum, df_summary_txt, *self.mobjects_near(df_summary.get_center(), radius=2), code_sum_txt, shift=DOWN*0.1)
        )

        self.wait()

        #################################################################
        # Animation (group_by)                                          #
        #################################################################

        self.play(
            Write(group_summarize_txt),
            run_time=0.5
        )

        self.play(
            AddTextLetterByLetter(code_group_txt),
            run_time=2.5
        )

        self.play(
            Create(arrow_group),
            Write(df_sum_by_major_txt),
            run_time=0.5
        )

        self.wait(0.5)

        self.play(
            Create(group_by_rect)
        )

        self.wait(0.5)

        self.play(
            FadeIn(
                *[df_students.add_bg_rectangle((i,2), color="#3D7225") for i in [2,3]],
                df_students.add_bg_rectangle((4,2), color=RED_E),
                *[df_students.add_bg_rectangle((i,2), color=BLUE_E) for i in [5,6,7]],
            )
        )

        self.wait(0.5)

        self.play(
            df_students.animate_cell_movement((1,2), df_sum_by_major, (1,1)),
            *[df_students.animate_cell_movement((i,2), df_sum_by_major, (2,1)) for i in [2,3]],
            df_students.animate_cell_movement((4,2), df_sum_by_major, (3,1)),
            *[df_students.animate_cell_movement((i,2), df_sum_by_major, (4,1)) for i in [5,6,7]],
            run_time=1.5
        )

        self.play(
            Uncreate(group_by_rect)
        )

        self.play(
            Create(avg_grade_rect)
        )

        self.wait(0.5)

        self.play(
            Transform(avg_grade_txt.copy(), df_sum_by_major.get_entries((1,2))),
            FadeIn(df_sum_by_major.bg_rectangles[(1,2)], target_position=avg_grade_txt),
            FadeIn(df_sum_by_major.get_cell((1,2), color=WHITE), target_position=avg_grade_txt)
        )

        self.play(
            *[df_students.animate_cell_movement((i,3), df_sum_by_major, (2,2), transform_entry=True) for i in [2,3]],
            run_time=1.5
        )

        self.play(
            *[df_students.animate_cell_movement((i,3), df_sum_by_major, (3,2), transform_entry=True) for i in [4]],
            run_time=1.5
        )

        self.play(
            *[df_students.animate_cell_movement((i,3), df_sum_by_major, (4,2), transform_entry=True) for i in [5,6,7]],
            run_time=1.5
        )

        self.play(
            Uncreate(avg_grade_rect)
        )

        self.play(
            Create(ttl_abs_rect)
        )

        self.wait(0.5)

        self.play(
            Transform(ttl_abs_txt.copy(), df_sum_by_major.get_entries((1,3))),
            FadeIn(df_sum_by_major.bg_rectangles[(1,3)], target_position=ttl_abs_txt),
            FadeIn(df_sum_by_major.get_cell((1,3), color=WHITE), target_position=ttl_abs_txt)
        )

        self.play(
            *[df_students.animate_cell_movement((i,4), df_sum_by_major, (2,3), transform_entry=True) for i in [2,3]],
            run_time=1.5
        )

        self.play(
            *[df_students.animate_cell_movement((i,4), df_sum_by_major, (3,3), transform_entry=True) for i in [4]],
            run_time=1.5
        )

        self.play(
            *[df_students.animate_cell_movement((i,4), df_sum_by_major, (4,3), transform_entry=True) for i in [5,6,7]],
            run_time=1.5
        )

        self.play(
            Uncreate(ttl_abs_rect)
        )

        self.play(
            Create(n_stud_rect)
        )

        self.wait(0.5)

        self.play(
            Transform(n_stud_txt.copy(), df_sum_by_major.get_entries((1,4))),
            FadeIn(df_sum_by_major.bg_rectangles[(1,4)], target_position=n_stud_txt),
            FadeIn(df_sum_by_major.get_cell((1,4), color=WHITE), target_position=n_stud_txt)
        )

        self.play(
            *[df_students.animate_cell_movement((i,2), df_sum_by_major, (2,4), transform_entry=True, fade_bg=True) for i in [2,3]],
            run_time=1.5
        )

        self.play(
            *[df_students.animate_cell_movement((i,2), df_sum_by_major, (3,4), transform_entry=True, fade_bg=True) for i in [4]],
            run_time=1.5
        )

        self.play(
            *[df_students.animate_cell_movement((i,2), df_sum_by_major, (4,4), transform_entry=True, fade_bg=True) for i in [5,6,7]],
            run_time=1.5
        )

        self.play(
            Uncreate(n_stud_rect)
        )

        self.wait(3)

        self.play(
            FadeOut(*self.mobjects, shift=DOWN*0.1)
        )
