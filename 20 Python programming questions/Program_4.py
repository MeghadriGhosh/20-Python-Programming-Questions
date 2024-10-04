#   Fibonacci Sequence
#   Write a function to generate the Fibonacci sequence up to n terms.


def fibonacci(n):
    # Handle cases where n is 0 or negative
    if n <= 0:
        return []
    
    # For n = 1, return only the first term [0]
    if n == 1:
        return [0]
    
    # Start with the first two terms of the Fibonacci sequence
    fib_sequence = [0, 1]
    
    # Generate the rest of the sequence up to n terms
    for i in range(2, n):
        next_term = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_term)
    
    return fib_sequence

# Example usage:
n = 10
print(fibonacci(n))  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
