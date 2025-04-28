# * first *
for i in range(5):
    print('*' * i)

rows = 5
for i in range(rows, 0, -1): 
    print('*' * i)

# * secound *

num = 1

for i in range(1, 5):
    for j in range(i):
        print(num, end="")
        num += 1
    print()
    
# * third *

row = 4
for i in range(0, row + 1):
    for space in range(row - i):
        print(" ", end=" ")
    for star in range(2 * i + 1):
        print("*", end=" ")
    print()

# * fourth *

for i in range(6, 0, -1):
    for j in range(i , 7):
        print(j, end="")
    print()