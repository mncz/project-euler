# Large Sum

with open("_013.txt", "r") as file:
    numbers = [int(x) for x in file.readlines()]

sum = sum(numbers)

print(sum // 10 ** (len(str(sum)) - 10))
