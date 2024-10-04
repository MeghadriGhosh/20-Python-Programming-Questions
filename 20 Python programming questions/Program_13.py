#   Find All Permutations of a String
#   Write a function to generate all permutations of a given string.


#   Method 1: Using Recursion

def permute_string(s):
    # Base case: if the string is empty or has one character
    if len(s) <= 1:
        return [s]

    permutations = []  # List to store all permutations

    for i in range(len(s)):
        # Get the current character and the remaining characters
        current_char = s[i]
        remaining_chars = s[:i] + s[i+1:]  # Exclude the current character

        # Recursively get all permutations of the remaining characters
        for perm in permute_string(remaining_chars):
            permutations.append(current_char + perm)

    return permutations

# Example usage:
string = "abc"
result = permute_string(string)
print(result)  # Output: ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

#   Method 2: Using itertools.permutations

import itertools

def permute_string_itertools(s):
    # Use itertools.permutations to generate permutations
    return [''.join(p) for p in itertools.permutations(s)]

# Example usage:
string = "abc"
result = permute_string_itertools(string)
print(result)  # Output: ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
