# Problem 2. Even Fibonacci Numbers

def sum_even_fibo(n=4_000_000):
    s = 2
    crr, nxt = 1, 2
    while nxt < n:
        crr, nxt = nxt, crr + nxt
        if nxt % 2 == 0:
            s += nxt
    return s

sum_even_fibo() # 4613732
