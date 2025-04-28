my_list = list(input("Enter letters: "))
upper_case = [i.upper() for i in my_list]

for i in my_list:
    if i.isalpha():
        print(i.upper(), end=" ")
print(" = ",upper_case)