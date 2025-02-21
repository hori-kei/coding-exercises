t = (1, [2, 3], "4", (5, 6, 7), "8", (9, 10))
new_t = [i for i in t if isinstance(i, tuple)]
print(len(new_t))
