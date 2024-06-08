def count_greater_elements(arr):
    count = 0
    n = len(arr)
    
    for i in range(n-1):
        greater = False
        for j in range(i+1, n):
            if arr[i] > arr[j]:
                greater = True
            else:
                arr[j] = -1
        
        if not greater:
            count += 1
    
    return count

def count_greater_elements_fb(arr):
	# Initialize an empty list to store the result
	result = []
	
	# Iterate over the array from right to left
	for i in range(len(arr)-1, -1, -1):
		# Initialize a counter for greater elements
		greater_count = 0
		
		# Check elements on the right side
		for j in range(i+1, len(arr)):
			# If the current element is greater, increment the counter
			if arr[j] > arr[i]:
				greater_count += 1
		
		# If no greater elements are found, replace with -1
		if greater_count == 0:
			result.append(-1)
		else:
			result.append(greater_count)
	
	# Return the result list in the original order
	return result[::-1]

# Example usage:
# arr = [3, 4, 5, 1, 2]
# print(count_greater_elements(arr))  # Output: [2, 1, 0, -1, -1]

# Example usage
arr = [3, 8, 2, 7, 5, 1, 6, 4]
count = count_greater_elements(arr)
print("Count of elements greater than any element on the right side:", count)
print("Updated array:", arr)

arr = [3, 4, 5, 1, 2]
count = count_greater_elements_fb(arr)
print("Count of elements greater than any element on the right side:", count)
print("Updated array:", arr)