a = float(input("aの値を入力: "))
b = float(input("bの値を入力: "))

# TODO

def prime_number(n):
    if n < 1 or n != int(n):
         print(f"error: {n}は自然数ではありません。")
    else:
         j = 0
         for i in range(2,int(n)):
            if n % i == 0:
                   j += 1
         if n == 1:
             j = 1
         if j == 0:
             print(bool(1))
         else:
             print(bool(0))


prime_number(a)
prime_number(b)