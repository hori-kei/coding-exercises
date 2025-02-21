import json

s = '{"A": 111, "B": 222, "C": 333}'
print(s)
d = json.loads(s)
print(d)

new_d = json.dumps(d)
print(new_d)
