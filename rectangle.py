from shape import Shape


class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__(width, height)

    def calculate_surface(self, list_figures: str):
        res = self.width * self.height

        return res
