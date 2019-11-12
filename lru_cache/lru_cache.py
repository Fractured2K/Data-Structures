import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.limit = limit
        self.nodes = 0
        self.cache = DoublyLinkedList()
        self.storage = {}

    """
    Retrieves the value associated with the given key.

    Also needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.

    Returns the value associated with the key
    or
    None if the key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        # Check if key is storage
        if key in self.storage:
            # Select node
            node = self.storage[key]

            # Move selected node to front of cache
            self.cache.move_to_front(node)

            # Return nodes current value
            return node.value[1]

        return None
    """
    Adds the given key-value pair to the cache.

    The newly-added pair should be considered the most-recently used
    entry in the cache.

    If the cache is already at max capacity before this entry is added,
    then the oldest entry in the cache needs to be removed to make room.

    Additionally, in the case that the key already exists in the cache,
    we simply want to overwrite the old value associated with the key with the newly-specified value.
    """
    def set(self, key, value):
        if key in self.storage:
            # Select node
            node = self.storage[key]
            # Assign new value to node
            node.value = (key, value)
            # Move to the front of cache
            self.cache.move_to_front(node)
            return

        # Check cache capacity
        if self.nodes is self.limit:
            # Remove oldest item in storage
            del self.storage[self.cache.tail.value[0]]
            # Removes oldest item in cache
            self.cache.remove_from_tail()
            # Decrement amount of nodes
            self.nodes -= 1

        # Add newest item to front of cache
        self.cache.add_to_head((key, value))
        # Add newest item to storage
        self.storage[key] = self.cache.head
        # Increment current node amount
        self.nodes += 1



cache = LRUCache()

cache.set('a', 'b')
cache.set('b', 'b')
cache.set('z', 'eb')
cache.get('z')
