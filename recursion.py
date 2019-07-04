def sum_to_one(n):
  if n == 1:
    return n
  else:
    print("Recursing with input: %s"%(n))
    return n + sum_to_one(n-1)

print(sum_to_one(7))
