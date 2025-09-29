from manim import *
import numpy as np
from math import *
from scipy.stats import binom
from dudek_utils import *
from manim.typing import *
from sys import maxsize

PROB_PINK="#F799E9"
class Spinner(Group):
    def __init__(self, probability, color = BLUE, start_angle = PI/2, clockwise=False, reverse_sector_direction=True, **kwargs):
        super().__init__(**kwargs)

        self.circle = Circle(color=WHITE)

        self.probability = ValueTracker(probability)
        self.start_angle = start_angle
        self.clockwise = clockwise

        def draw_sector():
            sector = Sector(
                radius = self.circle.width/2,
                angle=self.probability.get_value()*TAU*(-1 if clockwise else 1),
                start_angle=start_angle,
                arc_center=self.circle.get_center(),
                fill_color=color
            )
            
            if reverse_sector_direction: sector = sector.reverse_direction()

            return sector

        self.sector = always_redraw(draw_sector)
        self.sector.set_z_index(self.circle.z_index - 1) # Move sector behind circle
        
        self.angle = 20*DEGREES

        self.arrow = GenericImageMobject("assets/spinner.png").scale(0.35).shift(UP*0.115).shift(RIGHT*0.002).rotate(self.angle, about_point=self.circle.get_center())

        self.image = None

        self.add(self.circle, self.sector, self.arrow)
    
    def add_image(self, image_mobject=None, angle=180*DEGREES, r=0.25, **kwargs):
        if angle == "prob":
            angle = self.start_angle + self.probability.get_value()/2*TAU*(-1 if self.clockwise else 1)
    
        image_location = self.circle.get_center() + np.array([cos(angle), sin(angle), 0]) * self.circle.width * r

        if image_mobject is not None:
            self.image = image_mobject
            self.image.move_to(image_location)
            self.image.set_z_index(self.arrow.z_index - 1) # Move image behind arrow

            self.add(self.image)

            return(self.image)
        else:
            return(image_location)

    def set_probability(self, probability, **kwargs):

        return(
            self.probability.animate.set_value(probability)
        )


    def spin(self, n_rotations, **kwargs):
        self.angle = (self.angle + n_rotations*TAU) % TAU
        return(
            Rotate(self.arrow, angle=n_rotations*TAU, 
                   about_point=self.circle.get_center(), 
                   rate_func=rate_functions.rush_from, **kwargs)
        )

