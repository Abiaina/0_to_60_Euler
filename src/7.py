import math

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?
n = 10001
prime_count = 0
nth_prime_num = -1
def prime_num_check(num):
    is_prime_num = True
    if num == 2:
        return is_prime_num
    for i in range(2, num, 1):
        # print(num % i)
        if num % i == 0:
            return False
    return is_prime_num
ii = 2
while prime_count < n:
    if prime_num_check(ii):
        # print(ii)
        nth_prime_num = ii
        prime_count += 1
    ii += 1

print(nth_prime_num)