def print_positive_numbers(start, end):
    for num in range(start, end + 1):
        if num > 0:
            print(num)

# Input the range
start_range = int(input("Enter the starting number of the range: "))
end_range = int(input("Enter the ending number of the range: "))

if start_range > end_range:
    print("Invalid range. Starting number should be less than or equal to the ending number.")
else:
    print("Positive numbers in the range:")
    print_positive_numbers(start_range, end_range)
