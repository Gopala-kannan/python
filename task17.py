def digits(number):
    return sum(int(digit) for digit in str(number) if digit.isdigit())

values = input("Enter a number : ")
print("sum of digits : ", digits(values))