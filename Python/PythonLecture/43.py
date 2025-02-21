l1 = [4, "aaa", 2, "ddd", "ccc", 3, 1, "bbb"]
l_str = sorted([i for i in l1 if isinstance(i, str)])
l_int = sorted([i for i in l1 if isinstance(i, int)])
print(l_int + l_str)
