import math

from shape import Shape
import math


class Circle(Shape):
    def __init__(self, width, height):
        super().__init__(width, height)

    def calculate_surface(self, list_figures: str):
        res_s = (self.width * self.width) * math.pi
        return res_s
