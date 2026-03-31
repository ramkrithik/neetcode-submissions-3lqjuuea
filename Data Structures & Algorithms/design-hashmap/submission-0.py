class MyHashMap:

    def __init__(self):
        self.key_tracker =[]
        self.hash_map = []

    def put(self, key: int, value: int) -> None:
        if key in self.key_tracker:
            for i in self.hash_map:
                if i[0] == key:
                    i[1] = value
        else:
            self.key_tracker.append(key)
            self.hash_map.append([key,value])

    def get(self, key: int) -> int:
        if key not in self.key_tracker:
            return -1
        for i in self.hash_map:
            if i[0] == key:
                return i[1] 

    def remove(self, key: int) -> None:
        if key in self.key_tracker:
            for idx,pair in enumerate(self.hash_map):
                if pair[0] == key:
                    break
            self.hash_map.pop(idx)
            self.key_tracker.remove(key)


        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)