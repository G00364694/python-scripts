# Francis Adepoju...2018, January  Ex. 1
"""
# This program calculates and displays Fibonacci numbers.(Hard coded number)
# This program calculates the nth Fibonacci number where n the 
# sum of the first and last letters of my first name as numbers. 
# Taking A as the number 1, B as 2, C as 3, and so on. 
# For example, name = Ian, so I should calculate the 25th Fibonacci 
# number because I is 9 and n is 14, giving 25 in total.
# F= 6 and S = 19
"""
def fib(n):
  """This function returns the nth Fibonacci number."""
  i = 0
  j = 1
  n = n - 1

  while n >= 0:
    i, j = j, i + j     # i = j; j = i + j
    n = n - 1
  
  return i

# Test the function with the following value.
x = 32
y = 6 + 19
ans = fib(x)
ans2 = fib(y)
#print("Fibonacci number", x, "is", ans)
print("-------------------------------------------------------")
print("Fibonacci number for FRANCIS, F + S equals:", y, "is", ans2)
print("")




