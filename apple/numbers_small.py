nums = [8,1,2,2,3]
idx = []
for i in range(len(nums)):
    count = 0
    for j in range(len(nums)):
        if nums[i] > nums[j]:
            count +=1
    idx.append(count)

print(idx)