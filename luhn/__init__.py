__version__ = '0.1.0'

m = [0, 2, 4, 6, 8, 1, 3, 5, 7, 9]

def digit(msg):
  try:
    digits = list(msg)
    odd_digits = [*map(int, digits[1:][::2])]
    even_digits = [m[int(d)] for d in digits[0:][::2]]
    x = sum(odd_digits) + sum(even_digits)

    x = (10 - x % 10)
    return 0 if x == 10 else x
  except ValueError:
    return -1

def validate(msg):
  return digit(msg) == 0

def generate(msg):
  return msg + str(digit(msg))

