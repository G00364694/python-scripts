# Francis Adepoju, 2018-02-16
#Project Euler problem #1

summ = 0
i = 1

while i < 1000:
    if i % 3 == 0 or i % 5 == 0:
        summ += i
    i += 1
print("Sum of divisible of 3 or 5 les than 1000 equals:  ", summ)

