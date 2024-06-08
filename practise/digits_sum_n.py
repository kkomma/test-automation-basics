def smallest_sumwrong(n):
    if n == 0:
        return 0
    if n < 9:
        return n
    digits = []
    for i in range(9, 0, -1):
        while n >= i:
            digits.append(i)
            n -= i
    print(digits)
    v = int(''.join(map(str, digits)))
    print(v)
    return 

def smallest_sum(n):
    result = 0
    for i in range(9, 0, -1):
        while n >= i:
            n -= i
            result = result * 10 + i
    print(result)
    return result


def smallest_number_with_sum(n):
    if n == 0:
        return 0    
    digits = []    
    for digit in range(9, 0, -1):
        while n >= digit:
            print('--',n, digit)
            digits.append(digit)
            print('==',digits)
            n -= digit    
    digits.reverse()    
    smallest_number = int(''.join(map(str, digits)))    
    return smallest_number


# Test cases
print(smallest_number_with_sum(16))  # Output: 79
print(smallest_number_with_sum(19))  # Output: 199
print(smallest_number_with_sum(7))   # Output: 7
print(smallest_number_with_sum(0))   # Output: 0 (if n is 0, the smallest number is 0)
print('op::',smallest_number_with_sum(50))


