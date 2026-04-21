class Solution:
    def reverseBits(self, n: int) -> int:
        s = format(n,"032b")[::-1]
        return int(s,2)
        