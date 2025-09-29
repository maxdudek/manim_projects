from manim import *
from probability_mobjects import *
from dudek_utils import *

def get_footnote(number, redraw=True):
    footnote_border = Circle(radius=0.5, stroke_width=4, color=WHITE).align_on_border(UL, buff=0.5).shift(RIGHT*0.2)
    footnote_center = footnote_border.get_center()
    footnote_txt = MathTex(str(number)).move_to(footnote_border)
    footnote_angle = ValueTracker(0)

    if redraw:
        footnote_sector = always_redraw(lambda: Sector(
                radius = 0.5,
                angle=footnote_angle.get_value(),
                start_angle=0,
                arc_center=footnote_center,
                fill_color=PURPLE
        ))
    else:
        footnote_sector = Circle(0.5, color=PURPLE, fill_opacity=1).move_to(footnote_center)

    return footnote_sector, footnote_angle, footnote_border, footnote_txt

class _34_footnote_two_sided(Scene):
    def construct(self):

        footnote_sector, footnote_angle, footnote_border, footnote_txt = get_footnote(1)

        # dividing_line = Line(
        #     start=self.camera.frame_center + UP*self.camera.frame_height/2, 
        #     end = self.camera.frame_center + DOWN*self.camera.frame_height/2
        # )

        # null_hypothesis_txt = Tex(
        #     r"null hypothesis ($H_0$)"
        # ).move_to(self.camera.frame_center + LEFT*self.camera.frame_width/4).align_on_border(UP)

        # null_spinner = Spinner(0.5).next_to(null_hypothesis_txt, DOWN).scale(1.7).set_x(null_hypothesis_txt.get_x()).set_y(1)
        # null_spinner.add_image(GenericImageMobject("assets/rod.png").scale(1.7))

        # null_equation = Group(
        #     MathTex("P(", color=BLUE), GenericImageMobject("assets/rod.png").scale(1), MathTex(") = \mu = 0.5", color=BLUE)
        # ).arrange(RIGHT, buff=0.1).next_to(null_spinner, DOWN)

        alt_hypothesis_txt = Tex(
            r"alternative hypothesis ($H_1$)"
        ).move_to(self.camera.frame_center).align_on_border(UP)
        alt_hypothesis_txt[0][0:11].set_color(YELLOW)
        alt_hypothesis_txt[0][22:24].set_color(YELLOW)

        alt_spinner = Spinner(0.6).next_to(alt_hypothesis_txt, DOWN).scale(1.7).set_x(alt_hypothesis_txt.get_x()).set_y(1)
        alt_spinner.add_image(GenericImageMobject("assets/rod.png").scale(1.7))

        # steve_angel = GenericImageMobject("assets/steve_angel.png").scale(0.4).next_to(null_spinner, LEFT, buff=0)
        steve_devil = GenericImageMobject("assets/steve_devil.png").scale(0.4).next_to(alt_spinner, LEFT, buff=0)

        alt_equation = Group(
            MathTex("P(", color=BLUE), GenericImageMobject("assets/rod.png").scale(1), MathTex(") = \mu > 0.5", color=BLUE)
        ).arrange(RIGHT, buff=0.1).next_to(alt_spinner, DOWN)

        blaze_hypotheses = Group(alt_hypothesis_txt, alt_spinner, steve_devil, alt_equation)

        geq = alt_equation[2][0][3]

        one_sided_txt = Text('"one-sided" alternative', font_size=40).next_to(alt_equation, DOWN, buff=1)
        one_sided_arrow = Arrow(
            one_sided_txt.get_edge_center(UP),
            geq.get_edge_center(DOWN),
            stroke_width=6
        )

        #########################

        person_green = GenericImageMobject("assets/person_green.png")
        person_white = GenericImageMobject("assets/person_white.png")

        drug_data = BinomDataGraphic(38, 48, person_green.copy(), person_white.copy(), 
                                     width=3, ncol=9).move_to((1.5,0,0))
        pill = GenericImageMobject("assets/pill.png").scale(2).next_to(drug_data, UP)
        
        no_drug_data = BinomDataGraphic(21, 48, person_green.copy(), person_white.copy(), 
                                        width=3, ncol=9).next_to(drug_data, RIGHT)
        no_pill = Group(
            GenericImageMobject("assets/pill.png").scale(2),
            GenericImageMobject("assets/dont.png").scale(0.4)
        ).next_to(no_drug_data, UP).set_y(pill.get_y())
        
        person_green.scale_to_fit_height(drug_data[1].height)

        legend = Group(
            person_green.copy(),
            Text("= recovered", font_size=32)
        ).arrange(RIGHT, buff=0.2).next_to(Group(drug_data, no_drug_data), DOWN)

        null_hypothesis_txt = Tex(
            r"null hypothesis",
            font_size = 60
        ).move_to((-3.5, 2, 0))

        alt_hypothesis_txt = Tex(
            r"alternative hypothesis",
            font_size = 60
        ).move_to((-3.5, -0.5, 0))
        alt_hypothesis_txt[0][0:11].set_color(YELLOW)

        null_equation = Group(
            MathTex("H_0: P("), person_green.copy(), MathTex("|"), pill.copy().scale(0.8),
            MathTex(") = P("), person_green.copy(), MathTex("|"), no_pill.copy().scale(0.8), MathTex(")")
        ).arrange(RIGHT, buff=0.1).next_to(null_hypothesis_txt, DOWN)

        alt_equation = Group(
            MathTex("H_1: P("), person_green.copy(), MathTex("|"), pill.copy().scale(0.8),
            MathTex(r") \neq P("), person_green.copy(), MathTex("|"), no_pill.copy().scale(0.8), MathTex(")")
        ).arrange(RIGHT, buff=0.1).next_to(alt_hypothesis_txt, DOWN)
        alt_equation[0][0][0:2].set_color(YELLOW)

        drug_example = Group(drug_data, pill, no_drug_data, no_pill, legend, 
                             null_hypothesis_txt, alt_hypothesis_txt, null_equation, alt_equation)

        neq = alt_equation[4][0][1:3]

        two_sided_txt = Text('"two-sided" alternative', font_size=40).next_to(alt_equation, DOWN, buff=1)
        two_sided_arrow = Arrow(
            two_sided_txt.get_edge_center(UP),
            neq.get_edge_center(DOWN),
            stroke_width=6
        )

        #################################################################
        # Animation (1)                                                 #
        #################################################################
        # self.add(NumberPlane(
        #     background_line_style={
        #         "stroke_width": 2,
        #         "stroke_opacity": 0.6
        #     }).set_z_index(-1))
        # self.add(footnote_circle, footnote_txt, footnote_border)
        # self.add(blaze_hypotheses, one_sided_txt, one_sided_arrow)
        # self.add(drug_example, two_sided_txt, two_sided_arrow)

        self.add(footnote_sector)
        self.play(
            footnote_angle.animate.set_value(TAU),
            Create(footnote_border),
            run_time=0.5
        )
        self.play(
            Write(footnote_txt),
            FadeIn(blaze_hypotheses),
            run_time=0.6
        )

        self.wait()

        self.play(
            Indicate(geq, scale_factor=1.4),
            run_time=2
        )

        self.wait()

        self.play(
            alt_spinner.probability.animate.set_value(0.4)
        )

        self.play(
            alt_spinner.probability.animate.set_value(0.6)
        )

        self.wait()

        self.play(
            Write(one_sided_txt),
            GrowArrow(one_sided_arrow),
            run_time=0.8
        )

        self.wait()

        self.play(
            FadeOut(blaze_hypotheses, one_sided_arrow, one_sided_txt)
        )

        self.play(
            FadeIn(drug_example)
        )

        self.wait()

        self.play(
            Indicate(neq, scale_factor=1.4),
            run_time=2
        )

        self.wait()

        self.play(
            Write(two_sided_txt),
            GrowArrow(two_sided_arrow),
            run_time=0.8
        )

        self.wait()
 
        self.play(
            FadeOut(*[m for m in self.mobjects if m not in [footnote_sector, footnote_border, footnote_txt]])
        )

        self.wait(0.1)






