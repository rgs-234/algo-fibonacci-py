
# Recursive solution
# def fibonacci(n):
#   if n <= 1:
#     return n
#   else:
#     return fibonacci(n - 1) + fibonacci(n - 2)
    


# Non-recursive solution
def fibonacci(n):
  num1 = 0
  num2 = 1

  for num in range(n):
    temp = num2
    num2 = num1 + num2
    num1 = temp

  return num1