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
        self.limit = limit  # Max number of nodes
        self.order = DoublyLinkedList()  # Set up the storage to DLL
        self.size = 0  # set node to 0
        self.storage = {}  # set the cache

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """

    def get(self, key):
        # If key is in storage
        if key in self.storage:
            # move it to the end
            node = self.storage[key]
            self.order.move_to_end(node)
            # return the value
            return node.value[1]

        # If key is NOT in storage
        else:
            # return none
            return None

        # if key not in self.cache:
        #     return None
        # node_move = self.cache[key]
        # self.storage.move_to_front(node_move)
        # return node_move.value[1]

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """

    def set(self, key, value):

        # check and see if the key is in the dict
        if key in self.storage:
            # If it is
            node = self.storage[key]
            # overwrite the value
            node.value = (key, value)
            # move it to the end
            self.order.move_to_end(node)
            # nothing else to do, so exit function
            return

         # check and see if cache is full
        if self.size == self.limit:
            # remove oldests entry from dictionary
            del self.storage[self.order.head.value[0]]
            # AND LL
            self.order.remove_from_head()
            # reduce the size
            self.size -= 1

        # Add to the linked list (key and the value)
        self.order.add_to_tail((key, value))
        # Add the key and value to the dictionary
        self.storage[key] = self.order.tail
        # increment size
        self.size += 1


# First check the length of nothing greater then 10 if it greater then 10 then
# remove from 1 item from tail.
#
# Also need to delete item from the cache as well as the DDL
# With new item being added. I need to move that to the head of the DDL and cache
#
# Have another If statement that checks the current key and replaces the value
# ^ 1st also after updated move to the head of the Cache
