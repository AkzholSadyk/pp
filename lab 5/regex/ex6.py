import re
def ss(a):
   x = re.sub('[ ,.]', ':', a)
   return x

a=input('')

print(ss(a))