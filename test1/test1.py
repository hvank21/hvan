import sys
from math import cos, radians

print("Hello, Visual Studio")
for i in range(360):
    print(cos(radians(i)))

    # Create a string with spaces proportional to a cosine of x in degrees
def make_dot_string(x):
    return ' ' * int(20 * cos(radians(x)) + 20) + 'o'

for i in range(0,360,12):
    s = make_dot_string(i)
    print(s)