import re

def ss(a):
    b = '^a.*b$'
    if re.search(b, a):
        return 'Found a match!'
    else:
        return 'Not matched!'

a = str(input())
b = ss(a)
print(b)