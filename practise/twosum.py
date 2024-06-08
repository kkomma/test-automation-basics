class TwoSum:

    def twosum(self, nums, target):
        dict = {}
        for i in range(len(nums)):
            if target - nums[i] in dict:
                return [dict[target - nums[i]], i]
            dict[nums[i]] = i
        return None

if __name__ == '__main__':
    ts = TwoSum()
    print(ts.twosum([2, 7, 11, 15], 9))  # [0, 1]
    print(ts.twosum([3, 2, 4], 6))  # [1, 2]
    print(ts.twosum([3, 3], 6))  # [0, 1]
    print(ts.twosum([3, 3, 3], 6))  # [0, 1]
    print(ts.twosum([3, 3, 3, 3], 6))  # [0, 1]
    print(ts.twosum([3, 3, 3, 3, 3], 6))  # [0, 1]
    print(ts.twosum([3, 3, 3, 3, 3, 3], 6))  # [0, 1]
    print(ts.twosum([3, 3, 3, 3, 3, 3, 3], 6))  # [0, 1]
    print(ts.twosum([3, 3, 3, 3, 3, 3, 3, 3], 6))  # [0, 1]
    print(ts.twosum([3, 3, 3, 3, 3, 3, 3, 3, 3], 6))  # [0, 1]
    print(ts.twosum([3, 3, 3, 3, 3, 3, 3, 3, 3, 3], 6))  # [0, 1]
    print(ts.twosum([3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3], 6))
    print(ts.twosum([3, 2, 1], 16))  # [0, 1]        