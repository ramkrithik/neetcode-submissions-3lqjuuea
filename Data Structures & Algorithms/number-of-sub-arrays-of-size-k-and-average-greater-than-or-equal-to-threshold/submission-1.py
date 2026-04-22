class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        # from collections import deque

        # L = 0
        # window = deque()

        # count = 0
        # for R in range(len(arr)+1):
        #     if R-L == k:
        #         avg = sum(window)/k
        #         if avg >= threshold:
        #             count+=1
        #         L+=1
        #         window.popleft()
            
        #     if R != len(arr):
        #         window.append(arr[R])
        
        # return count

        L=0
        count =0 
        cur_sum = sum(arr[:k-1])

        for R in range(k-1,len(arr)):
            cur_sum += arr[R]

            if cur_sum/k >= threshold:
                count+=1
            
            cur_sum -= arr[L]
            L+=1
        
        return count


            

