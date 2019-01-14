from math import pi


def circle(radius):
    print('Circle area', pi * float(radius) ** 2)


if __name__ == '__main__':
    radius = input('Enter radius: ')
    circle(radius)
