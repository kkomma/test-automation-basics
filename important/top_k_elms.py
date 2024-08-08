from typing import List
from collections import Counter
import heapq

class TopKFrequentElements:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        
        count = Counter(nums)
        return [item for item, _ in count.most_common(k)]
    
    @staticmethod
    def main():
        solution = TopKFrequentElements()
        
        # # Test case 1: Basic input
        # nums1 = [1, 1, 1, 2, 2, 3]
        # k1 = 2
        # result1 = solution.topKFrequent(nums1, k1)
        # print(f"Test case 1: {result1}")  # Expected output: [1, 2]
        
        # # Test case 2: Empty input
        # nums2 = []
        # k2 = 3
        # result2 = solution.topKFrequent(nums2, k2)
        # print(f"Test case 2: {result2}")  # Expected output: []
        
        # # Test case 3: Input with negative numbers
        # nums3 = [-1, -1, 0, 1, 1, 2]
        # k3 = 2
        # result3 = solution.topKFrequent(nums3, k3)
        # print(f"Test case 3: {result3}")  # Expected output: [-1, 1]
        
        # Test case 4: Input with duplicate numbers
        nums4 = [3, 1, 1, 2, 2, 2, 3, 3, 3]
        k4 = 3
        result4 = solution.topKFrequent(nums4, k4)
        print(f"Test case 4: {result4}")  # Expected output: [3, 2, 1]

if __name__ == "__main__":
    TopKFrequentElements.main()
