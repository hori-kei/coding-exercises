d = {"B": 222, "A": 111, "D": 444, "C": 333}
new_d = {k: v for k, v in d.items() if v % 2 == 0}
print(new_d)
