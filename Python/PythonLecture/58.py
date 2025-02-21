t = (1, [2, 3], "4", (5, 6, 7), None, (9, 10))
new_t = []
for i in t:
    if isinstance(i, list):
        new_t.append(tuple(i))
    elif isinstance(i, tuple):
        new_t.append(i)
    else:
        new_t.append((i,))
print(new_t)
