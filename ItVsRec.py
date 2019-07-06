#Iteration
def factorial(n):
  result = 1
  while n != 0:
    result = result*n
    n = n-1
  return result

#Recursion
def factorial(n):  
  if n < 0:    
    ValueError("Inputs 0 or greater only") 
  if n <= 1:    
    return 1  
  return n * factorial(n - 1)

#Iteration
def fibonacci(n):
  fibo = [0, 1]
  if n <= len(fibo)-1:
    return fibo[n]
  else:
    while n > len(fibo)-1:
      next_fibo = fibo[-1] + fibo[-2]
      fibo.append(next_fibo)
  return fibo[n]

#Recursion
def fibonacci(n):
  if n < 0:
    ValueError("Input 0 or greater only!")
  if n <= 1:
    return n
  return fibonacci(n - 1) + fibonacci(n - 2)

#Iteration
def sum_digits(n):
  if n < 0:
    ValueError("Inputs 0 or greater only!")
  result = 0
  while n is not 0:
    result += n % 10
    n = n // 10
  return result + n

#Recursion
def sum_digits(n):
  if n < 10:
    return n
  else:
    result = n % 10
    n = n // 10
    return result + sum_digits(n)

#Iteration
def find_min(my_list):
  min = None
  for element in my_list:
    if not min or (element < min):
      min = element
  return min

#Recursion
def find_min(my_list, min=None):
  if not my_list:
    return min
  else:
    if min == None or my_list[0] < min:
      min = my_list[0] 
  return find_min(my_list[1:], min)

#Quadratic iteration
def is_palindrome(my_string):
  while len(my_string) > 1:
    if my_string[0] != my_string[-1]:
      return False
    my_string = my_string[1:-1]
  return True

#Linear iteration
def is_palindrome(my_string):
  string_length = len(my_string)
  middle_index = string_length // 2
  for index in range(0, middle_index):
    opposite_character_index = string_length - index - 1
    if my_string[index] != my_string[opposite_character_index]:
      return False  
  return True

#Recursion
def is_palindrome(n):
  print(n)
  if len(n) == 0 or len(n) == 1:
    return True
  if n[0] == n[-1] and len(n) > 3:
    return is_palindrome(n[1:-1])
  else:
    if n[0] == n[-1]:
      return True
print(is_palindrome("parterretrap"))

#Iteration; multiply without *
def multiplication(num_1, num_2):
  result = 0
  for count in range(0, num_2):
    result += num_1
  return result

#Recursion
def multiplication(num1, num2):
  print(num1)
  if num2 == 0 or num1 == 0:
    return 0
  return num1 + multiplication(num1, num2-1)

#Iteration on counting levels of treenode structure
def depth(tree):
  result = 0
  queue = [tree]
  while queue:
    level_count = len(queue)
    for child_count in range(0, level_count):
      child = queue.pop(0)
      if child["left_child"]:
        queue.append(child["left_child"])
      if child["right_child"]:
        queue.append(child["right_child"])
    result += 1
  return result

#Recursion
def depth(tree):
  if not tree:
    return 0
  
  left_depth = depth(tree["left_child"])
  right_depth = depth(tree["right_child"])
  
  if left_depth > right_depth:
    return left_depth + 1
  else:
    return right_depth + 1
  
def build_bst(my_list):
  if len(my_list) == 0:
    return None

  mid_idx = len(my_list) // 2
  mid_val = my_list[mid_idx]

  tree_node = {"data": mid_val}
  tree_node["left_child"] = build_bst(my_list[ : mid_idx])
  tree_node["right_child"] = build_bst(my_list[mid_idx + 1 : ])

  return tree_node

tree_level_1 = build_bst([1])
tree_level_2 = build_bst([1, 2, 3])
tree_level_4 = build_bst([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]) 
  
