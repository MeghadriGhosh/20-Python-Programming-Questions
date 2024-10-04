#   Flatten a Nested List
#   Write a function to flatten a list that may contain nested lists.


def flatten(nested_list):
    flat_list = []  # List to store the flattened result

    for element in nested_list:
        if isinstance(element, list):  # Check if the element is a list
            flat_list.extend(flatten(element))  # Recursively flatten and extend the flat_list
        else:
            flat_list.append(element)  # Append non-list elements to flat_list

    return flat_list

# Example usage:
nested_list = [1, [2, 3], [4, [5, 6]], 7]
result = flatten(nested_list)
print(result)  # Output: [1, 2, 3, 4, 5, 6, 7]
