class Node:
    def __init__(self, val, prev=None, next=None, child=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

def flatten(head):
    if not head:
        return head
    
    curr = head
    while curr:
        if curr.child:
            next_node = curr.next
            child_tail = curr.child
            while child_tail.next:
                child_tail = child_tail.next
            curr.next = curr.child
            curr.child.prev = curr
            curr.child = None
            child_tail.next = next_node
            if next_node:
                next_node.prev = child_tail
        curr = curr.next
    
    return head

# Example usage
def main():
    # Create a sample multilevel doubly linked list
    head = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)
    node7 = Node(7)
    node8 = Node(8)
    node9 = Node(9)
    node10 = Node(10)
    node11 = Node(11)
    node12 = Node(12)

    head.next = node2
    node2.prev = head
    node2.next = node3
    node3.prev = node2
    node3.next = node4
    node4.prev = node3
    node4.next = node5
    node5.prev = node4
    node5.next = node6
    node6.prev = node5

    node3.child = node7
    node7.next = node8
    node8.prev = node7
    node8.next = node9
    node9.prev = node8

    node8.child = node11
    node11.next = node12
    node12.prev = node11

    node9.child = node10

    # Flatten the multilevel doubly linked list
    flatten(head)

    # Print the flattened list
    curr = head
    while curr:
        print(curr.val, end=" ")
        curr = curr.next

if __name__ == "__main__":
    main()