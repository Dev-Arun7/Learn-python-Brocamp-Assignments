def sum_numbers(*args):
    total = sum(args)
    return total

input_values = input("Enter numbers separated by commas: ")
values = [float(value.strip()) for value in input_values.split(',')]

result = sum_numbers(*values)
print("Sum of the entered values:", result)
