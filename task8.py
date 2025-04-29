def element_count(list, elements):
    return list.count(elements)

my_list = input("Enter a list of elements separated by spaces: ").split()
element_name = input("Enter the element to count: ")
count = element_count(my_list, element_name)
print("The appears : ", element_name)
print("times :", count) #function method

# simple method

my_list = input("Enter a list of elements separated by spaces :")
element = input("Enter a element to count :")
count = my_list.count(element)
print("count :", count)
