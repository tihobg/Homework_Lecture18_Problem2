from typing import List


def add_type_figure() -> List:
    figure_data = []
    add_figure_type = input('Please add the type of the figure (T, R or C)\n')
    while add_figure_type:
        if add_figure_type == 'T' or add_figure_type == 'R' or add_figure_type == 'C':
            break
        add_figure_type = input('Please, enter the correct type - T, R or C\n')
    if add_figure_type == 'C':
        add_figure_radius = enter_circle_radius()
        figure_data = add_circle_data(add_figure_type, add_figure_radius)
        return figure_data
    else:
        add_figure_width = enter_figure_width()
        add_figure_height = enter_figure_height()
        figure_data = add_figure_data(add_figure_type, add_figure_width, add_figure_height)
        return figure_data


def enter_circle_radius() -> int:
    while True:
        try:
            add_figure_radius = int(input('Please add the radius of the figure (integer)\n'))
            break
        except ValueError:
            print('Not a number!')
            print('Try again!')
    return add_figure_radius


def enter_figure_width() -> int:
    while True:
        try:
            add_figure_width = int(input('Please add the width of the figure (integer)\n'))
            break
        except ValueError:
            print('Not a number!')
            print('Try again!')
    return add_figure_width


def enter_figure_height() -> int:
    while True:
        try:
            add_figure_height = int(input('Please add the height of the figure (integer)\n'))
            break
        except ValueError:
            print('Not a number!')
            print('Try again!')
    return add_figure_height


def add_circle_data(add_figure_type, add_figure_radius) -> List:
    figure_data = [add_figure_type, ' ', add_figure_radius]
    print(figure_data)
    return figure_data


def add_figure_data(add_figure_type, add_figure_width, add_figure_height) -> List:
    figure_data = [add_figure_type, ' ', add_figure_width, ' ', add_figure_height]
    print(figure_data)
    return figure_data
