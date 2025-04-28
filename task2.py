# palindrome 

text = str(input("Enter a text: ")) # get input value
if text == text[::-1]: # check if the text is equal to its reverse
    print("The text is a palindrome.")
else:
    print("The text is not a palindrome.")

