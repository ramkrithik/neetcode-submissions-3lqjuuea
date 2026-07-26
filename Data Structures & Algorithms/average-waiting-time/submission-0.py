class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        
        time = 0
        waiting_time = 0
        for arr, prep in customers:
            time = max(time,arr) + prep
            waiting_time += time-arr    

        return waiting_time/len(customers)
