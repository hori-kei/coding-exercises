d = {"A": 111, "B": 222, "C": 333}
new_l = {key: value for key, value in d.items() if value > 150}
print(new_l)
