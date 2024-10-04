#   Count Vowels and Consonants in a String
#   Write a program to count the number of vowels and consonants in a given string.


def count_vowels_and_consonants(s):
    # Define the set of vowels
    vowels = set("aeiouAEIOU")
    
    # Initialize counters for vowels and consonants
    vowel_count = 0
    consonant_count = 0
    
    # Iterate over each character in the string
    for char in s:
        # Check if the character is a letter
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
    
    return vowel_count, consonant_count

# Example usage:
s = "Hello World!"
vowels, consonants = count_vowels_and_consonants(s)
print(f"Vowels: {vowels}, Consonants: {consonants}")  # Output: Vowels: 3, Consonants: 7
