def triangle_pattern_2(n):
    for i in range(1, n + 1):
        # Leading spaces
        print(" " * (n - i), end="")
        # List comprehension to print numbers for this row
        print(" ".join([str(x) for x in range(1, 2 * i)]))

# Test
n = 3
triangle_pattern_2(n)
