s = input("文字を入力してください > ")
vowels = ["a", "i", "u", "e", "o"]
new_s = ""
for i in s:
    if i not in vowels:
        new_s += i
print(new_s)
