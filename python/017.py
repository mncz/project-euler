# Number Letter Counts

from num2words import num2words

print(sum([len(num2words(x).replace(" ", "").replace("-", "")) for x in range(1, 1001)]))
