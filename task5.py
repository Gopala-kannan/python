# reverse list without built in method

def reverse(list):
    reverse =[]
    for items in list:
        reverse.insert(0, items)
    return reverse

new_list = reverse(["car", "cycle", "bike", "motorcycle", "twowheeler", "automobile", "bus", "truck"])
print(new_list)
    
