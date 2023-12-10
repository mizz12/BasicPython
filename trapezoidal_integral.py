import math
# --example--
# print(sin(0))
# >>> 0
# -----------

def integrate_sin(f,a = 0,b = 1,n = 100):
    h = (b - a) / n
    sigma = 0
    for k in range(1,n + 1):
         x1 = a + (k - 1) * h
         x2 = a + k * h
         sigma += f(x1) + f(x2)
    return float((h / 2) * sigma)

#(1)
def sin(x):
     return math.sin(x)
print(integrate_sin(sin,a,math.pi / 2,50))

#(2)
def f(x):
     return 4 / (1 + x ** 2)
print(integrate_sin(f,a,b,n))

#(3)
def f(x):
     return (math.pi ** 0.5) ** (-1 * x ** 2)
print(integrate_sin(f,-100,100,1000))
