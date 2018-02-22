# Francis Adepoju, 2018-02-14
# the smallest positive number that is evenly divisible by all of the numbers from 1 to 20... Euler problem 5
# 
# ... https://www.w3resource.com/euler-project/euler-problem5.php#
# Given that 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
# 
# The number in question must be divisible by all of the numbers between 1 and 20 (assume inclusive for the ranges).
# As a result, it must be divisible by all of the numbers between 1 and 10. The smallest number that is divisible
# by all the numbers between 1 and 10 (given by Project Euler) is 2520. Thus, the number in question here must be a
# multiple of 2520.

# The program to find this number will start at 2, iterate to 20, and for each of those numbers it will divide by every 
# known prime less than that number (technically any prime less than the square root of the number) to determine their factorization. 
# We will find the numbers that are prime as we go (they won't be divisible by any lesser prime, by definition).

def gcd(x, y):
	#return y and gcd(y, x % y) or x     # Compute the greatest common denominator (gcd) function
  return (y and gcd(y, x % y) or x)

def lcm(x, y):
	return (x * y / gcd(x, y))

smallestInteger = 1
for i in range(1, 21):     # Find the least common multiple of 1 & 20, recursively
	smallestInteger = lcm(smallestInteger, i)
	print("factor found :", smallestInteger)
print("Euclidean Algorithm Implementation yields: ", int(smallestInteger))
