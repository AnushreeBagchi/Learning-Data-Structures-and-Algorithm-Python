class HashTable:
    def __init__(self, initial_size=10000):
        self.table = [None for _ in range(initial_size)]
    def get_hash_value(self, string):
        value = ord(string[0])*100+ord(string[1])
        return value
    def store(self, string):
        hv = self.get_hash_value(string)
        if self.table[hv] != None:
            self.table[hv].append(string)
        else:
            self.table[hv] = string
    def lookup(self, string):
        hv = self.get_hash_value(string)
        if self.table[hv] != None:
            if string in self.table[hv]:
                return hv
        return -1

table = HashTable()
print(table.lookup("UDACITY"))
table.store("UDACITY")
print(table.lookup("UDACITY"))
print(table.lookup("UDACIOUS"))

