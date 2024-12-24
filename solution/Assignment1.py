def factorial_2(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_2(n - 1)

# Test
n = 5
print(f"Factorial of {n} is: {factorial_2(n)}")
