import math

answered = False
num_of_divisors = 500
triangle_num = 0
row = 0
divisor_count = 1

while answered == False:
    triangle_num += row
    row += 1
    divisor_count_trangle_num = int(triangle_num)

    for i in range(1, int(math.sqrt(divisor_count_trangle_num)), 1):
        if divisor_count_trangle_num % i == 0:
            divisor_count += 1

    if divisor_count*2 > num_of_divisors:
        answered = True
        print(triangle_num)
    else:
        divisor_count = 1
