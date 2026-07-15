class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        from collections import Counter,deque
        from heapq import heappush,heappop

        frequency = Counter(tasks)
        heap = []
        q = deque()
        
        for freq in frequency.values():
            heappush(heap,-freq)
        
        time = 0
        while q or heap:
            time+=1

            if q and q[0][0] <= time:
                heappush(heap, q.popleft()[1])
            
            if heap:
                freq = heappop(heap)
                freq+=1
                if freq<0:
                    q.append((time+n+1,freq))
        
        return time