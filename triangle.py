from shape import Shape


class Triangle(Shape):
    def __init__(self, width, height):
        super().__init__(width, height)

    def calculate_surface(self, list_figures: str):
        # print(f"Width: {self.width}")
        res = (self.width * self.height) / 2
        return res

