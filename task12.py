def unique(str):
    character = set()
    for char in str:
        if char in character:
            return False
        character.add(char)
    return True
str = input("Enter a value :")
print(unique(str)) # function method

# simple method

value = input("Enter a value :")
for char in value:
    if value.count(char) > 1:
        print("False")
        break
    else:
        print("True")

# this code is find a unique elements 
# output = gopal = one world not repeat so it is unique element
# output = hello = one world repeact again and again "l l" so it is not unique element
