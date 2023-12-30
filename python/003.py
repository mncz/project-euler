# Largest Prime Factor

import math

def is_prime(n):
    if n <= 1:
        return False
    
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    
    return True

x, f = 600851475143, 2

while x > 1:
    if not is_prime(f):
        f += 1
        continue

    if x % f == 0:
        x //= f
    else:
        f += 1

print(f)
