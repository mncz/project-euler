# 1000-digit Fibonacci Number

fibonacci = [1, 1]
index = 2

while len(str(fibonacci[1])) < 1000:
    fibonacci[0], fibonacci[1] = fibonacci[1], fibonacci[0] + fibonacci[1]
    index += 1

print(index)
