# Counting Sundays

from datetime import date, timedelta

def date_range(start, end):
    for n in range(int((end - start).days)):
        yield start + timedelta(n)

start = date(1901, 1, 1)
end = date(2000, 12, 31)
count = 0

for d in date_range(start, end):
    if d.strftime("%A") == "Sunday" and d.strftime("%-d") == "1":
        count += 1

print(count)
