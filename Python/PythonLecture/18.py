s = input("文字を入力してください > ")
new_dict = {}
for i in s:
    if i in new_dict.keys():
        new_dict[i] += 1
    else:
        new_dict[i] = 1
print(new_dict)
