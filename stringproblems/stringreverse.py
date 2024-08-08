
class StringReverse:

    def reverseSwap(self, s):
        s = list(s)
        left = 0
        right = len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return ''.join(s)
    
    def reverse(self, s):
        return s[::-1]
    
    def reverseStringMethod(self, s):
        charArray = []
        for index in range(len(s)-1,-1,-1):
            charArray.append(s[index])
        return ''.join(charArray)

obj = StringReverse()
input_string = 'apple inc'
print(obj.reverseSwap(input_string))
print(obj.reverse(input_string))
print(obj.reverseStringMethod(input_string))

