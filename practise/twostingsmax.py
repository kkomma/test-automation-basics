def largest_number_counting_sort(s1, s2):
    # Function to count the frequency of each digit
    def count_digits(string):
        count = [0] * 10
        for digit in string:
            count[int(digit)] += 1
        return count
    
    # Count the frequency of each digit in s1 and s2
    count_s1 = count_digits(s1)
    count_s2 = count_digits(s2)
    
    # Construct the largest number for both s1 and s2 using Counting Sort logic
    def construct_largest(count):
        largest = ""
        for digit in range(9, -1, -1):  # From 9 to 0 in descending order
            print(f'largest and current dight {digit} {str(digit)} {count[digit]} ',largest)
            largest += str(digit) * count[digit]
        return largest
    
    largest_s1 = construct_largest(count_s1)
    largest_s2 = construct_largest(count_s2)
    
    # Convert the constructed strings to integers
    num_s1 = int(largest_s1)
    num_s2 = int(largest_s2)
    
    # Compare the numbers
    if num_s1 > num_s2:
        return s1
    elif num_s2 > num_s1:
        return s2
    else:
        return "Both numbers are equal"

# Test the function
s1 = "1234"
s2 = "321"
from collections import defaultdict
b = defaultdict()
for s in s1:
    if s in b.keys():
        b[s] = b[s] + 1
    else:
        b[s] = 1
print(b)        
result = largest_number_counting_sort(s1, s2)
print(f"The largest number is formed by: {result}")

if __name__ == '__main__':
    a = set()
    for s in s1:
        a.add(s)
    print(a)
    largest_number_counting_sort(s1, s2)