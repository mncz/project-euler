# Factorial Digit Sum

import math

print(sum([int(x) for x in str(math.prod([i for i in range(1, 101)]))]))
