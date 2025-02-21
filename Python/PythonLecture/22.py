s1 = input("1つ目の文字列を入力してください > ")
s2 = input("2つ目の文字列を入力してください > ")
new_s = ""
for i in s1:
    if i in s2 and i not in new_s:
        new_s += i
print(new_s)
