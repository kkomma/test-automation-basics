def count_dividing_elements(arr):
    count = 0
    total_sum = sum(arr)
    
    for num in arr:
        if num != 0 and total_sum % num == 0:
            count += 1
    
    return count

# Example usage
arr = [2, 4, 6, 8, 10]
result = count_dividing_elements(arr)
print(f"Number of elements that divide the sum of all other elements: {result}")