def count_tuples(tuple, elements):
    return tuple.count(elements)

get_tuple =input("Enter a tuple of elements separated by spaces: ")
element_name = input("Enter the element to count: ")
count = count_tuples(get_tuple, element_name)
print("The appears : ", element_name)
print("times :", count) #function method

# simple method

tuple_input =input("Enter a tuple of element : ")
element = input("Enter the element to count : ")
count = tuple_input.count(element)
