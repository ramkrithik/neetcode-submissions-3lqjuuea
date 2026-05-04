class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        import heapq

        class Node:
            def __init__(self,idx):
                self.idx=idx
            
            def __lt__(self, other):
                if capital[self.idx] != capital[other.idx]:
                    return capital[self.idx] < capital[other.idx]
                return self.idx < other.idx

        
        min_capital = []
        max_profit = []

        for idx, i in enumerate(capital):
            heapq.heappush(min_capital,Node(idx))
        
        for _ in range(k):
            while min_capital and capital[min_capital[0].idx] <= w:
                idx = heapq.heappop(min_capital).idx
                heapq.heappush(max_profit, -profits[idx])
            
            if not max_profit:
                break
            
            w+= -heapq.heappop(max_profit)

        return w