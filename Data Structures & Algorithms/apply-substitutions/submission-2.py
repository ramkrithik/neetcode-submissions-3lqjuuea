class Solution:
    def applySubstitutions(self, replacements: List[List[str]], text: str) -> str:
        mapping = {k: v for k, v in replacements}
        cache = {}
        def replace_recursively(key):
            if key in cache:
                return cache[key]
            res = mapping[key]
            for k in mapping:
                if k != key and f"%{k}%" in res:
                    res = res.replace(f"%{k}%", replace_recursively(k))
            cache[key] = res
            return res
        
        for k in mapping:
            replace_recursively(k)
        
        for k in cache:
            text = text.replace(f"%{k}%", cache[k])
        return text

        # possible_keys = {}
        # for key,replacement in replacements:
        #     possible_keys[f"%{key}%"] = replacement
        
        # while "%" in text:
        #     for key in possible_keys:
        #         if key in text:
        #             text = text.replace(key,possible_keys[key])
        
        # return text
