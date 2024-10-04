#   Remove Duplicates from a List
#   Write a function to remove duplicates from a list while maintaining order.


def remove_duplicates(lst):
    seen = set()  # Set to track seen elements
    result = []   # List to store the results

    for item in lst:
        if item not in seen:
            seen.add(item)  # Add item to seen set
            result.append(item)  # Append to result if it's the first occurrence
    
    return result

# Example usage:
input_list = [1, 2, 3, 2, 4, 1, 5, 3, 6]
output_list = remove_duplicates(input_list)
print(output_list)  # Output: [1, 2, 3, 4, 5, 6]
