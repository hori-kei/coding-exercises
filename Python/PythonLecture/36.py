l1 = []
for i in range(2):
    inner_list = []
    for j in range(1, 6):
        inner_list.append(5 * i + j)
    l1.append(inner_list)
print(l1)

l2 = [[5 * i + j for j in range(1, 6)] for i in range(2)]
print(l2)
