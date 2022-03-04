# Write a Python function to find the Max of three numbers.
# Sample List : [3, 8, 2]
# Expected Output : 8


def find_max(numbers):
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num


list = [3, 8, 2]
print(find_max(list))