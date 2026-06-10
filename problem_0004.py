# Problem 4. Largest Palindrome Product

def find_largest_palindrome(n=999):
    m = 0
    for i in range(n, -1, -1):
        for j in range(n, i-1, -1):
            x = i * j
            if is_palindrome(str(x)):
                m = max(m, x)
    return m

def is_palindrome(a):
    return a == a[::-1]

find_largest_palindrome() # 906609
