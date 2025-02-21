s1 = input("1つ目の文字列を入力してください > ")
s2 = input("2つ目の文字列を入力してください > ")
split_s1 = s1.split()
split_s2 = s2.split()
new_l = [i for i in split_s1 if i in s2]
print(new_l)
