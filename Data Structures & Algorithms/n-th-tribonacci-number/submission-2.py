class Solution:
    def tribonacci(self, n: int) -> int:
        from collections import deque
        
        deque = deque()

        deque.append(0)
        deque.append(1)
        deque.append(1)
        if n < 3:
            return deque[n]

        for i in range(2,n):
            deque.append(sum(deque))
            deque.popleft()
        
        return deque[-1]
