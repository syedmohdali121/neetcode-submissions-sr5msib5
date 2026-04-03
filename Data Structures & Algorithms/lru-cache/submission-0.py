class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    

    def __init__(self, capacity: int):
        self.capacity = capacity  # Now self.capacity can be used anywhere in the class!
        self.cache = {}

        # Create dummy head and tail nodes to avoid edge cases
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        
        # Connect the dummies: head <-> tail
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add_node(self, node):
        """Always add the new node right after head (Most Recently Used position)."""
        # Step 1: Temporarily store the node currently sitting after the head
        old_first = self.head.next 
        
        # Step 2: Connect the new node to the head and the old first node
        node.prev = self.head
        node.next = old_first
        
        # Step 3: Update the head and the old first node to point back to the new node
        self.head.next = node
        old_first.prev = node

    def _remove_node(self, node):
        """Remove an existing node from the linked list."""
        # Step 1: Identify the neighbors
        prev_node = node.prev
        next_node = node.next
        
        # Step 2: Bridge the gap, bypassing the target node
        prev_node.next = next_node
        next_node.prev = prev_node
        

    def get(self, key: int) -> int:
        
        if key in self.cache:
            # 1. Find the node
            node = self.cache[key]
            # 2. Extract it from its current spot
            self._remove_node(node)
            # 3. Drop it at the front (make it Most Recently Used)
            self._add_node(node)
            return node.value
            
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # If the key exists, update its value and move to front
            node = self.cache[key]
            node.value = value
            self._remove_node(node)
            self._add_node(node)
        else:
            # If we are at capacity, we must evict the Least Recently Used item
            if len(self.cache) >= self.capacity:
                # The LRU item is always sitting right in front of the tail dummy
                lru_node = self.tail.prev
                
                # Remove it from the dictionary
                del self.cache[lru_node.key]
                # Remove it from the linked list
                self._remove_node(lru_node)
            
            # Create the new node
            new_node = Node(key, value)
            
            # Add it to the dictionary and the front of the linked list
            self.cache[key] = new_node
            self._add_node(new_node)
        
