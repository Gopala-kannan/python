# remove duplicate for list

def remove_duplicate(list):
    input_list = input("Enter the numbers separated by space: ").split()
    input_list = [int(items) for items in input_list]
    unique_list = []
    for items in input_list:
        if items not in unique_list:
            unique_list.append(items)
    return unique_list
print(remove_duplicate([])) #function method

# simple method
list_input = input("Enter a Number: ")
unique_list = list(set(list_input))
print(unique_list)
