l1 = [1, 5, 3, 2, 4]
s = l1[0]
for i in l1[1:]:
    if i > s:
        s = i
print(s)
