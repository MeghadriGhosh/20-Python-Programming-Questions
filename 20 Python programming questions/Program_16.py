#   Binary Search Implementation
#   Implement a binary search algorithm to find the position of a target value in a sorted list.


def binary_search(sorted_list, target):
    left, right = 0, len(sorted_list) - 1  # Initialize left and right pointers

    while left <= right:
        mid = (left + right) // 2  # Find the middle index

        # Check if the target is present at mid
        if sorted_list[mid] == target:
            return mid  # Target found, return its index
        # If the target is greater, ignore the left half
        elif sorted_list[mid] < target:
            left = mid + 1
        # If the target is smaller, ignore the right half
        else:
            right = mid - 1

    return -1  # Target not found

# Example usage:
sorted_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 6
result = binary_search(sorted_list, target)
print(result)  # Output: 5 (index of the target)
