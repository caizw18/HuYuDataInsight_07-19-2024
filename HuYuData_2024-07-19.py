class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def delete_node(self, key):
        current = self.head
        if current is not None and current.data == key:
            if current.next:
                self.head = current.next
                self.head.prev = None
            else:
                self.head = None
            current = None
            return

        while current is not None:
            if current.data == key:
                break
            current = current.next

        if current is None:
            return

        if current.next:
            current.prev.next = current.next
            current.next.prev = current.prev
        else:
            current.prev.next = None

        current = None

    def search(self, key):
        current = self.head
        while current is not None:
            if current.data == key:
                return True
            current = current.next
        return False

    def display_forward(self):
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next
        print()

    def display_backward(self):
        current = self.head
        if current is None:
            print("List is empty")
            return

        while current.next:
            current = current.next

        while current:
            print(current.data, end=' ')
            current = current.prev
        print()


# Example usage
if __name__ == "__main__":
    dll = DoublyLinkedList()

    dll.insert_at_end(1)
    dll.insert_at_end(2)
    dll.insert_at_end(3)
    dll.insert_at_beginning(4)

    print("Doubly Linked List (Forward):")
    dll.display_forward()

    print("Doubly Linked List (Backward):")
    dll.display_backward()

    dll.delete_node(3)
    print("After deleting 3:")
    dll.display_forward()