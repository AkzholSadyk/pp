import re

def ss(a):
    b = '^a(b*)$'
    if re.search(b, a):
        return "match"
    else:
        return "not matched"

a = str(input())
b = ss(a)
print(ss(a))