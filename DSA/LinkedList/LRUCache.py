class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.start, self.end = Node(-1, -1), Node(-1, -1)  
        self.start.next, self.end.prev = self.end, self.start
        
        self.capacity = capacity
        self.size = 0

        self.mp = {}

    def insert_at_beginning(self, node):
        start_next = self.start.next
        self.start.next = node
        node.prev = self.start
        node.next = start_next
        start_next.prev = node

    def delete_node_in_place(self, node):
        node_prev, node_next = node.prev, node.next
        node_prev.next, node_next.prev = node_next, node_prev

    def get(self, key: int) -> int:
        if key not in self.mp:
            return -1
        
        node = self.mp[key]
        self.delete_node_in_place(node)    
        self.insert_at_beginning(node)
        self.mp[key] = node
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.mp:
            node = self.mp[key]
            node.val = value
            self.delete_node_in_place(node)    
            self.insert_at_beginning(node)
            return
        
        if self.size < self.capacity:
            # no eviction insert in beginning
            self.size += 1
            node = Node(key, value)
            self.insert_at_beginning(node)
            self.mp[key] = node
            return
        
        # eviction
        del self.mp[self.end.prev.key]
        end_prev_prev = self.end.prev.prev
        end_prev_prev.next = self.end
        self.end.prev = end_prev_prev

        
        node = Node(key, value)
        self.insert_at_beginning(node)
        self.mp[key] = node

