class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        way2 = 1
        way1 = 2
        for n in range(3,n+1):
            current = way2 + way1
            way2 = way1
            way1 = current
        return way1

        