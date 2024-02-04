def prime_numbers(n):
    if n <= 1:
        return False
    for i in range(2,int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

n = [2, 3, 4, 5, 6, 7, 8, 9, 10]

prime_numbers1 = list(filter(lambda x: prime_numbers(x), n))

print("Prime numbers:", prime_numbers1)