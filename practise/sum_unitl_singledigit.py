def sum_of_digits(n):
    while n > 9:
        print(n)
        n = sum(int(digit) for digit in str(n))
    return n

# Test the function
print(sum_of_digits(12345))  # Output: 6