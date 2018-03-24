# Francis Adepoju. 7 Feb 2018       Ex. #3
# The Collatz conjecture program
# https://en.wikipedia.org/wiki/Collatz_conjecture
"""
# Python script that starts with an integer and repeatedly applies the Collatz function 
# (divide by 2 if even, multiply by three and 1 if odd) using a while loop and if statement. 
# At each iteration, the current value of the integer should be printed to the screen. 
# You can specify in your code the starting value of 17. 
# If you wish to enhance your program, have the program ask the user for the integer instead of 
# specifying a value at the start of your code. 
"""
# Accept an integer input from the Keyboard
print("*******************************")
intVar = int(input("Please Enter an Integer number: "))   
print("*******************************")
# If (intVar != ord('\t') ): #if null value ids not supplied
while intVar != 1: 
    print("% 3d" % intVar)
    if (intVar % 2 == 0):
        # Even, therefore divide intVar by 2
        intVar = intVar/2                   
    else:
        #Not Even so, multiply by 3 and add 1 to intVar
        intVar = (intVar * 3) + 1           

print ("% 3d" % intVar)                     # End of while loop
print(f'{intVar}')                          # Use the f-string feature of python-3


