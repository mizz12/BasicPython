a = 1
b = -6
c = 9

# TODO
def formula(a,b,c):
    x1 = (-b+(b**2-4*a*c)**(1/2))/2*a
    x2 = (-b-(b**2-4*a*c)**(1/2))/2*a
    return x1,x2

print(formula(1,-6,9))
print(formula(1,2,-8))
print(formula(8,-6,-35))
print(formula(1,0,1))
