class ConverString:
    
    def convert_string_n(self, s):
        lower = []
        upper = []
        nrs = []
        for char in s:
            if char.islower():
                lower.append(char)
            elif char.isupper():
                upper.append(char)
            else:
                nrs.append(char)
        
        sorted_lower = self.counting_sort(lower)
        sorted_upper = self.counting_sort(upper)
        sorted_nrs = self.counting_sort(nrs)
        return ''.join(sorted_lower + sorted_upper + sorted_nrs)
    def counting_sort(self, arr):
        if not arr:
            return arr
        # Find the range of the characters in the array
        min_val = min(arr)
        max_val = max(arr)
        # Create a count array to store the count of each unique character
        count = [0] * (ord(max_val) - ord(min_val) + 1)
        # Store the count of each character
        for char in arr:
            count[ord(char) - ord(min_val)] += 1
        # Build the sorted array
        sorted_arr = []
        for i, cnt in enumerate(count):
            sorted_arr.extend([chr(i + ord(min_val))] * cnt)
        return sorted_arr

obj = ConverString()
s='aBcA1bC2'
print(obj.convert_string_n(s))