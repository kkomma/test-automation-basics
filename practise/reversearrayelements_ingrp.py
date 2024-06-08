class ReverseInGroups:
    def __init__(self):
        self.arr = []
        self.k = 0
        self.n = 0

    def reverseInGroups(self):
        for i in range(0, self.n, self.k):
            left = i
            right = min(i + self.k - 1, self.n - 1)
            while left < right:
                self.arr[left], self.arr[right] = self.arr[right], self.arr[left]
                left += 1
                right -= 1

    def printArr(self):
        for i in range(self.n):
            print(self.arr[i], end=" ")
        print()

    def main(self):
        self.arr = [1, 2, 3, 4, 5]
        self.k = 3
        self.n = len(self.arr)
        self.reverseInGroups()
        self.printArr()
        self.arr = [10, 20, 30, 40, 50, 60]
        self.k = 2
        self.n = len(self.arr)
        self.reverseInGroups()
        self.printArr()

if __name__ == '__main__':
    rig = ReverseInGroups()
    rig.main()        