class Solution:
    def applySubstitutions(self, replacements: List[List[str]], text: str) -> str:
        possible_keys = {}
        for key,replacement in replacements:
            possible_keys[f"%{key}%"] = replacement
        
        while "%" in text:
            for key in possible_keys:
                if key in text:
                    text = text.replace(key,possible_keys[key])
        
        return text
