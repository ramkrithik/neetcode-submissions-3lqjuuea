class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:

        out = []

        c = {}
        def backtrack(i):

            if i in c:
                return c[i]

            if i == len(s):
                return [""]
            
            results = []
            for word in wordDict:
                if s[i:i+len(word)] == word:
                    rest = backtrack(i + len(word))
                    for sentence in rest:
                        if sentence:
                            results.append(word + " " + sentence)
                        else:
                            results.append(word)
            
            c[i] = results
            return c[i]

        return backtrack(0)
                

