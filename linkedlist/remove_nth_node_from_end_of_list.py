class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(head, n):
    # Create a dummy node to handle edge cases
    dummy = ListNode(0)
    dummy.next = head

    # Initialize two pointers, slow and fast
    slow = dummy
    fast = dummy

    # Move the fast pointer n steps ahead
    for _ in range(n):
        fast = fast.next

    # Move both pointers until the fast pointer reaches the end
    while fast.next:
        slow = slow.next
        fast = fast.next

    # Remove the nth node from the end
    slow.next = slow.next.next

    # Return the updated head of the linked list
    return dummy.next

# Test the removeNthFromEnd function
def main():
    # Create a sample linked list
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    # Remove the 2nd node from the end
    n = 2
    new_head = removeNthFromEnd(head, n)

    # Print the updated linked list
    while new_head:
        print(new_head.val, end=" ")
        new_head = new_head.next

if __name__ == "__main__":
    main()