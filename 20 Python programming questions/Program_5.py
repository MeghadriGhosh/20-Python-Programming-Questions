#   Check Prime Number
#   Write a function to check whether a number is prime or not.


import math

def is_prime(n):
    # Check if n is less than or equal to 1
    if n <= 1:
        return False
    
    # 2 and 3 are prime numbers
    if n <= 3:
        return True
    
    # Eliminate numbers divisible by 2 or 3
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    # Check divisibility from 5 to sqrt(n) with step 6
    # Numbers that are divisible by 2 or 3 have already been excluded
    for i in range(5, int(math.sqrt(n)) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    
    return True

# Example usage:
n = 29
print(is_prime(n))  # Output: True

n = 10
print(is_prime(n))  # Output: False
