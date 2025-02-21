l1 = [1, 2, 3, 4, 5]
l2 = [3, 4, 5]
print(f"l1はl2に含まれている : {set(l1).issubset(l2)}")
print(f"l2はl1に含まれている : {set(l2).issubset(l1)}")
