# Problem 3. Largest Prime Factor

def find_largest_prime_factor(n=600_851_475_143):
    x = int(n ** 0.5)
    for i in range(x, 1, -1):
        if n % i == 0:
            if is_prime(i):
                return i
    return n

def is_prime(n):
    x = int(n ** 0.5)
    for i in range(x, 1, -1):
        if n % i == 0:
            return False
    return True

find_largest_prime_factor() # 6857
