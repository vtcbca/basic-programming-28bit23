def is_palindrome_2(s):
    s = s.replace(" ", "").lower()  # Remove spaces and convert to lowercase
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

# Test
input_string = "A man a plan a canal Panama"
print(f"Is palindrome? {is_palindrome_2(input_string)}")
