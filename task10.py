
def average_age(person_list):
    age = [age for name, age in person_list]
    return sum(age) / len(person_list)
    
person_list = [("gopal", 21), ("kanna", 22), ("sajith", 20), ("mari", 17)]

print(average_age(person_list)) #function method

# simple method

person_list = [("gopal", 21), ("kanna", 22), ("sajith", 20), ("mari", 17)]
average_age = sum([age for name, age in person_list]) / len(person_list)
print(average_age)
