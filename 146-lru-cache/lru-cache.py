class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.dictionary = {}
        

    def get(self, key: int) -> int:
        if key in self.dictionary.keys():
            value = self.dictionary[key]
            del(self.dictionary[key])
            self.dictionary[key]=value
            return value
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.dictionary.keys():
            del(self.dictionary[key])
            self.dictionary[key]=value
        else:
            if len(self.dictionary)<self.capacity:
                self.dictionary[key]=value
            else:
                del(self.dictionary[list(self.dictionary)[0]])
                self.dictionary[key]=value

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)