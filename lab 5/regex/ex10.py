import re
def convert(text) :
    x=re.sub(r"(\w)([A-Z])", r"\1 \2", text)
    ans=re.sub("[]","_",x)
    return ans 
a=input()
print(convert(a))