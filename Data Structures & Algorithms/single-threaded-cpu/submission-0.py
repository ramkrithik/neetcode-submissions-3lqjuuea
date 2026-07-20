from heapq import heappush, heappop
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        
        for idx, task in enumerate(tasks):
            task.append(idx)
        
        tasks.sort(key=lambda key: key[0])

        res, minheap = [],[]
        i, time = 0, tasks[0][0]

        while minheap or i<len(tasks):
            while i<len(tasks) and time >= tasks[i][0]:
                heappush(minheap,[tasks[i][1],tasks[i][2]])
                i+=1
            if not minheap:
                time = tasks[i][0]
            else:
                processing_time, idx = heappop(minheap)
                time+= processing_time
                res.append(idx)
        
        return res



