from doubly_linked_list import DoublyLinkedList

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current_node = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if len(self.storage) < self.capacity:
            self.storage.add_to_tail(item)
            self.current_node = self.storage.head
        else:
            if not self.current_node.next:
                self.current_node.value = item
                self.current_node = self.storage.head
            else:
                self.current_node.value = item
                self.current_node = self.current_node.next

    def get(self):
        arr = []
        cur = self.storage.head
        while cur:
            arr.append(cur.value)
            cur = cur.next
        return arr
