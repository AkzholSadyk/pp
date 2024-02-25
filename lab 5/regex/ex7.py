import re
def ss(a):
    x = re.split('_',a)
    rr = x[0] + ''.join(i.title() for i in x[1:])
    return rr
    


a=input('')
print(ss(a))