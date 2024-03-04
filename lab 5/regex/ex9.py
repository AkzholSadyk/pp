import re
def text(a):
   return re.sub(r" (\W) ([A-Z])", r"\1 \2", a)
a=input('')
print(text(a))