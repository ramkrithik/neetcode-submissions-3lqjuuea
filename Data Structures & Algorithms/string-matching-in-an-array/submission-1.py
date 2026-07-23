class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:

        words.sort(key = lambda x: len(x))

        out = set()

        for idx,word in enumerate(words):

            for j in range(idx+1,len(words)):

                if word in words[j]:
                    out.add(word)
        
        return list(out)


        