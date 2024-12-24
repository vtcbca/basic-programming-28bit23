def alphabet_pattern_2(n):
    for i in range(1, n + 1):
        # Print leading spaces
        print(" " * (n - i), end="")
        
        # Collect the increasing sequence
        increasing = [chr(64 + j) for j in range(1, i + 1)]
        decreasing = increasing[:-1][::-1]  # Reversed decreasing sequence

        # Combine and print the full row
        row = increasing + decreasing
        print(" ".join(row))
        
# Test
n = 3
alphabet_pattern_2(n)
