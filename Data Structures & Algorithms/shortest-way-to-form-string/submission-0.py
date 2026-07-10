class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        source_chars = set(source)

        for char in target:
            if char not in source_chars:
                return -1
        
        m = len(source)

        source_it = 0

        count = 0

        for char in target:

            if source_it == 0:
                count+=1
            

            while source[source_it] != char:

                source_it = (source_it+1) % m

                if source_it== 0:
                    count+=1
            
            source_it = (source_it+1) % m
        
        return count

        