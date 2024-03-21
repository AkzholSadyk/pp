import re
def convert(a) :
    x=re.sub("(\w)([A-Z])", "\1 \2", a)
    ans=re.sub("[]","_",x)
    return ans 
a=input()
print(convert(a))