class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def sortLinkedList(head):
    if not head or not head.next:
        return head

    # Split the linked list into two halves
    slow = head
    fast = head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    second_half = slow.next
    slow.next = None

    # Recursively sort the two halves
    left = sortLinkedList(head)
    right = sortLinkedList(second_half)

    # Merge the sorted halves
    return merge(left, right)

def merge(left, right):
    dummy = ListNode()
    curr = dummy

    while left and right:
        if left.val < right.val:
            curr.next = left
            left = left.next
        else:
            curr.next = right
            right = right.next
        curr = curr.next

    if left:
        curr.next = left
    if right:
        curr.next = right

    return dummy.next

def main():
    # Test data
    # Create a linked list: 4 -> 2 -> 1 -> 3
    head = ListNode(4)
    head.next = ListNode(2)
    head.next.next = ListNode(1)
    head.next.next.next = ListNode(3)

    # Sort the linked list
    sorted_head = sortLinkedList(head)

    # Print the sorted linked list
    curr = sorted_head
    while curr:
        print(curr.val, end=" ")
        curr = curr.next

if __name__ == "__main__":
    main()