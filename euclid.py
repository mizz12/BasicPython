a = int(input("a の値を入力: "))
b = int(input("b の値を入力: "))

# TODO

if(a > b):
    c = a
    a = b
    b = c
def euclid(a,b):
     while b :
          c = b
          b = a % b
          a = c
     return int(c)
    
print(euclid(a,b))