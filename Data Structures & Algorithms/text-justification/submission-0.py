class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:

        if len(words) <=0:
            return []

        i = 0
        running_len = 0
        curr_strs = []
        out = []
        while i < len(words):
            if running_len + len(curr_strs) + len(words[i]) > maxWidth:
                to_fill = maxWidth-running_len
                left_slot_additional = to_fill % max((len(curr_strs) - 1),1)
                shared_space = to_fill//max(len(curr_strs) - 1,1)
                line = ""
                for k,word in enumerate(curr_strs):
                    line += word
                    if k < len(curr_strs) - 1:
                        line += " " * (shared_space + (1 if k < left_slot_additional else 0))
                    elif len(curr_strs) == 1:
                        line += " " * to_fill
                out.append(line)
                curr_strs = []
                running_len = 0
            
            curr_strs.append(words[i])
            running_len += len(words[i])
            i+=1
        
        if curr_strs:
            line = " ".join(curr_strs)
            line += " " * (maxWidth - len(line))
            out.append(line)

        return out
        
        