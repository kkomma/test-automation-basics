import string

class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        a = [0]*26
        alphabet = list(string.ascii_lowercase)
        for letter in alphabet:
            count = float('inf')
            for word in words:
                count = min(count, word.count(letter))
            a[ord(letter)-ord('a')] += count
        res =[]
        for idx,val in enumerate(alphabet):
             if a[idx] > 0:
                for i in range(a[idx]):
                    res.append(val)
        return res

# Time complexity: O(n*m) where n is the number of words and m is the length of the longest word
a = ["bella","label","roller"]
sol = Solution()
print(sol.commonChars(a)) # ['l', 'l', 'e]
    
a = ["cool","lock","cook"]
sol = Solution()
print(sol.commonChars(a)) # ['c', 'o']
