l1 = [4, 6, 9, 2]
l2 = [3, 5, 7]
l3 = [1, 9, 7]
new_l = [l1, l2, l3]
sort_l = sorted(new_l, key=lambda x: sum(x) / len(x), reverse=True)
print(sort_l[0])
