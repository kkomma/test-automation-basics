class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def sort(self):
        if self.head is None:
            return

        # Convert linked list to a list
        values = []
        current = self.head
        while current:
            values.append(current.data)
            current = current.next

        # Sort the list
        values.sort()

        # Update the linked list with sorted values
        current = self.head
        for value in values:
            current.data = value
            current = current.next

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.insert(5)
    linked_list.insert(2)
    linked_list.insert(8)
    linked_list.insert(1)
    linked_list.insert(3)

    print("Original Linked List:")
    linked_list.display()

    linked_list.sort()

    print("Sorted Linked List:")
    linked_list.display()