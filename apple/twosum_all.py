def find_indexes(nums, target):
    indexes = []
    num_dict = {}

    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_dict:
            indexes.append([num_dict[complement], i])
        num_dict[num] = i

    return indexes

# Example usage
nums = [2, 7, 11, 15, 3, 6, 8]
target = 9
result = find_indexes(nums, target)
print(result)  # Output: [(0, 1), (4, 5)]
for index in result:
    print(index[0])
    print(index[1])