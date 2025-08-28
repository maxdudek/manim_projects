from manim import *
from manim.opengl import *
from scipy.stats import binom
from scipy.special import bdtr

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

# def pbinom(x, n, p):
#     lower_tail = binom.cdf(x-1, n, p).item()
#     return (1 - lower_tail)