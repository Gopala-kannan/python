unquie_list = [1, 3, 4, 5, 9, 8, 4, 5, 7, 1, 6]
unquie_elements = []

for i in unquie_list:
    if i not in unquie_elements:
        unquie_elements.append(i)
print(unquie_elements)