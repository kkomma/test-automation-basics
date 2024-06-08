class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        rob, norob = 0, 0
        for num in nums:
            newRob = norob + num
            norob = max(rob, norob)
            rob = newRob
        return max(rob, norob)

# https://leetcode.com/problems/house-robber/solutions/4600148/beats-100-c-java-python-js-explained-with-video-dynamic-programming-space-optimized/?
# Use two variables, rob and norob, to keep track of the maximum amount of money robbed with or without robbing the current house.
# Iterate through each house, and at each step, calculate the maximum amount of money if the current house is robbed (newRob) and if it is not robbed (newNoRob).
# Update rob and norob for the next iteration.
# The final result is the maximum amount between the two scenarios: robbing the last house or not robbing it.


# Example 1: Rob houses in a neighborhood
nums = [2, 7, 9, 3, 1]
sol = Solution()
print(sol.rob(nums)) # 12
# Example 2: Rob houses in a neighborhood
nums = [2, 3, 2]
sol = Solution()
print(sol.rob(nums)) # 4
