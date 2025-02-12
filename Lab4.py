#Matthew Goldstein

'''
Function 1: Fibonacci Numbers

Background

The Fibonacci numbers are a sequence of numbers where each number is the sum of the two numbers that appear before it. The sequence starts with 0 and 1. The first 20 numbers are as follows:

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181

Assignment

Your task is to define a function named “fibonacci” that takes an integer and returns the Fibonacci number at that position in the sequence. The number in the first position is 0. You can assume that the parameters to the function will be positive integers. You may not use a direct mathematical formula to find the Nth Fibonacci number.

Examples

You can test your function’s correctness by checking that all the cases below are true:
fibonacci(1) == 0
fibonacci(2) == 1
fibonacci(3) == 1
fibonacci(6) == 5
fibonacci(25) == 46368
'''


def fibonacci(n):
    """Returns the nth Fibonacci number (0-indexed)."""
    if n <= 0:
        return "Input must be a positive integer"

    # Starting values for Fibonacci sequence
    a, b = 0, 1

    # Calculate Fibonacci number at position n
    for _ in range(1, n):
        a, b = b, a + b

    return a


# User input
user_input = int(input("Enter a positive integer to find the Fibonacci number at that position: "))

# Display the result
result = fibonacci(user_input)
print(f"The Fibonacci number at position {user_input} is: {result}")

'''
Function 2: Prime Numbers 

Background

A prime number is an integer greater than one that is only divisible by 1 and itself. You can check if N is divisible by M with the statement N % M == .0. Examples of prime numbers are 2, 3, 11, and 29. Examples of non-prime numbers are 6, 8, and 9. 6 and 8 are divisible by 2. 9 and 6 are divisible by 3.

Assignment

Your task is to define a function named “is_prime” that takes an integer as a parameter and returns True if the number is prime, and False if the number is not prime. You can assume that the parameters to the function will be integers, but they may be negative.

Examples

You can test your function’s correctness by checking that all the cases below are true:
is_prime(2) == True
is_prime(11) == True
is_prime(1741) == True
is_prime(1) == False
is_prime(9) == False
is_prime(-2) == False
'''


def is_prime(n):
    """Returns True if n is a prime number, otherwise returns False."""

    # Prime numbers are greater than 1
    if n <= 1:
        return False

    # Check divisibility from 2 to the square root of n
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False  # Found a divisor, so n is not prime

    return True  # No divisors found, n is prime


# Get user input and check if the number is prime
try:
    n = int(input("Enter a number to check if it's prime: "))
    if is_prime(n):
        print(f"{n} is a prime number.")
    else:
        print(f"{n} is not a prime number.")
except ValueError:
    print("Invalid input. Please enter an integer.")

'''Function 3: Prime Factorization

Background

All positive integers greater than 1 can be expressed as the product of a unique combination of prime numbers. This combination of prime numbers is referred to as the number’s prime factorization. For example, the number 30 can be expressed as 2 * 3 * 5. The prime factorization for a prime number is just itself.

Assignment

Your assignment is to write a function named “print_prime_factors” that will take an integer as its parameter and calculate the integer’s prime factorization. While the first two functions returned their results, this function will instead print the result and return nothing. The output should be in the format: parameter = factor1 * factor2 * factor3. Note that a prime may appear more than once in the prime factorization, and the factors should be printed in order of least to greatest. You can assume that the inputs to the function will be positive integers greater than 1.


Examples

Here is a sample program for testing your function:

print_prime_factors(10)
print_prime_factors(2)
print_prime_factors(24)
print_prime_factors(2475)
print_prime_factors(23)

This should print out the following:
10 = 2 * 5
2 = 2
24 = 2 * 2 * 2 * 3
2475 = 3 * 3 * 5 * 5 * 11
23 = 23
'''

def print_prime_factors(n):
    """Prints the prime factorization of the given number."""

    factors = []

    # Start by dividing by 2 (smallest prime)
    while n % 2 == 0:
        factors.append(2)
        n //= 2

    # Now check for odd factors starting from 3
    divisor = 3
    while divisor * divisor <= n:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 2

    # If n is prime and greater than 2, it will remain
    if n > 2:
        factors.append(n)

    # Print the result in the desired format
    print(f"{int(factors[0])} = {' * '.join(map(str, factors))}")


# Get user input and output the prime factors
try:
    n = int(input("Enter a number to find its prime factors: "))
    print_prime_factors(n)
except ValueError:
    print("Invalid input. Please enter a positive integer greater than 1.")
