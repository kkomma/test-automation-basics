from collections import Counter
import heapq

class SortCharactersByFrequency:
    def frequencySort(self, s: str) -> str:
        if not s:
            return s
        
        count = Counter(s)
        print('count::',count)
        pq = [(-freq, char) for char, freq in count.items()]
        print('pq1::',pq)
        heapq.heapify(pq)
        print('pq2::',pq)
        
        result = []
        while pq:
            freq, char = heapq.heappop(pq)
            result.append(char * -freq)
        
        print('result::',result)
        st = ''.join(result)
        print('st::',st)
        return st
    
    @staticmethod
    def main():
        obj = SortCharactersByFrequency()
        
        # # Test Case 1: Empty string
        # s1 = ""
        # expected1 = ""
        # result1 = obj.frequencySort(s1)
        # print("Test Case 1 Passed" if result1 == expected1 else "Test Case 1 Failed")
        
        # # Test Case 2: String with single character
        # s2 = "a"
        # expected2 = "a"
        # result2 = obj.frequencySort(s2)
        # print("Test Case 2 Passed" if result2 == expected2 else "Test Case 2 Failed")
        
        # # Test Case 3: String with multiple characters, no repeated characters
        # s3 = "abcde"
        # expected3 = "abcde"
        # result3 = obj.frequencySort(s3)
        # print("Test Case 3 Passed" if result3 == expected3 else "Test Case 3 Failed")
        
        # Test Case 4: String with multiple characters, some repeated characters
        s4 = "aaaabccba"
        expected4 = "aaaaabbcc"
        result4 = obj.frequencySort(s4)
        print("Test Case 4 Passed" if result4 == expected4 else "Test Case 4 Failed")

if __name__ == "__main__":
    SortCharactersByFrequency.main()
