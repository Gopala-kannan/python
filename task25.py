char = input("Enter a charaters :").split()

for i in char:
    count = char.count(i)
    print(f"'{i}' charaters {count} times")
print(f"Total characters: {len(''.join(char))}")
    