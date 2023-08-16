from triangle import Triangle
from rectangle import Rectangle
from circle import Circle
# from shape import Shape
from ui import add_type_figure

while True:
    try:
        num_figures = int(input('Please enter the number of the figures:\n'))
        break
    except ValueError:
        print('Not a number!')
        print('Try again!')

# dict_figures = {
#     'Circle': 'C',
#     'Triangle': 'T',
#     'Rectangle': 'R'
# }
list_figures_res = []
list_figures = []
for i in range(num_figures):
    fig = add_type_figure()
    list_figures.append(fig)
    print(list_figures)

print(list_figures)
for i in range(len(list_figures)):
    print(i + 1, list_figures[i], end='. ')
    print(list_figures[i])

for i in range(len(list_figures)):
    if list_figures[i][0] == 'T':
        triangle = Triangle(list_figures[i][2], list_figures[i][4])
        # list_figures_res.append(triangle)
        print(f"S Triangle: {triangle.calculate_surface(list_figures[i][0])}")

    elif list_figures[i][0] == 'C':
        circle = Circle(list_figures[i][2], list_figures[i][2])
        # list_figures_res.append(circle)
        print(f"S Circle: {circle.calculate_surface(list_figures[i][0])}")
    else:
        rectangle = Rectangle(list_figures[i][2], list_figures[i][4])
        # list_figures_res.append(rectangle)
        print(f"S Rectangle: {rectangle.calculate_surface(list_figures[i][0])}")
