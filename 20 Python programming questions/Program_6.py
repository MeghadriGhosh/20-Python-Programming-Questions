#   Find the Largest and Smallest Element in a List
#   Write a function that finds the largest and smallest element in a list without using built-in functions like min() and max().


def find_largest_and_smallest(lst):
    # Check if the list is empty
    if len(lst) == 0:
        return None, None  # Return None if the list is empty
    
    # Initialize both smallest and largest with the first element of the list
    smallest = largest = lst[0]
    
    # Iterate over the list starting from the second element
    for i in range(1, len(lst)):
        if lst[i] < smallest:
            smallest = lst[i]
        if lst[i] > largest:
            largest = lst[i]
    
    return smallest, largest

# Example usage:
numbers = [3, 1, 4, 1, 5, 9, -2, 6]
smallest, largest = find_largest_and_smallest(numbers)
print(f"Smallest: {smallest}, Largest: {largest}")  # Output: Smallest: -2, Largest: 9
