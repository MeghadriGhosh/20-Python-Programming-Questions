#   Count Occurrences of Each Element in a List
#   Write a function that counts the occurrence of each element in a list.


def count_occurrences(lst):
    count_dict = {}  # Dictionary to store element counts

    # Iterate through each element in the list
    for element in lst:
        if element in count_dict:
            count_dict[element] += 1  # Increment count if element exists
        else:
            count_dict[element] = 1  # Initialize count to 1 for new element

    return count_dict

# Example usage:
input_list = [1, 2, 2, 3, 3, 3, 4]
result = count_occurrences(input_list)
print(result)  # Output: {1: 1, 2: 2, 3: 3, 4: 1}
