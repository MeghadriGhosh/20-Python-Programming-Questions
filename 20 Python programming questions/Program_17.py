#   Find the Missing Number in an Array
#   Given an array containing n-1 numbers taken from 1 to n, find the missing number.


def find_missing_number(arr):
    n = len(arr) + 1  # Since the array contains n-1 numbers
    expected_sum = n * (n + 1) // 2  # Calculate the expected sum
    actual_sum = sum(arr)  # Calculate the actual sum of the array
    missing_number = expected_sum - actual_sum  # Find the missing number
    return missing_number

# Example usage:
array = [1, 2, 4, 5]  # Missing number is 3
result = find_missing_number(array)
print(result)  # Output: 3
