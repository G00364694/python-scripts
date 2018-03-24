# # Francis Adepoju. 8 March 2018   Ex. #6
# https://stackoverflow.com/questions/35467303/write-factorial-with-while-loop-python
"""
# Write a Python script containing a function called factorial() that 
# takes a single input/argument which is a positive integer and returns 
# its factorial. The factorial of a number is that number multiplied by 
# all of the positive numbers less than it. For example, 
# the factorial of 5 is 5x4x3x2x1 which equals 120. 
# You should, in your script, test the function by calling it with the 
# values 5, 7, and 10.
"""

def factorial(inNum):
    num = 1
    while inNum >= 1:
        num *= inNum        # num = num * inNum
        inNum = inNum - 1
    # return final result to the caller
    return num              

print(f'The factorial of 5 is:\t {factorial(5)}')  
print(f'The factorial of 7 is:\t {factorial(7)}')
print(f'The factorial of 10 is:\t {factorial(10)}')
