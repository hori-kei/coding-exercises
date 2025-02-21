l1 = [1, 2, 3, "4", 5]
s = any(isinstance(i, str) for i in l1)
if s:
    print("文字列が入っています")
else:
    print("文字列は入っていません")
