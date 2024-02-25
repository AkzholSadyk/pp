import re

def ss(a):
    b = re.findall('[A-Z]',a)
    return b
   

a = str(input())
print(ss(a))