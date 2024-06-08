class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

# Main function
if __name__ == "__main__":
    # Create a linked list
    linked_list = LinkedList()
    
    # Add nodes to the linked list
    linked_list.head = Node(1)
    second = Node(2)
    third = Node(3)
    fourth = Node(4)
    linked_list.head.next = second
    second.next = third
    third.next = fourth
    
    # Print the original linked list
    print("Original linked list:")
    linked_list.print_list()
    
    # Reverse the linked list
    linked_list.reverse()
    
    # Print the reversed linked list
    print("Reversed linked list:")
    linked_list.print_list()