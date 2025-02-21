s = input("文字を入力してください > ")
if s[0].isupper():
    s += s
elif s[0].islower():
    s = s[0].upper() + s[1:]
print(s)
