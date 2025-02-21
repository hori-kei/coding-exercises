l1 = [1, 2, None, False, "3", "4", None, True]
new_l = [i for i in l1 if i is True or i is None]
print(len(new_l))
