# Multiples of 3 and 5

# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

sum_of_multiples_3_5 = 0
num = 0
while num < 1000:
    if num % 3 == 0 or num % 5 == 0:
        sum_of_multiples_3_5 += num
    num += 1
print(sum_of_multiples_3_5)