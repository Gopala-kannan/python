# reverse list without built in method

def reverse(list):
    reverse =[]
    for items in list:
        reverse.insert(0, items)
    return reverse

new_list = reverse(["car", "cycle", "bike", "motorcycle", "twowheeler", "automobile", "bus", "truck"])
print(new_list) # this function method 

# simple method

new_list = (["car", "cycle", "bike", "motorcycle", "twowheeler", "automobile", "bus", "truck"])
reverse = new_list[::-1]
print(reverse)


    
