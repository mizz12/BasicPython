
a = int(input("a の値を入力: "))
b = int(input("b の値を入力: "))

# TODO

if(a > b):
    b,a = a,b
def euclid(a,b):
     while b :
          c = b
          b = a % b
          a = c
     return int(c)
    
print(euclid(a,b))