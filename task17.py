def digits(number):
    return sum(int(digit) for digit in str(number) if digit.isdigit())

values = input("Enter a number : ")
print("sum of digits : ", digits(values)) # function method

# simple method
values = input("Enter a number : ")
sum = 0
for i in values:
    if i.isdigit():
        sum += int(i)
print("sum of digits :", sum)

# output = input_value = 526 = running 5+2+6 = 13 
# output = so the digits value is 13
