def my_function(x):
    return x+5

def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))


def my_function(*, x):
  print(x)

my_function(x = 3)