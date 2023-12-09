#trapezoidal_integral.py
import math
# --example--
# print(sin(0))
# >>> 0
# -----------

pi = math.pi
a = 0
b = 1 / 2 * pi
n = 100

h = (b - a) / n
def integrate_sin(x):
    sigma = 0
    for k in range(1,n + 1):
         sigma += math.sin(a + (k - 1) * h) + math.sin(a + k * h)
    return (h / 2) * sigma

print(integrate_sin(0))