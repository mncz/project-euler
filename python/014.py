# Longest Collatz Sequence

seq, num = 0, 1

for i in range(1, 1000000):
    n = i
    s = 1

    while n > 1:
        if n % 2 == 0:
            n /= 2
        else:
            n = 3 * n + 1
        
        s += 1
    
    if max(seq, s) == s:
        seq = s
        num = i

print(num)
