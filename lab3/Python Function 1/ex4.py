def prime_numbers(a):
    if a <= 1:
        return False
    for i in range(2,int(a ** 0.5) + 1):
        if a % i == 0:
            return False
    return True

a=[int(i) for i in input().split()]
aaa= list(filter(lambda x: prime_numbers(x), a))
print(aaa)