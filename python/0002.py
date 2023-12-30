# Even Fibonacci Numbers

a, b, c = 1, 2, 0
f = [b]

while c < 4000000:
    c = a + b
    a, b = b, c

    if c % 2 == 0:
        f.append(c)

print(sum(f))
