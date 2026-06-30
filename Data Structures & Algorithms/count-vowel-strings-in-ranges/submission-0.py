class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:

        count = {-1:0}
        total = 0
        vowels = {"a","e","i","o","u"}
        for i, s in enumerate(words):
            if s[0] in vowels and s[-1] in vowels:
                total+=1
            
            if i not in count:
                count[i] = total
        res = []
        for q in queries:
            res.append(count[q[1]] - count[q[0]-1])
        
        return res


        