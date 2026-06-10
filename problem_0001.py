# Problem 1. Multiples of 3 or 5

def find_multiples(n=1000):
    s = 0
    for i in range(n):
        if i % 3 == 0 or i % 5 == 0:
            s += i
    return s

find_multiples() # 233168
