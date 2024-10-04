#   Check if a String is Palindrome
#   Write a function to check if a given string is a palindrome.


def is_palindrome(s):
    # Initialize two pointers: one at the start and one at the end of the string
    start = 0
    end = len(s) - 1
    
    # Compare characters from the start and end, moving towards the center
    while start < end:
        if s[start] != s[end]:
            return False
        start += 1
        end -= 1
    
    return True

# Example usage:
s = "racecar"
print(is_palindrome(s))  # Output: True

s = "hello"
print(is_palindrome(s))  # Output: False
