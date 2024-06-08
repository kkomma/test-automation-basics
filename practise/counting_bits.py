
def count_bits(n):
        res = 0
        while n:
            n = n & n - 1
            res += 1
        return res
c = 0
a = []
for i in range(6):    
    a.append(count_bits(i))
print(a)

def is_power_of_two(n):
    return n & n - 1 == 0

def is_divisible_by_two(n):
    return n & (n-1)//2 == 0

print(is_power_of_two(4))
print(is_power_of_two(3))
print(is_divisible_by_two(4))
print(is_divisible_by_two(7))


