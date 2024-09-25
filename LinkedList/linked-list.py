class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def traverse(self):
        if not self.head:
            print("The list is empty.")
            return
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def insert_at_position(self, data, position):
        if position == 0:
            self.insert_at_beginning(data)
            return
        new_node = Node(data)
        current = self.head
        for _ in range(position - 1):
            if current is None:
                raise Exception("Position out of bounds")
            current = current.next
        new_node.next = current.next
        current.next = new_node

    def delete_at_beginning(self):
        if not self.head:
            print("The list is empty. No deletion performed.")
            return
        self.head = self.head.next

    def delete_at_end(self):
        if not self.head:
            print("The list is empty. No deletion performed.")
            return
        if not self.head.next:
            self.head = None
            return
        current = self.head
        while current.next.next:
            current = current.next
        current.next = None

    def delete_at_position(self, position):
        if not self.head:
            print("The list is empty. No deletion performed.")
            return
        if position == 0:
            self.delete_at_beginning()
            return
        current = self.head
        for _ in range(position - 1):
            if not current.next:
                raise Exception("Position out of bounds")
            current = current.next
        current.next = current.next.next

    def search(self, key):
        current = self.head
        position = 0
        while current:
            if current.data == key:
                print(f"Element {key} found at position {position}")
                return
            current = current.next
            position += 1
        print(f"Element {key} not found in the list.")

    def reverse(self):
        previous = None
        current = self.head
        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        self.head = previous

    def is_empty(self):
        return self.head is None


# Example Usage
ll = LinkedList()
ll.insert_at_end(1)
ll.insert_at_end(2)
ll.insert_at_end(3)
ll.traverse()  # Output: 1 -> 2 -> 3 -> None

ll.insert_at_beginning(0)
ll.traverse()  # Output: 0 -> 1 -> 2 -> 3 -> None

ll.delete_at_position(2)
ll.traverse()  # Output: 0 -> 1 -> 3 -> None

ll.search(1)  # Output: Element 1 found at position 1
ll.search(5)  # Output: Element 5 not found in the list.

ll.reverse()
ll.traverse()  # Output: 3 -> 1 -> 0 -> None
