
class Substring:
    def largest_substring_withoutrepeat_chars(s):
        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res
        
    if __name__ == '__main__':
        s = "abcabcbb"
        print(largest_substring_withoutrepeat_chars(s))

        s = "bbbbb"
        print(largest_substring_withoutrepeat_chars(s))

        s = "aabaaa"
        print(largest_substring_withoutrepeat_chars(s))

        s = "baaaaa"
        print(largest_substring_withoutrepeat_chars(s))
