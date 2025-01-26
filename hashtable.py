#simple realisation concept of HashTable

def HashFunction(value):
    return value%10

class HashTable:
    def __init__(self, setsize):
        self.setsize = setsize
        self.table = [[] for _ in range(setsize)]

    def add(self, val):
        hash = HashFunction(val)
        if hash < self.setsize:
            self.table[hash].append(val)

    def find(self, val):
        if val in self.table[HashFunction(val)]:
            return True
        return False

    def print(self):
        for i in self.table:
            for j in i:
                print(j)
            print("\n")
        
        
table = HashTable(10)
table.add(2)
table.add(34)
print(table.find(34))
table.print()