class BinomDataGraphic(Group):
    """
    x (int):                  number of positive trials
    n (int):                  total number of trials
    pos_image (GenericImageMobject): representing positive trial
    neg_image (GenericImageMobject): representing negative trial
    buffer_ratio (float):     distance bewteen images, and border 
                              (as proportion of supplied dimenstion)
    """
    def __init__(self, x, n, pos_image: GenericImageMobject, neg_image: GenericImageMobject, 
                 width=None, height=None, nrow=None, ncol=None, buffer_ratio=0.01, border = True,
                 **kwargs):
        super().__init__(**kwargs)

        self.n = n
        self.x = x
        self.pos_image = pos_image
        self.neg_image = neg_image

        if (nrow is None) + (ncol is None) != 1:
            raise ValueError("Must specify exactly one of nrow or ncol")

        if (width is None) + (height is None) != 1:
            ValueError("Must specify exactly one of width or height")

        if (nrow is None): nrow = ((n-1) // ncol) + 1
        if (ncol is None): ncol = ((n-1) // nrow) + 1

        self.ncol = ncol
        self.nrow = nrow

        if (height is None):
            buffer = buffer_ratio * width
            image_width = (width - buffer*(ncol+1)) / (ncol+1)
            pos_image.scale_to_fit_width(image_width)
            neg_image.scale_to_fit_width(image_width)

            height = buffer*(nrow+1) + self.get_image_height()*(nrow+1)

        if (width is None):
            buffer = buffer_ratio * height
            image_height = (height - buffer*(nrow+1)) / (nrow+1)
            pos_image.scale_to_fit_height(image_height)
            neg_image.scale_to_fit_height(image_height)

            width = buffer*(ncol+1) + self.get_image_width()*(ncol+1)

        self.buffer_ratio = buffer / width # buffer_ratio is always proportional to width

        self.border = Rectangle(width = width, height = height)
        self.has_border = False
        
        # Add images
        for i in range(n):
            old_image = pos_image if i < x else neg_image
            new_image = old_image.copy().move_to(self.index2point(i))
            # new_image = Dot(self.index2point(i), color = BLUE, radius=0.02) # debug
            # new_image = Text(str(i), font_size=16).move_to(self.index2point(i)) # debug
            self.add(new_image)

        if (border):
            self.has_border = True
            self.add(self.border)
            
    def get_debug_text(self):
        text = Paragraph(
            f"nrow = {self.nrow}\n" +
            f"ncol = {self.ncol}\n" +
            f"width = {self.border.width:.3f}\n" +
            f"height = {self.border.height:.3f}\n" +
            f"image_width = {self.get_image_width():.3f}\n" +
            f"image_height = {self.get_image_height():.3f}\n" +
            f"buffer = {self.get_buffer():.3f}\n",
            font_size = 24,
            color = BLUE
        ).align_on_border(UP+LEFT)

        return text
        
    def get_image_height(self):
        return max(self.pos_image.height, self.neg_image.height)
    
    def get_image_width(self):
        return max(self.pos_image.width, self.neg_image.width)
    
    def get_top_left(self):
        return(self.border.get_corner(UP+LEFT))

    def get_buffer(self):
        return self.border.width * self.buffer_ratio

    def index2coord(self, index):
        col = index % self.ncol
        row = index // self.ncol
        return (row, col)
    
    def coord2index(self, row, col):
        return (row*self.ncol) + col
    
    def coord2image(self, row, col):
        i = self.coord2index(row, col)
        return self[i]

    def coord2point(self, row, col):
        point = self.get_top_left()
        point += DOWN*(row+1)*(self.get_image_height() + self.get_buffer())
        point += RIGHT*(col+1)*(self.get_image_width() + self.get_buffer())
        return point

    def index2point(self, index):
        return(self.coord2point(*self.index2coord(index)))
    
    def create_by_index(self, **kwargs):
        images = self[:-1] if self.has_border else self
        add_animation = AnimationGroup(*[FadeIn(i) for i in images], **kwargs)
        return add_animation
        
class PMFBarPlot(VGroup):
    def __init__(
        self, x_values, y_values, width, height, 
        x_label=None, x_prime=0, color1=BLUE, color2=DARK_BLUE, gap=0.05, 
        max_y = None, y_nums = True, x_labels_font_size=28, coloring_mode="upper_tail",
        rejection_region_start = maxsize, rejection_region_size = 0.05, show_y_label = True,
        include_ticks=True, mode=None, x_prime_height_scale=1,
        x_label_offset=np.array([0,0,0]), **kwargs
        ):
        """
        coloring_mode:  "upper_tail" colors all bars >= x'
                        "equal" colors only the bar == x'
                        "rejection_region"
                        "two-sided" colors all bars >= x' and all bars <= 2*mode-x'
        """
        super().__init__(**kwargs)

        self.x_values = x_values
        self.y_values = y_values # Don't use this, use y_trackers

        self.color1 = color1
        self.color2 = color2

        self.mode = mode
        self.x_prime_height_scale = x_prime_height_scale

        self.x_prime = ValueTracker(x_prime)

        self.rejection_region_start = ValueTracker(rejection_region_start)
        self.rejection_region_size = ValueTracker(rejection_region_size)

        # Update axes ranges
        if max_y is None: max_y = max(y_values) * 1.1
        base10_inc = 10 ** floor(log10(max_y/2))
        num_base10_inc = floor(max_y / base10_inc)
        y_inc = base10_inc * ceil(num_base10_inc/5)

        x_inc = max(1, len(x_values)//8)

        self.axes = Axes(
            x_range=[min(x_values)+0.5, max(x_values)+1.5, x_inc],
            y_range=[0, max_y, y_inc],
            x_length=width,
            y_length=height,
            axis_config={
                "color": WHITE,
                "include_ticks": include_ticks
            },
            y_axis_config={"include_numbers": y_nums},
            tips=False,
        )
        self.add(self.axes)

        # Create bars
        self.bars = VGroup()
        self.height_trackers = list()
        self.y_trackers = list()
        self.bar_dict = dict()
        self.bar_width = self.axes.get_x_unit_size()-gap
        
        for k, pmf_val in zip(x_values, y_values):
            height_tracker = ValueTracker(self.y2h(pmf_val))
            height_tracker.add_updater(lambda: self.y2h(pmf_val))
            y_tracker = ValueTracker(pmf_val)

            def bar_drawer(k=k, pmf_val=pmf_val, y_tracker=y_tracker):
                
                return Rectangle(
                    width=self.bar_width,
                    height=self.y2h(y_tracker.get_value()),
                    color=self.get_bar_color(k, coloring_mode),
                    fill_opacity=0.7,
                    stroke_width=1
                ).move_to(self.axes.c2p(k+1, pmf_val/2)).align_to(self.axes.c2p(k+1, 0), DOWN)

            bar = always_redraw(bar_drawer)

            # bar = always_redraw(
            #     lambda k=k, pmf_val=pmf_val, y_tracker=y_tracker: Rectangle(
            #         width=self.bar_width,
            #         height=self.y2h(y_tracker.get_value()),
            #         color=self.color1 if k >= self.x_prime.get_value() else self.color2,
            #         fill_opacity=0.7,
            #         stroke_width=1
            #     ).move_to(self.axes.c2p(k+1, pmf_val/2)).align_to(self.axes.c2p(k+1, 0), DOWN)
            # )
            self.height_trackers.append(height_tracker)
            self.y_trackers.append(y_tracker)
            self.bars.add(bar)
            self.bar_dict[k] = bar

        self.add(self.bars)

        # Axis Title Labels
        if (x_label is not None): 
            self.x_label = self.axes.get_x_axis_label(
                x_label.scale(1),
                edge=DOWN, direction=DOWN,buff=0.7,
            ).shift(x_label_offset)
            self.add(self.x_label)

        if show_y_label:
            self.y_label = self.axes.get_y_axis_label(
                MathTex("P(X = x)").scale(0.8).rotate(90 * DEGREES),
                edge=LEFT, direction=LEFT, buff=0.3,
            )
            self.add(self.y_label)

        # x-axis num labels
        self.x_num_labels = VGroup()
        for k in x_values[::x_inc]:
            x_num_label = Text(str(int(k)), font_size=x_labels_font_size)
            x_num_label.next_to(self.axes.c2p(k+1, 0), DOWN)
            self.x_num_labels.add(x_num_label)
        self.add(self.x_num_labels)

        # x_prime line
        self.x_prime_line = always_redraw(
            lambda: Line(
                start = self.axes.c2p(self.x_prime.get_value()+1, (max_y/1.1)*self.x_prime_height_scale),
                end = self.axes.c2p(self.x_prime.get_value()+1, 0),
                color = ORANGE
            ).set_opacity(1 if self.x_prime.get_value() > 0 else 0)
        )

        # x_prime_label
        self.x_prime_label = Integer(self.x_prime.get_value(), font_size=36, color=ORANGE).next_to(self.x_prime_line, LEFT, buff=0.1).align_to(self.x_prime_line, UP)
        self.x_prime_label.add_updater(
            lambda i: i.next_to(self.x_prime_line, LEFT, buff=0.1).align_to(self.x_prime_line, UP).set_value(self.x_prime.get_value())
        )
        
    """
    Returns the rectangle shape for a specific x coordinate
    """
    def x2bar(self, x):
        return self.bar_dict[x]
    
    def x2i(self, x):
        return int(x - min(self.x_values))
    
    def i2x(self, i):
        return i + min(self.x_values)
    
    # y value to height
    def y2h(self, y):
        return self.axes.c2p(0, y)[1] - self.axes.c2p(0, 0)[1]
    
    def get_bar_color(self, k, coloring_mode):
        if coloring_mode == "upper_tail":
            color=self.color1 if k >= self.x_prime.get_value() else self.color2
        elif coloring_mode == "two-sided":
            x = self.x_prime.get_value()
            upper = max(x, 2*self.mode-x)
            lower = min(x, 2*self.mode-x)
            color=self.color1 if (k >= upper or k <= lower) else self.color2
        elif coloring_mode == "equal":
            color=self.color1 if (k == round(self.x_prime.get_value()) or self.x_prime.get_value() <= 0) else self.color2
        elif coloring_mode == "rejection_region":
            rejection_region_start = int(round(self.rejection_region_start.get_value()))
            if k < rejection_region_start: return self.color2

            start_index = self.x2i(rejection_region_start)
            end_index = self.x2i(k)
            # print(k)
            # print(self.x_values)
            # print(start_index, end_index)
            # print(len(self.y_trackers))
            y_vals = [self.y_values[i] for i in range(start_index, end_index+1)]

            if sum(y_vals) < self.rejection_region_size.get_value(): color = PROB_PINK
            else: color = self.color2

        return color

    def create_bars(self, **kwargs):
        # Get original y values
        y_values = [self.y_trackers[i].get_value() for i in range(len(self.bars))]

        animations = list()
        for i in range(len(self.bars)): 
            self.y_trackers[i].set_value(0)
            animations.append(self.y_trackers[i].animate.set_value(y_values[i]))

        return AnimationGroup(*animations, **kwargs)
    
    def freeze_bars(self):
        for bar in self.bars:
            bar.clear_updaters()
    
    def change_y_values(self, new_y_values, **kwargs):
        if len(new_y_values) != len(self.bars):
            raise ValueError(f"len(new_y_values) = {len(new_y_values)} does not equal len(self.bars) = {len(self.bars)}")

        animations = list()
        for i in range(len(self.bars)): 
            animations.append(self.y_trackers[i].animate.set_value(new_y_values[i]))
        
        self.y_values = new_y_values

        return AnimationGroup(*animations, **kwargs)

    
    @staticmethod
    def binom(n, p, width=5, height=3, alpha=0.01, min_prob=0.0001, **kwargs):
        x_values = np.arange(binom.ppf(alpha, n, p), binom.ppf(1-alpha, n, p)+1)
        y_values = np.array([binom.pmf(k, n, p) for k in x_values])

        # # Only show bars with significant probability
        idx = y_values > min_prob
        x_values = x_values[idx]
        y_values = y_values[idx]

        return PMFBarPlot(x_values, y_values, width=width, height=height, mode = n*p, **kwargs)

class TestScene(Scene):
    def construct(self):

        #################################################################
        # BinomDataGraphic                                              #
        #################################################################

        # rod = GenericImageMobject("assets/rod.png")
        # red_x = GenericImageMobject("assets/red_x.png")

        # data_graphic = BinomDataGraphic(67, 100, rod, red_x, width=5, nrow=10)

        # self.play(
        #     Create(data_graphic.border),
        #     data_graphic.create_by_index(),
        #     run_time=1
        # )
        # self.wait()

        #################################################################
        # BinomDataGraphic                                              #
        #################################################################


        # pmf_bars = [PMFBarPlot.binom(n,0.5) for n in [1, 2, 10, 100]]
        # self.add(pmf_bars[0])
        # self.wait()
        # for i in range(1,len(pmf_bars)):
        #     self.play(
        #         ReplacementTransform(pmf_bars[i-1], pmf_bars[i])
        #     )

        pmf_plot = PMFBarPlot.binom(
            n=1000, p=0.5, width=7, height=3, 
            gap=0.01, alpha=5e-7, min_prob=0, x_prime = 510,
            x_label=Tex("$x$", font_size = 40), coloring_mode = "rejection_region",
            rejection_region_start = 500, rejection_region_size = 0.2,
        )

        self.add(pmf_plot)
        self.wait()
        self.play(
            pmf_plot.rejection_region_start.animate.set_value(520),
            run_time=2
        )

        self.play(
            pmf_plot.rejection_region_start.animate.set_value(480),
            run_time=2
        )

        self.play(
            pmf_plot.rejection_region_size.animate.set_value(0.5),
            run_time=2
        )

        self.play(
            pmf_plot.rejection_region_size.animate.set_value(0.05),
            run_time=2
        )
        self.wait()


        self.wait()

