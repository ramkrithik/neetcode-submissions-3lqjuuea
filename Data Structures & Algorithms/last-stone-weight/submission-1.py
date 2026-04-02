class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq

        stones = [-stone for stone in stones]
        heapq.heapify(stones)

        while len(stones)>1:
            stone1 = -heapq.heappop(stones)
            stone2 = -heapq.heappop(stones)
            if stone1 == stone2:
                continue
            elif stone1 > stone2:
                stone1 = stone1-stone2
                heapq.heappush(stones,-stone1)
        
        return -stones[0] if stones else 0

        