
a = int(input("aの値を入力: "))
b = int(input("bの値を入力: "))

# TODO

def prime_number(x):
    j = 0
    for i in range(2,x):
         if x % i == 0:
             j += 1
    if x == 1:
         j = 1
    if j == 0:
         print(f"{x}は素数です。")
    else:
         print(f"{x}は素数ではありません。")


prime_number(a)
prime_number(b)