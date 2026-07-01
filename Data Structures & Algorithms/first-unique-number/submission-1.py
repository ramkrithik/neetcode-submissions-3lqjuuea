class FirstUnique:

    def __init__(self, nums: List[int]):
        
        self.unique_queue = {1:[]}
        self.non = set()
        self.nums = nums
        for i in nums:
            if i not in self.unique_queue[1] and i not in self.non:
                self.unique_queue[1].append(i)
            elif i in self.unique_queue[1]:
                self.unique_queue[1].remove(i)
                self.non.add(i)       

    def showFirstUnique(self) -> int:
        return self.unique_queue[1][0] if self.unique_queue[1] else -1

    def add(self, value: int) -> None:
        if value not in self.unique_queue[1] and value not in self.non:
            self.unique_queue[1].append(value)
        elif value in self.unique_queue[1]:
            self.unique_queue[1].remove(value)
            self.non.add(value)


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
