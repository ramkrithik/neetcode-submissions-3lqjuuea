class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        import heapq

        heap = []
        heapq.heapify(heap)

        for num in nums:
            heapq.heappush(heap,-num)
        
        return [-heapq.heappop(heap) for i in range(k)][-1]