import re

def ss(a):
    b ='^[A-Z]+([a-z]*)+$'  
    if re.search(b, a):
        return 'Found a match!'
    else:
        return 'Not matched!'

a = str(input())
b = ss(a)
print(b)