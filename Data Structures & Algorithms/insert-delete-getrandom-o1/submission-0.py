class RandomizedSet:

    def __init__(self):
        self.s = {}
        self.lis = []
        self.l = 0
        

    def insert(self, val: int) -> bool:
        if val in self.s:
            return False
        
        self.s[val] = self.l
        self.l+=1
        self.lis.append(val)
        return True

    def remove(self, val: int) -> bool:
        
        if val in self.s:
            idx = self.s.get(val)
            self.lis[-1],self.lis[idx] = self.lis[idx], self.lis[-1]
            new_val = self.lis[idx]
            self.s[new_val] = idx
            self.s.pop(val)
            self.lis.pop()
            self.l-=1
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.lis)

        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()