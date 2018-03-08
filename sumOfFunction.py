def sumAll(upto):
    sumUpTo = 0
    for i in range(1, upto + 1):
        sumUpTo += i
    return sumUpTo

print("The sum of values from 1 to 10 inclusive is :", sumAll(10))
print("The sum of values from 1 to 100 inclusive is :", sumAll(100))
print("The sum of values from 1 to 1000 inclusive is :", sumAll(1000))

    