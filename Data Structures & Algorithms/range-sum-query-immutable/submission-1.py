class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = []
        for i in nums:
            if not self.prefix:
                self.prefix.append(i)
            else:
                prev = self.prefix[-1]
                self.prefix.append(prev+i)

    def sumRange(self, left: int, right: int) -> int:
        
        prer = self.prefix[right]
        prel = self.prefix[left-1] if left >0 else 0

        return prer-prel


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)