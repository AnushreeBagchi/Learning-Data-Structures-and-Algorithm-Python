class LinkedList:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashMap:
    def __init__(self,initial_size=10):
        self.bucket_array = [None for _ in range(initial_size)]
        self.no_entries = 0
        self.p = 37
        self.load_factor = 0.7
    def get_bucket_index(self,key):
        return self.get_hash_code(key)
    def get_hash_code(self, key):
        key = str(key)
        num_buckets = len(self.bucket_array)
        hash_code = 0
        current_coefficient = 1
        for character in key:
            hash_code += ord(character)*current_coefficient
            hash_code = hash_code%num_buckets
            current_coefficient *= self.p
            current_coefficient = current_coefficient%num_buckets
        return hash_code%num_buckets
    def put(self,key,value):
        bucket_index = self.get_bucket_index(key)
        new_node = LinkedList(key, value)
        head = self.bucket_array[bucket_index]
        # if key is already present, update value
        while head is not None:
            if head.key == key:
                head.value = value
                return
            head = head.next
            # if not present
        head = self.bucket_array[bucket_index]
        new_node.next = head
        self.bucket_array[bucket_index] = new_node
        self.no_entries +=1
        # checking load factor
        current_load_factor = self.no_entries/len(self.bucket_array)
        if current_load_factor > self.load_factor:
            self.no_entries = 0
            self.rehash()
    def rehash(self):
        old_bucket_array = self.bucket_array
        old_no_entries = len(self.bucket_array)
        self.bucket_array = [None for _ in range(2*old_no_entries)]
        for head in old_bucket_array:
            while head is not None:
                key = head.key
                value = head.value
                self.put(key, value) 
                head = head.next
    def get(self,key):
        bucket_index = self.get_bucket_index(key)
        head = self.bucket_array[bucket_index]
        while head is not None:
            if head.key == key:
                return head.value
    def size(self):
        return self.no_entries
    def delete(self, key):
        bucket_index = self.get_bucket_index(key)
        head = self.bucket_array[bucket_index]
        previous = None
        while head is not None:
            if head.key == key:
                if previous is None:
                    self.bucket_array[bucket_index] = head.next
                else:
                    previous.next = head.next
                self.no_entries -=1
            else:
                previous = head
                head = head.next


        
            

hashmap = HashMap()
print(hashmap.get_hash_code("abcd"))
hashmap.put("one",1)
hashmap.put("abcd",125)

print(hashmap.get("abcd"))
print(hashmap.size())









        