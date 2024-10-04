#   Merge Two Sorted Lists
#   Write a function to merge two sorted lists into one sorted list.


def merge_sorted_lists(list1, list2):
    # Initialize pointers for both lists
    i, j = 0, 0
    merged_list = []  # This will hold the merged result

    # Iterate through both lists
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1  # Move the pointer in list1
        else:
            merged_list.append(list2[j])
            j += 1  # Move the pointer in list2

    # Append remaining elements from list1, if any
    while i < len(list1):
        merged_list.append(list1[i])
        i += 1

    # Append remaining elements from list2, if any
    while j < len(list2):
        merged_list.append(list2[j])
        j += 1

    return merged_list

# Example usage:
list1 = [1, 3, 5]
list2 = [2, 4, 6]
result = merge_sorted_lists(list1, list2)
print(result)  # Output: [1, 2, 3, 4, 5, 6]
