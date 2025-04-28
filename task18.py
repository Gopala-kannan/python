# Fibonacci

count = []
a, b = 0, 1
for _ in range(12):
    count.append(a)
    a, b = b, a +b
print(count)
