# Francis Adepoju. 7 Feb 2018
# The Collatz conjecture program
# https://en.wikipedia.org/wiki/Collatz_conjecture

intVar = int(input("Please Enter an Integer number: "))   # Take integer input
#intVar = 12
#if (intVar != ord('\t') ): #if null value ids not supplied
while intVar != 1: 
    print("%3d" %intVar)
    if (intVar % 2 == 0):
        intVar = intVar/2               #divide intVar by 2
    else:
        intVar = (intVar * 3) + 1       #multiply by 3 and add 1 to intVar

print ("%3d" %intVar)                   # End of while loop


