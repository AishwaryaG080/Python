from functools import reduce

input_str = input("Enter numbers: ")

numbers = list(map(int, input_str.split()))

filtered_numbers = list(filter(lambda x: 70 <= x <= 90, numbers))
print("List after filter =", filtered_numbers)

mapped_numbers = list(map(lambda x: x + 10, filtered_numbers))
print("List after map =", mapped_numbers)

if mapped_numbers: 
    product = reduce(lambda x, y: x * y, mapped_numbers)
    print("Output of reduce =", product)
