#   Two Sum Problem
#   Given an array of integers, find two numbers that add up to a specific target number.


def two_sum(nums, target):
    num_dict = {}  # Dictionary to store numbers and their indices

    for index, num in enumerate(nums):
        complement = target - num  # Calculate the complement

        # Check if the complement exists in the dictionary
        if complement in num_dict:
            return [num_dict[complement], index]  # Return the indices of the two numbers

        # Store the number and its index in the dictionary
        num_dict[num] = index

    return None  # Return None if no solution exists

# Example usage:
nums = [2, 7, 11, 15]
target = 9
result = two_sum(nums, target)
print(result)  # Output: [0, 1]
