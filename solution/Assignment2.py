import math

def is_prime_2(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Test
test_numbers = [11, 14, 23, 35, 17]
for number in test_numbers:
    print(f"Is {number} prime? {is_prime_2(number)}")
