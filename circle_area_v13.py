
from math import pi
import sys
import errno

def help():
    print("It's necessary to enter circle area.")
    print("Sintax: {} <radius>".format(sys.argv[0][:2]))

def circle(radius):
    return pi * float(radius) ** 2


if __name__ == '__main__':
    if len(sys.argv) < 2:
        help()
        sys.exit(errno.EPERM)
    if not sys.argv[1].isnumeric():
        help()
        print('Radius must be numeric', area)
        sys.exit(errno.EINVAL)

    radius = sys.argv[1]
    area = circle(radius)
    print('Circle area', area)
