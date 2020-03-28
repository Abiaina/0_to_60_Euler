import math

n = 1000
natual_squares = []
answered = False

for num in range(1, n, 1):
    if answered:
        break
    for i in range(1, n - num, 1):
        if answered:
            break
        ii = n - num - i
        if ii ** 2 == num ** 2 + i ** 2:
            answered = True
            print(ii*num*i)
            break