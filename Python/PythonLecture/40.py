l1 = [1, "22", 3, "444", 0.0, "5"]
int_l1 = [i for i in l1 if isinstance(i, int)]
print(max(int_l1))
print(min(int_l1))
