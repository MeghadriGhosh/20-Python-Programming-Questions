#   Check if Two Strings are Anagrams
#   Write a function to determine if two strings are anagrams of each other.


#   Method 1: Using Sorting

def are_anagrams(str1, str2):
    # Normalize the strings by converting to lowercase and removing spaces
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # Sort the characters and compare
    return sorted(str1) == sorted(str2)

# Example usage:
string1 = "listen"
string2 = "silent"
result = are_anagrams(string1, string2)
print(result)  # Output: True

#   Method 2: Using collections.Counter

from collections import Counter

def are_anagrams(str1, str2):
    # Normalize the strings by converting to lowercase and removing spaces
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # Compare character counts
    return Counter(str1) == Counter(str2)

# Example usage:
string1 = "listen"
string2 = "silent"
result = are_anagrams(string1, string2)
print(result)  # Output: True
