
from math import pi
import sys

def help():
    print("It's necessary to enter circle area.")
    print("Sintax: {} <radius>".format(sys.argv[0][:2]))

def circle(radius):
    return pi * float(radius) ** 2


if __name__ == '__main__':
    if len(sys.argv) < 2:
        help()
    else:
        radius = sys.argv[1]
        area = circle(radius)
        print('Circle area', area)
