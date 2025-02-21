s1 = input("1つ目の英単語を入力してください > ")
s2 = input("2つ目の英単語を入力してください > ")
s3 = input("3つ目の英単語を入力してください > ")
new_s = [s1, s2, s3]
new_s.sort()
print(f"並び替えた英単語 : {", ".join(new_s)}")
