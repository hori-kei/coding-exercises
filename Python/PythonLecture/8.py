l2 = [i for i in range(1, 31) if i % 3 == 0]
print(l2)

new_l = []
for i in range(1, 31):
    if i % 3 == 0:
        new_l.append(i)
print(new_l)
