class Node:
    def __init__(self):
        self.children = {}
        self.word = False
class WordDictionary:

    def __init__(self):
        self.root = Node()
        

    def addWord(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = Node()
            
            curr = curr.children[c]
        curr.word = True

    def search(self, word: str) -> bool:
        
        def dfs(curr, idx):
            if idx == len(word):
                return curr.word
            c = word[idx]

            if c == ".":
                for child in curr.children:
                    available = dfs(curr.children[child],idx+1)
                    if available:
                        return True
            elif c in curr.children:
                available = dfs(curr.children[c],idx+1)
                if available:
                    return True
            else:
                return False
            return False
        
        return dfs(self.root, 0)

                    
