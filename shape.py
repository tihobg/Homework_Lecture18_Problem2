# from triangle import Triangle


class Shape:
    def calculate_surface(self, list_figures: str):
        print('OK')

    def __init__(self,
                 width=0,
                 height=0
                 ):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @width.setter
    def width(self, value):
        self._width = value

    @height.setter
    def height(self, value):
        self._height = value

