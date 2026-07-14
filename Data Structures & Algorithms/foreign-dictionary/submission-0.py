class Solution:
    def foreignDictionary(self, words: List[str]) -> str:

        chars = {c:set() for word in words for c in word}

        for i in range(0,len(words)-1):
            w1= words[i]
            w2 = words[i+1]

            minlen = min(len(w1), len(w2))

            if len(w1) > len(w2) and w1[:minlen] == w2[:minlen]:
                return ""
            
            for j in range(0,minlen):
                if w1[j] != w2[j]:
                    chars[w1[j]].add(w2[j])
                    break
        
        visited = {}
        res = []

        def dfs(char):
            if char in visited:
                return visited[char]
            
            visited[char] = True

            for n in chars[char]:
                if dfs(n):
                    return True
            
            visited[char] = False
            res.append(char)
        
        for char in chars:
            if dfs(char):
                return ""
        
        res ="".join(res)[::-1]
        return res



        