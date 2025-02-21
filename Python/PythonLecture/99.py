l1 = ["アメリカ", "カナダ", "スイス", "メキシコ", "セントルシア", "タイ"]
l2 = ["サ", "シ", "ス", "セ", "ソ"]

print("さ行を含む単語 :")
for i in l1:
    for j in l2:
        if j in i:
            print(i)
            break
