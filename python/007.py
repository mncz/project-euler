# 10001st Prime

import math

def is_prime(n):
    if n <= 1:
        return False
    
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    
    return True

count, i = 0, 2

while count < 10001:
    if is_prime(i):
        count += 1
    
    i += 1

print(i - 1)
