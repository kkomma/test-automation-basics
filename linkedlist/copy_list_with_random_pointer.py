class Node:
    def __init__(self, val=0, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random

def copyRandomList(head):
    if not head:
        return None

    # Step 1: Create a dictionary to store the mapping
    mapping = {}

    # Step 2: Traverse the original linked list and create a new node for each original node
    curr = head
    while curr:
        mapping[curr] = Node(curr.val)
        curr = curr.next

    # Step 3: Traverse the original linked list again and set the next and random pointers of the copied nodes
    curr = head
    while curr:
        mapping[curr].next = mapping.get(curr.next)
        mapping[curr].random = mapping.get(curr.random)
        curr = curr.next

    # Step 4: Return the head of the copied linked list
    return mapping[head]

def main():
    # Create the original linked list
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node1.random = node3
    node2.random = node1
    node3.random = node4
    node4.random = node2

    # Copy the linked list
    copied_head = copyRandomList(node1)

    # Print the original linked list
    print("Original Linked List:")
    curr = node1
    while curr:
        print(f"Value: {curr.val}, Random: {curr.random.val if curr.random else None}")
        curr = curr.next

    # Print the copied linked list
    print("Copied Linked List:")
    curr = copied_head
    while curr:
        print(f"Value: {curr.val}, Random: {curr.random.val if curr.random else None}")
        curr = curr.next

if __name__ == "__main__":
    main()