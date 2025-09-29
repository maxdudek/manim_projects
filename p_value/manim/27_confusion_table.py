from manim import *
from probability_mobjects import *
from dudek_utils import *

def get_table_mobjects():
    table = MobjectTable(
        [
            [Paragraph("Type I Error\nFalse Positive\n(FP)", font_size=36, color=RED_D, alignment="center"), 
                Paragraph("Correct!\nTrue Positive\n(TP)", font_size=36, color=GREEN, alignment="center")],
            [Paragraph("Correct!\nTrue Negative\n(TN)", font_size=36, color=GREEN, alignment="center"), 
                Paragraph("Type II Error\nFalse Negative\n(FN)", font_size=36, color=RED_D, alignment="center")]
        ],
        h_buff = 1,
        v_buff = 0.8,
        include_outer_lines=True
    ).align_on_border(DR, buff=1)

    null_world = GenericImageMobject("assets/null_world.png").scale(0.5).next_to(table.get_cell((1,1)), UP, buff=0.3)
    alt_world = GenericImageMobject("assets/alt_world.png").scale(0.5).next_to(table.get_cell((1,2)), UP, buff=0.3)

    reject_txt = MarkupText("Reject H<sub>0</sub>\n(Significant)", font_size=40).next_to(table.get_cell((1,1)), LEFT, buff=0.3)

    fail_txt = MarkupText("Fail to reject H<sub>0</sub>\n(non-significant)", font_size=40).next_to(table.get_cell((2,1)), LEFT, buff=0.3)

    return table, null_world, alt_world, reject_txt, fail_txt

class _27_confusion_table(Scene):
    def construct(self):

        table, null_world, alt_world, reject_txt, fail_txt = get_table_mobjects()

        #################################################################
        # Animation (1)                                                 #
        #################################################################
        # self.add(NumberPlane(
        #     background_line_style={
        #         "stroke_width": 2,
        #         "stroke_opacity": 0.6
        #     }))
        
        # self.add(table, null_world, alt_world, reject_txt, fail_txt)
        self.play(
            Write(reject_txt),
            run_time=1
        )

        self.wait()

        self.play(
            Write(fail_txt),
            run_time=1
        )

        self.wait()

        self.play(
            FadeIn(null_world)
        )

        self.play(
            FadeIn(alt_world)
        )

        self.wait()

        self.play(
            Create(table.get_vertical_lines()),
            Create(table.get_horizontal_lines())
        )

        self.play(
            Write(table.get_entries((2,1))),
            Write(table.get_entries((1,2))),
            run_time=1
        )

        self.wait()

        self.play(
            Circumscribe(null_world)
        )

        self.wait()

        self.play(
            Circumscribe(reject_txt)
        )

        self.wait()

        self.play(
            Write(table.get_entries((1,1))),
        )

        self.wait()

        self.play(
            Circumscribe(alt_world)
        )

        self.wait()

        self.play(
            Circumscribe(fail_txt)
        )

        self.wait()

        self.play(
            Write(table.get_entries((2,2))),
        )

        self.wait()

        self.play(
            Group(table, null_world, alt_world, reject_txt, fail_txt).animate.scale(0.5).align_on_border(UR)
        )

        self.wait()

        # Export
        self.table = table
        self.null_world = null_world
        self.alt_world = alt_world
        self.reject_txt = reject_txt
        self.fail_txt = fail_txt

        # self.play(
        #     FadeOut(*self.mobjects, shift=DOWN*0.2)
        # )

        # self.wait(0.1)





