# Smallest Multiple

def is_divisible(n):
    for i in range(1, 21):
        if n % i != 0:
            return False
    
    return True

i = 38

while True:
    if is_divisible(i):
        break

    i += 19

print(i)
