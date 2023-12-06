a = int(input("aの値を入力: "))
b = int(input("bの値を入力: "))

# TODO

j = 0
for i in range(2,a):
     if a % i == 0:
          j += 1
if j == 0:
      print(f"{a}は素数です。")
else:
      print(f"{a}は素数ではありません。")

j = 0
for i in range(2,b):
     if b % i == 0:
          j += 1
if j == 0:
      print(f"{b}は素数です。")
else:
      print(f"{b}は素数ではありません。")