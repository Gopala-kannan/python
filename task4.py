# average of numbers in a list
numbers = input("Enter the numbers separated by space: ").split()
numbers = [int(items) for items in numbers] # then change the string to int
average = sum(numbers) / len(numbers)
print("The average is:", average)
print("The sum is:", sum(numbers))

