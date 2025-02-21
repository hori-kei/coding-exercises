a = int(input("1つ目の整数を入力してください > "))
b = int(input("2つ目の整数を入力してください > "))
r = a - b
if r < 0:
    r = -r
print(f"計算結果 : {r}")
