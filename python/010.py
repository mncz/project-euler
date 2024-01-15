# Summation of Primes

import math

def is_prime(n):
    if n <= 1:
        return False
    
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    
    return True

print(sum([i for i in range(1, 2000000) if is_prime(i)]))
