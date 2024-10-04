#   Sum of Digits of an Integer
#   Write a function that takes an integer and returns the sum of its digits.


def sum_of_digits(n):
    # Convert to absolute value to handle negative numbers
    n = abs(n)
    
    # Convert the number to a string and sum the digits
    digit_sum = sum(int(digit) for digit in str(n))
    
    return digit_sum

# Example usage:
number = -12345
result = sum_of_digits(number)
print(f"The sum of the digits of {number} is: {result}")  # Output: The sum of the digits of -12345 is: 15
