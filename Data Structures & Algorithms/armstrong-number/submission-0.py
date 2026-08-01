class Solution:
    def isArmstrong(self, n: int) -> bool:
        l = (len(str(n)))
        return n == sum((int(i)**l for i in str(n)))