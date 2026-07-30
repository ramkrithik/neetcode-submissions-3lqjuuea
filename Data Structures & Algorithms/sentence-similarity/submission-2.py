class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:

        if len(sentence1) != len(sentence2):
            return False
        
        sim_pair = {}
        for pair in similarPairs:
            if pair[0] not in sim_pair:
                sim_pair[pair[0]] = set()
            if pair[1] not in sim_pair:
                sim_pair[pair[1]] = set()
            sim_pair[pair[0]].add(pair[1])
            sim_pair[pair[1]].add(pair[0])
        
        for i in range(0,len(sentence1)):
            w1 = sentence1[i]
            w2 = sentence2[i]

            if w1 == w2:
                continue
            elif w1 in sim_pair and w2 in sim_pair[w1]:
                continue
            elif w2 in sim_pair and w1 in sim_pair[w2]:
                continue
            else:
                return False
        
        return True

        

