from typing import List
from collections import defaultdict

class Solution():

    def lengthOfLongestSubstringKDistinct(s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        left = ans = 0  # Initialize left pointer and answer
        curr_chars = defaultdict(int)  # Dictionary to store counts of characters
        for right in range(len(s)):  # Iterate through s using right pointer
            curr_chars[s[right]] += 1  # Increment count of current character
            while len(curr_chars) > k:  # If number of distinct characters exceeds k
                curr_chars[s[left]] -= 1  # Decrement count of character at left pointer
                if curr_chars[s[left]] == 0:
                    del curr_chars[s[left]]  # Remove character from dictionary if its count becomes zero
                left += 1  # Move left pointer to the right
            ans = max(ans, right - left + 1)  # Update answer with length of current substring
        return ans  # Return the length of the longest substring with at most k distinct characters
    
if __name__ == '__main__':
    s = "eceba"
    k = 2
    print(Solution.lengthOfLongestSubstringKDistinct(s,k))  # 3
    print(Solution.characterreplacement(s,k))  # 3
    
    s = "aa"
    k = 1
    print(Solution.lengthOfLongestSubstringKDistinct(s,k))  # 2
    
    s = "a"
    k = 1
    print(Solution.lengthOfLongestSubstringKDistinct(s,k))  # 1
    
    s = "a"
    k = 0
    print(Solution.lengthOfLongestSubstringKDistinct(s,k))  # 0
    
    s = "a"
    k = 2
    print(Solution.lengthOfLongestSubstringKDistinct(s,k))  # 1