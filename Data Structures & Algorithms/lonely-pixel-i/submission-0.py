class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:

        r = {}
        c = {}
        for i in range(len(picture)):
            r[i] = []
            for j in range(len(picture[0])):
                if picture[i][j] == "B":
                    r[i].append(j)
                    if j not in c:
                        c[j] = []
                    c[j].append(i)
        
        count = 0
        for key in r:
            if len(r[key]) == 1:
                val = r[key][0]
                if len(c[val]) == 1:
                    count +=1
        
        return count

