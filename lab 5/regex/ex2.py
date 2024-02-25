import re

def ss(a):
    x = '^a(b*)$'
    if re.search(x, a) and 3<=len(a)<=4:
        return "match"
    else:
        return "not matched"

a = str(input())
b = ss(a)
print(ss(a))
