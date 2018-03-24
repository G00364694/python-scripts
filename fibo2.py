# Author Francis Adepoju  Ex. 2
# A program that displays Fibonacci numbers using people's names.
"""
# This program calculates and displays Fibonacci numbers.(Numbers generated with the ord function)
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
    i, j = j, i + j
    n = n - 1
  
  return i

#name = "McLoughlin"
name = "Adepoju"
first = name[0]
last = name[-1]
# The ord builtin function returns the ASCII number equivalent of the argument passed into it.
firstno = ord(first)
lastno = ord(last)
x = firstno + lastno

ans = fib(x)
print("")
print("My surname is", name)
print("The first letter", first, "is number", firstno)
print("The last letter", last, "is number", lastno)
print("")
# Concatenating Number with String. Number must be cast to string, ie. str(x)
print("Therefore, Fibonacci number of (" + first + " +  " + last + ") = " + str(x) + " is: ", ans)
