def reverse(a):
    reversed = a[::-1]
    reversed = ' '.join(reversed)
    return reversed

a =[str(i) for i in input().split()] 
b = reverse(a)
print(b)
