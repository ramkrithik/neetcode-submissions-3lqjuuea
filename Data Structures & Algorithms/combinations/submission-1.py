class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        curcomb, allcomb = [], []
        self.helper(1,curcomb,allcomb,n,k)
        return allcomb

    
    def helper(self, i, curcomb,allcomb,n,k):
        if len(curcomb) == k:
            allcomb.append(curcomb.copy())
            return
        if i > n:
            return

        for j in range(i,n+1):
            curcomb.append(j)
            self.helper(j+1,curcomb,allcomb,n,k)
            curcomb.pop()
        
        # curcomb.append(i)
        # self.helper(i+1,curcomb,allcomb,n,k)
        # curcomb.pop()

        # self.helper(i+1,curcomb,allcomb,n,k)

        