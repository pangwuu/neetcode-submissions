class ListNode:
    def __init__(self, key, prev=None, next=None):
        self.key = key
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        # keep track of which key corresponds to which listNode
        self.key_to_node = {}

        # we keep track of priority with a doubly linked LL, head = oldest, tail = newest
        self.head = ListNode(-1)
        self.tail = ListNode(-1)

        self.head.next = self.tail
        self.tail.prev = self.head
    
    def remove(self, key):
        node = self.key_to_node[key]

        previousNode = node.prev
        nextNode = node.next
        
        previousNode.next = nextNode
        nextNode.prev = previousNode

    def insert(self, key):
        # inserts at the 2nd last position
        node = self.key_to_node[key]

        node.prev = self.tail.prev
        node.next = self.tail

        self.tail.prev.next = node
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(key)
            self.insert(key)
            return self.cache[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        # if the key does exist, update the location
        if key in self.cache:
            self.remove(key)
            self.insert(key)
            self.cache[key] = value
        else:
            # do we need to evict one?
            if len(self.cache) == self.capacity:
                # remove head
                curr_LRU = self.head.next.key
                self.remove(curr_LRU)

                self.cache.pop(curr_LRU)
                self.key_to_node.pop(curr_LRU)
            
            # then we do the standard add
            newNode = ListNode(key)
            self.key_to_node[key] = newNode
            self.cache[key] = value
            self.insert(key)

