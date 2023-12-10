import math
#問3
a = int(input("a の値を入力: "))
b = int(input("b の値を入力: "))

# TODO

def euclid(a,b):
     if(a > b):
          b,a = a,b
     while b :
          c = b
          b = a % b
          a = c
     return int(c)
    
print(euclid(a,b))

#問4

def relatively_prime(a,b):
     if euclid(a,b) == 1:
          return bool(1)
     else:
          return bool(0)
     
print(relatively_prime(a,b))

#エクストラ問題

import random

l = 0
for i in range(100000):
     a,b = random.sample(range(1, 10000), 2)
     if relatively_prime(a,b) == True:
          l += 1
print(f"互いに素である確率は{l / 100000}です。")

#答え合わせ用
print(6 / (math.pi ** 2))
