# Find Keys with Maximum Value

def maximum_dict(price):
    maximum_price = max(price.values())
    max_items = [key for key, value in price.items() if value == maximum_price]
    print(max_items)

shops = {
        "books" : 356,
        "notes" : 200,
        "pen"   : 15,
        "pencle": 10,
        "scale" : 20
}

maximum_dict(shops)   #function method

# simple method

shops = {
        "books" : 356,
        "notes" : 200,
        "pen"   : 15,
        "pencle": 10,
        "scale" : 20
}

print(max(shops, key=shops.get)) # highlest value
print(min(shops, key=shops.get)) # smallest value
