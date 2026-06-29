class TimeMap:

    def __init__(self):
        self.d = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # from bisect import insort
        if key not in self.d:
            self.d[key] = []
        # insort(self.d[key],(timestamp,value))
        self.d[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:

        if key not in self.d:
            return ""
        l = 0
        r = len(self.d[key])-1
        res = ""
        while l<=r:
            m = (l+r)//2
            if self.d[key][m][0] <= timestamp:
                res = self.d[key][m][1]
                l = m+1
            else:
                r = m-1
        
        return res
        
