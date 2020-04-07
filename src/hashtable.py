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

        # Part 1: Hash collisions should be handled with an error warning. (Think about and
        # investigate the impact this will have on the tests)

        # Part 2: Change this so that hash collisions are handled with Linked List Chaining.

        Fill this in.
        '''

        # assign new index
        index = self._hash_mod(key)

        # generate a new key/value pair
        new_pair = LinkedPair(key, value)

        # generate or make space available in memory for the next key/value pair
        new_pair.next = self.storage[index]

        # store new key/value pair in the array using the index
        self.storage[index] = new_pair

    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''

        # get index
        index = self._hash_mod(key)

        # check if index exist
        if self.storage[index] is None:
            print("The key is not there")

        # if index exist, get it's position in the storage
        remove = self.storage[index]

        # set current position of the index to next
        self.storage[index] = remove.next

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''

        # get current index
        index = self._hash_mod(key)

        # get the position of the current index
        current_pair = self.storage[index]

        while current_pair:
            # check if the key at current positon is equal to key
            if current_pair.key == key:
                # if so, return it's value
                return current_pair.value
            # else set the current position to next
            current_pair = current_pair.next

        return None

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''

        temp_storage = self.storage
        self.capacity *= 2
        self.storage = [None] * self.capacity

        for data in temp_storage:
            if data != None:
                current = data
                while current != None:
                    self.insert(current.key, current.value)

                    current = current.next


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
