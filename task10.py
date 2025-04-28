
def average_age(person_list):
    age = [age for name, age in person_list]
    return sum(age) / len(person_list)
    
person_list = [("gopal", 21), ("kanna", 22), ("sajith", 20), ("mari", 17)]

print(average_age(person_list))


