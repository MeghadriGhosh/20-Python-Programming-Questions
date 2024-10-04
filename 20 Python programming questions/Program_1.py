#   Reverse a String
#   Write a function to reverse a string without using built-in methods.


def reverse_string(s):
    # Convert the string to a list since strings are immutable
    char_list = list(s)
    
    # Initialize two pointers, one at the beginning and one at the end
    start = 0
    end = len(char_list) - 1
    
    # Swap characters from the start and end, moving towards the middle
    while start < end:
        char_list[start], char_list[end] = char_list[end], char_list[start]
        start += 1
        end -= 1
    
    # Convert the list back to a string
    return ''.join(char_list)

# Example usage:
s = "hello"
print(reverse_string(s))  # Output: "olleh"
