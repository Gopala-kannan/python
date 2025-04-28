palindrome_num = int(input("Enter a number : "))

if str(palindrome_num) == str(palindrome_num)[::-1]:
    print(palindrome_num, "Palindrome")
else:
    print(palindrome_num, "Not Palindrome")
