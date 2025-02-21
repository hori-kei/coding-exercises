s = "This is the Python exercise."
l1 = s.split()
new_l = [i for i in l1 if "t" not in i]
print(" ".join(new_l))
