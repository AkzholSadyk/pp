x = lambda a: a + 10
print(x(5))
print(x(6))
print(x(100))


x = lambda a, b, c : a + b + c
print(x(5, 6, 2))


def myfunc(n):
  return lambda a : a * n



