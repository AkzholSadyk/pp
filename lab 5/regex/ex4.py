import re

def ss(a):
    b ='^[A-Z]+([a-z]*)+$'  #'^[A-Z].*$'
    if re.search(b, a):
        return 'Found a match!'
    else:
        return 'Not matched!'

a = str(input())
b = ss(a)
print(b)