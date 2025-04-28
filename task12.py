def unique(str):
    character = set()
    for char in str:
        if char in character:
            return False
        character.add(char)
    return True
str = input("Enter a value :")
print(unique(str))