from manim import *
from manim.opengl import *
from scipy.stats import binom
from scipy.special import bdtr
from math import *
import functools

BLUE_TXT="#76C9DC"

FadeIn = functools.partial(FadeIn, shift=DOWN*0.2)
FadeOut = functools.partial(FadeOut, shift=DOWN*0.2)

Circumscribe = functools.partial(Circumscribe, time_width=0.6)

# Text.set_default(font="Aptos")
class GenericImageMobject:
    def __new__(cls, filename_or_array, **kwargs):
        if config.renderer == RendererType.OPENGL:
            return OpenGLImageMobject(filename_or_array, **kwargs)
        else:
            return ImageMobject(filename_or_array, **kwargs)
        
# P(X >= x)
def pbinom(x, n, p):
    lower_tail = bdtr(x-1, n, p)
    return (1 - lower_tail)

def binom_pmf(x, n, p):
    return comb(n, x) * (p**x) * ((1-p)**(n-x))

def dnorm(x):
    return exp(-1/2 * x**2)/sqrt(2*PI)

def pdf_plot(
    func, xmin, xmax, ymax, x_length, y_length, 
    stat_start=1.6, where=(3,0,0), label="z",
    x_inc=1, y_inc=0.1,
):
    grid = Axes(
        x_range=[xmin,xmax,x_inc],  # step size determines num_decimal_places.
        y_range=[0, ymax, y_inc],
        x_length=x_length,
        y_length=y_length,
        tips=False,
    ).move_to(where)
    density = grid.plot(func, color=WHITE, stroke_width=3)
    tracker = ValueTracker(stat_start)
    area_lower = always_redraw(lambda:
        grid.get_area(density, x_range= (xmin,tracker.get_value()), color=DARK_BLUE, opacity=0.7)
    )
    area_upper = always_redraw(lambda:
        grid.get_area(density, x_range= (tracker.get_value(),xmax), color=BLUE, opacity=0.7)
    )
    line = always_redraw(lambda:
        Line(
            grid.c2p(tracker.get_value(), ymax),
            grid.c2p(tracker.get_value(), 0),
            color=ORANGE
        )
    )
    label = MathTex(label, color=ORANGE)
    label.add_updater(lambda m: m.next_to(line, UP))
    label.resume_updating()

    return grid, density, tracker, Group(area_lower, area_upper), line, label

def separate_double_arrow(double_arrow):

    if double_arrow.width > double_arrow.height:
        dirs = (LEFT, RIGHT)
    else:
        dirs = (UP, DOWN)

    arrow1 = Arrow(
        double_arrow.get_center(),
        double_arrow.get_edge_center(dirs[0]),
        color=double_arrow.color,
        stroke_width = double_arrow.stroke_width,
        buff=0
    )

    arrow2 = Arrow(
        double_arrow.get_center(),
        double_arrow.get_edge_center(dirs[1]),
        color=double_arrow.color,
        stroke_width = double_arrow.stroke_width,
        buff=0
    )

    return VGroup(arrow1, arrow2)


def GrowDoubleArrow(double_arrow_separated):
    return AnimationGroup(
        GrowArrow(double_arrow_separated[0]),
        GrowArrow(double_arrow_separated[1])
    )



# def pbinom(x, n, p):
#     lower_tail = binom.cdf(x-1, n, p).item()
#     return (1 - lower_tail)