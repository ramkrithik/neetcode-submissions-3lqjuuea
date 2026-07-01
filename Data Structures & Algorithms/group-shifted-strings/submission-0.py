class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:

        def get_hash(s):
            key = ""

            for a,b in zip(s, s[1:]):
                diff = (ord(b) - ord(a))%26
                key += chr(diff + ord("a"))
            return key
        
        groups = {}

        for string in strings:
            has = get_hash(string)
            if has not in groups:
                groups[has] = []
            groups[has].append(string)
        
        return list(groups.values())




        