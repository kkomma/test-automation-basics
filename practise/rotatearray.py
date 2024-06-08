class RotateArray:

    def rotate_array(self,arr, num_positions):
        print('num_positions',num_positions)
        print('arr',len(arr))
        num_positions = num_positions % len(arr)
        print('a',num_positions)
        self.reverse(arr, 0, len(arr) - 1)
        self.reverse(arr, 0, num_positions - 1)
        self.reverse(arr, num_positions, len(arr) - 1)

    def reverse(self, a, start, end):
        while start < end:
            a[start], a[end] = a[end], a[start]
            start += 1
            end -= 1        

    def rotate(self, nums, k):
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        print('k::',k)
        nums[:] = nums[-k:] + nums[:-k]
        return nums
    
    def main(self):
        nums = [1, 2, 3, 4, 5, 6, 7]
        k = 3
        print(self.rotate(nums, k))
        nums = [-1, -100, 3, 99]
        k = 2
        print(self.rotate(nums, k))

if __name__ == '__main__':
    ra = RotateArray()
    ra.main()        
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    ra.rotate_array(nums,3)        
    print(nums)    