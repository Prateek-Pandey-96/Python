class RandomizedSet:

    def __init__(self):
        self.mp = defaultdict(int)
        self.elements = []

    def insert(self, val: int) -> bool:
        if val in self.mp:
            return False
        self.elements.append(val)
        self.mp[val] = len(self.elements) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.mp:
            return False
        
        idx = self.mp[val]
        self.elements[idx] = self.elements[len(self.elements)-1]
        self.mp[self.elements[idx]] = idx
        self.elements.pop()
        del self.mp[val]
        return True

    def getRandom(self) -> int:
        idx = random.randint(0, len(self.elements)-1)
        return self.elements[idx]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
