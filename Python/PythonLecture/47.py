l1 = [1, 3, 2, 3, 4, 6, 5, 8, 7]
new_l = [v for i, v in enumerate(l1) if not (i % 3 == 0 and v % 3 == 0)]
print(new_l)
