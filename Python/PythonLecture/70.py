keys = ["A", "B", "C"]
values = [111, 222, 333]
new_d = {k: v for k, v in zip(keys, values)}
print(new_d)
