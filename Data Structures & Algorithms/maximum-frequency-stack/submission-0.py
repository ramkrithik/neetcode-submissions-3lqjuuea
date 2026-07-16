class FreqStack:

    def __init__(self):

        self.freq = {}
        self.pairs = {}
        self.max_freq = 0
        

    def push(self, val: int) -> None:
        self.freq[val] = self.freq.get(val,0)

        prev = self.freq[val]
        self.freq[val] = prev+1
        
        self.pairs[prev+1] = self.pairs.get(prev+1,[])

        self.pairs[prev+1].append(val)

        self.max_freq = max(self.max_freq,prev+1)

    def pop(self) -> int:

        to_rem = self.pairs[self.max_freq].pop()
        self.freq[to_rem]-=1

        if not self.pairs[self.max_freq]:
            del self.pairs[self.max_freq]
            self.max_freq -= 1
        
        return to_rem
        


        
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()