class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        LIS = [1] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])
        return max(LIS)
        
obj = Solution()
print(obj.lengthOfLIS([10,9,2,5,3,7,101,18])) # 4
print(obj.lengthOfLIS([0,1,0,3,2,3])) # 4
print(obj.lengthOfLIS([7,7,7,7,7,7,7])) # 1

