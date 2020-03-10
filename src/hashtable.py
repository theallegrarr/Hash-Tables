# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity
        self.count = 0

    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        '''
        Store the value with the given key.
        Hash collisions should be handled with Linked List Chaining
        Fill this in.
        '''
        new_node = LinkedPair(key, value)
        hm_key = self._hash_mod(key)
        head = self.storage[hm_key]
        node = head
        # if there is nothing in hash table at that key populate it with new_node
        if not head:
            self.storage[hm_key] = new_node
        else:
            # if first node has same key overwrite value
            if head.key == key:
                new_node.next = head.next
                self.storage[hm_key] = new_node
            else:
                while node:
                    # if next node is None populate with new_node
                    if not node.next:
                        node.next = new_node
                        break
                    # if next node key is equal overwrite with new_node
                    elif node.next.key == key:
                        new_node.next = node.next.next
                        node.next = new_node
                        break
                    else:
                        node = node.next


    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        last = None
        current = self.storage[index]
        while current and current.key != key:
            last = current
            current = current.next
        # If key isn't found
        if self.storage[index] is None:
            print("Key could not be found.")
        # If key is found
        else:
            # Remove the first element in the linked list
            if last is None:
                self.storage[index] = current.next
            else:
                last.next = current.next


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        current = self.storage[index]
        while current:
            if current.key == key:
                return current.value
            else:
                current = current.next
        return None


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        self.capacity = self.capacity * 2
        new_ht = HashTable(self.capacity)
        for node in self.storage:
            while node:
                new_ht.insert(node.key, node.value)
                node = node.next
        self.storage = new_ht.storage



if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
