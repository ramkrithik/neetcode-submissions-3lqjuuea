class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq
        from collections import Counter
        counts = [(-i[1],i[0]) for i in Counter(nums).items()]

        max_heap = heapq.heapify(counts)

        return [heapq.heappop(counts)[1] for i in range(k)]


        