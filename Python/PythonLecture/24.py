s1 = input("1つ目の文字列を入力してください > ")
mid = len(s1) // 2
if len(s1) % 2 == 0:
    s1 = s1[0:mid] + "@" + s1[mid:]
elif len(s1) % 3 == 0:
    s1 = s1[0:mid] + "@" + s1[mid + 1 :]
print(s1)
