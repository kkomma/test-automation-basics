class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n
        n1, n2 = 2, 3

        for i in range(4, n + 1):
            temp = n1 + n2
            n1 = n2
            n2 = temp
        return n2

    def climbStairs1(self, n: int) -> int:      
        one, two = 1,1
        for i in range(n-1):
            temp = one
            one = one + two
            two = temp
        return one


if __name__ == '__main__':
    climb = Solution()
    print(climb.climbStairs1(5))
    print(climb.climbStairs1(6))
    print(climb.climbStairs1(7))