class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def hasCycle(head):
    if not head or not head.next:
        return False

    slow = head
    fast = head.next

    while slow != fast:
        if not fast or not fast.next:
            return False
        slow = slow.next
        fast = fast.next.next

    return True

# Test the linked list cycle detection
def main():
    # Create a linked list with a cycle
    head = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)

    head.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node2  # Create a cycle

    # Check if the linked list has a cycle
    if hasCycle(head):
        print("The linked list has a cycle.")
    else:
        print("The linked list does not have a cycle.")

if __name__ == "__main__":
    main()