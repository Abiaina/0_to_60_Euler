
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


n = 20

# Checks if new dividend is divisible by every element in range (from 1 to max_num)
def divisible_by_all_check(max_num, dividend):
    dividend_to_entire_list = True
    for i in range(1, max_num, 1):
        if dividend % i != 0:
            dividend_to_entire_list = False
    return dividend_to_entire_list   
    
dividend = n
smallest_dividend = -1
while smallest_dividend < 0:
    if divisible_by_all_check(n, dividend):
        smallest_dividend = dividend
    dividend += n 
    
print(smallest_dividend)