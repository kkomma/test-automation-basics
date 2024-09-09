class Roman_To_Integer:
    def romanToInt(self, s):
        if s is None or len(s) == 0:
            return 0

        nums = [0] * len(s)

        for i in range(len(s)):
            if s[i] == 'M':
                nums[i] = 1000
            elif s[i] == 'D':
                nums[i] = 500
            elif s[i] == 'C':
                nums[i] = 100
            elif s[i] == 'L':
                nums[i] = 50
            elif s[i] == 'X':
                nums[i] = 10
            elif s[i] == 'V':
                nums[i] = 5
            elif s[i] == 'I':
                nums[i] = 1

        sum = 0
        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                sum -= nums[i]
            else:
                sum += nums[i]

        return sum + nums[-1]

# Test the code
solution = Roman_To_Integer()
print(solution.romanToInt("III"))  # Output: 3
print(solution.romanToInt("IV"))   # Output: 4
print(solution.romanToInt("IX"))   # Output: 9
print(solution.romanToInt("LVIII"))# Output: 58
print(solution.romanToInt("MCMXCIV")) # Output: 1994
