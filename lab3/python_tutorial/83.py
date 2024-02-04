def my_function(*kids):
  print("The youngest child is " + kids[0])
my_function("Emil", "Tobias", "Linus")



def my_function(*, x):
  print(x)

my_function(x = 3)


def my_function(a, b, /, *, c, d):
  print(a + b + c + d)

my_function(5, 6, c = 7, d = 8)


def my_function(*, x):
  print(x)

my_function(3)