d = {"B": 222, "A": 111, "D": 444, "C": 333}
sorted_d = min(d.keys(), key=lambda k: d[k])
print(sorted_d)
