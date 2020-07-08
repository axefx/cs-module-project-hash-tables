from linkedlist import LinkedList

class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity = MIN_CAPACITY):
        self.data_storage = [LinkedList()] * capacity
        self.capacity = capacity
        self.count = 0


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        return self.capacity


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # tip: https://brilliant.org/wiki/hash-tables/
        # the number of items in table divided by size of table
        # gives idea of how packed it is not balance
        return self.count / self.capacity


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        https://stackoverflow.com/a/13809282/108022
        https://stackoverflow.com/questions/10696223/reason-for-5381-number-in-djb-hash-function/13809282#13809282

        Implement this, and/or FNV-1.
        """
        hash = 5381
        for x in key:
            # http://www.goodmath.org/blog/2013/10/20/basic-data-structures-hash-tables/
            hash = (hash * 33) + ord(x)
            # https://gist.github.com/mengzhuo/180cd6be8ba9e2743753
            # hash = (( hash << 5) + hash) + ord(x)
        return hash & 0xFFFFFFFF


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # get hash index
        i = self.hash_index(key)
        # create entry with key and value
        entry = HashTableEntry(key, value)
        # get ll using index
        cur = self.data_storage[i]
        # handle empty
        if cur.head is None:
            cur.insert(entry)            
            self.count += 1
        # else head is not None
        else:
            current = cur.head
            while current:
                if current.value.key == key:
                    current.value.value = value
                current = current.next
            cur.insert(entry)
            self.count += 1
        # todo: resize at load factor above .7
        # double the capacity


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        self.put(key, None)
        self.count -= 1
        # todo: resize down by half at load factor below .2
        # up to a minimum 


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        i = self.hash_index(key)
        cur = self.data_storage[i].head
        while cur:
            if cur.value.key == key:
                return cur.value.value
            cur = cur.next
        return None


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # save old data_storage
        # old_data-storage = self.data_storage
        # set data_storage = [None] * new_capacity
        # self.data_storage = [LinkedList()] * new_capacity
        # traverse old data_storage
        # for node in old_data-storage:
            # cur = node.value.head
        # put into new data_storage with new_capacity
        # update capacity to new_capacity




if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
    print(ord('a'))
    print(((5381 << 5)+ 5381)+ ord('a'))
    print(5381 << 5)
    print(5381 * 33)
    print(5381 * 33 - 5381)
