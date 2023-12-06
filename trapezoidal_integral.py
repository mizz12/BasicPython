#trapezoidal_integral.py
from math import sin
import math
# --example--
# print(sin(0))
# >>> 0
# -----------

pi = math.pi
a = 0
b = 1 / 2 * pi
x = 45
n = 100

h = (((b - a) / n) / 2) 
for k in range(1,n):
    sigma = sin(x) * (a + (k - 1) * h) + sin(x) * (a + (k * h))

print(h * sigma)