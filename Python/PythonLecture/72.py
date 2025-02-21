d = {"A": 111, "B": 222, "C": 333}
l1 = ["B", "C", "D", "A"]

for i in l1:
    print(f"{i}に対するValue : {d.get(i)}")
