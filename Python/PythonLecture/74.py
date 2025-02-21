d = {"B": 222, "A": 111, "D": 333, "C": 444}
sorted_d = dict(sorted(d.items(), key=lambda x: x[1]))
print(sorted_d)
