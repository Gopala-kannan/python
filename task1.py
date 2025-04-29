# count a vowels and consonants in a string

value = str(input("Enter a value : ")) # get input value
def count(value): # use function to count vowels and consonants
    vowel_words = "aeiouAEIOU" # vowels letters
    vowels = 0
    consonants = 0
    for i in value:
        if i.isalpha(): # check all characters 
            if i in vowel_words:
                vowels += 1
            else:
                consonants += 1
    return vowels, consonants

vowels, consonants = count(value)
print("your input :", value)
print("Number of vowels:", vowels)
print("Number of consonants:", consonants) # this is function method


# simple method

vowels_words = "aeiouAEIOU"
value_input = input("Enter a value : ")
vowels, constants = 0, 0
for i in value_input:
    if i.isalpha():
        if i in vowel_words:
            vowels += 1
        else:
            constants += 1
print("Number of vowels: ", vowels)
print("Number of constants : ", constants)
