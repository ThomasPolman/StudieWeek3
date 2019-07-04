def sum_recursion(n):
  if n == 1:
    return n
  else:
    return n + sum_to_one(n-1)

def factorial_recursion(n):
  if n < 2:
    return 1
  else:
    return n * factorial(n-1)
