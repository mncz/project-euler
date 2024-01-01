# Largest Product in a Series

file = open('_008.txt')
number = ''.join([x.strip() for x in file.readlines()])
ans = 0

for i in range(len(number) - 13):
    p = 1

    for n in number[i:i+13]:
        p *= int(n)
    
    ans = max(ans, p)

print(ans)
