def reverse_string_2(s):
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str  # Add each character in front
    return reversed_str

# Test
input_string = "Hello, World!"
print(f"Reversed string: {reverse_string_2(input_string)}")
