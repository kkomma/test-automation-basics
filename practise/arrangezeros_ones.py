class ArrangeZerosOnes:
    
    def arrange_zeros_ones_alternative(self, arr):
        count = 0
        for i in range(len(arr)):
            if arr[i] == 1:
                arr[i] = 0
                count +=1
        while count:
            arr[-count] = 1
            count -= 1
        return arr
    
    def arrange_zeros_ones(self, arr):
        left = 0
        right = len(arr) - 1
        while left < right:
            if arr[left] == 1 and arr[right] == 0:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1
            elif arr[left] == 0:
                left += 1
            elif arr[right] == 1:
                right -= 1
        return arr

if __name__ == '__main__':
    azo = ArrangeZerosOnes()
    print(azo.arrange_zeros_ones_alternative([0, 1, 0, 1, 1, 1, 0, 0, 1, 0]))    