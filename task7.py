#  comman elements

def common_elements(list1, list2):
    common= []
    for i in list1:
        if i in list2:
            common.append(i)
    return common
list1 = input("Enter the first list: ").split()
list2 = input("Enter the second list: ").split()
print("the common elements is : ", common_elements(list1, list2)) #function method

# simple method
list_1 = input("Enter the first list : ")
list_2 = input("Enter the second list : ")
common = [i for i in list_1 if i in list_2]
print(common)
