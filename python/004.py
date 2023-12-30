# Largest Palindrome Product

def is_palindrome(n):
    n = str(n)
    m = len(n) // 2

    if n[0:m] == n[::-1][0:m]:
        return True
    else:
        return False

ans = 0

for i in range(100, 1000):
    for j in range(100, 1000):
        p = i * j

        if is_palindrome(p):
            ans = max(ans, p)

print(ans)
