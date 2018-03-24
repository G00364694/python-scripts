#Francis Adepoju, 2018-02-14
# Sum of numbers multiples of 3 or 5... Euler problem 1
# https://projecteuler.net/problem=1

summ = 0
cnt = 1

while cnt < 1000:
    if cnt % 3 == 0 or cnt % 5 == 0:
        summ += cnt # Add thje next multiple of 3 or 5
    cnt += 1        # increment the cnt variable
print("Sum of the 3 or 5 multiples, less than 1000 is: ", summ)
print("Repeat...Sum of the 3 or 5 multiples, less than 1000 is: ", summ)




