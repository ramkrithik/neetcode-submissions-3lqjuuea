class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        def reverse(l,r):
            while l<r:
                s[l],s[r] = s[r],s[l]
                l+=1
                r-=1
            return

        reverse(0,len(s)-1)

        prev_space = None
        for i in range(0,len(s)):
            if s[i] == " ":
                if prev_space is None:
                    prev_space = i
                    reverse(0,i-1)
                else:
                    reverse(prev_space+1,i-1)
                    prev_space = i
        
        if prev_space is None:
            reverse(0,len(s)-1)
        else:
            reverse(prev_space+1,len(s)-1)
