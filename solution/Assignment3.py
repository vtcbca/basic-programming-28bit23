def fibonacci_2(max_value):
    fib_sequence = []
    a, b = 0, 1
    while a <= max_value:
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

# Test
max_val = 50
print(f"Fibonacci sequence up to {max_val}: {fibonacci_2(max_val)}")
