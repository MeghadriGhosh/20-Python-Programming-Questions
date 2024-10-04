#   Maximum Subarray Sum (Kadane’s Algorithm)
#   Write a function to find the maximum sum of a contiguous subarray using Kadane’s algorithm.


def max_subarray_sum(arr):
    max_current = arr[0]  # Initialize max_current to the first element
    max_global = arr[0]   # Initialize max_global to the first element

    for i in range(1, len(arr)):
        max_current = max(arr[i], max_current + arr[i])  # Update max_current
        if max_current > max_global:
            max_global = max_current  # Update max_global if needed

    return max_global

# Example usage:
array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
result = max_subarray_sum(array)
print(result)  # Output: 6 (the subarray [4, -1, 2, 1] has the maximum sum)
