from typing import List
from itertools import chain

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        lst=[]
        for i in range(n):
            lst+=[nums[i]]
            lst+=[nums[i+n]]
        return lst
    
class Solution1:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        return list(chain(*zip(nums, nums[n:])))

if __name__=='__main__':
    a=Solution()
    print(a.shuffle([2,5,1,3,4,7],3))
    a=Solution1()
    d = a.shuffle([2,5,1,3,4,7],3)
    print(d)    