#   Find the Factorial of a Number
#   Implement a recursive and an iterative solution to compute the factorial of a number.


#   1. recursive solution:

def factorial_recursive(n):
    # Base case: factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1
    else:
        # Recursive case: n * factorial of (n-1)
        return n * factorial_recursive(n - 1)

# Example usage:
n = 5
print(factorial_recursive(n))  # Output: 120

#   2. iterative solution:

def factorial_iterative(n):
    result = 1
    for i in range(2, n + 1):  # Start loop from 2 to n
        result *= i
    return result

# Example usage:
n = 5
print(factorial_iterative(n))  # Output: 120
