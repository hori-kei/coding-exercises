l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
new_l = [tuple(l1[i : i + 3]) for i in range(0, 9, 3)]
print(new_l)
