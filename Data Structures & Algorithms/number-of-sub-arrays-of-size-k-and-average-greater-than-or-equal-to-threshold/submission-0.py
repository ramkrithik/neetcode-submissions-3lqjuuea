class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        from collections import deque

        L = 0
        window = deque()

        count = 0
        for R in range(len(arr)+1):
            if R-L == k:
                avg = sum(window)/k
                if avg >= threshold:
                    count+=1
                L+=1
                window.popleft()
            
            if R != len(arr):
                window.append(arr[R])
        
        return count
            

