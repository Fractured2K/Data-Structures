from doubly_linked_list import DoublyLinkedList
import sys
sys.path.append('../doubly_linked_list')


class Queue:
    def __init__(self):
        self.size = 0

        # Why is our DLL a good choice to store our elements?
        # DLL is good because it's memory efficent O(1), there's no need to loop when removing or inserting elements
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        self.size += 1
        self.storage.add_to_tail(value)

    def dequeue(self):
        value = self.storage.remove_from_head()

        if value is not None:
            self.size -= 1

        return value

    def len(self):
        return self.size
