class Solution:
    def climbStairs(self, n: int) -> int:
        c = {}
        def climb(val):
            if val in c:
                return c[val]
            if val==0:
                return 1
            if val==1:
                return 1
            c[val] = climb(val-1) + climb(val-2)
            return c[val]
        return climb(n)
        