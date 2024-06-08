class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def remove_duplicates_from_sorted_list_ii(head):
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy
    curr = head

    while curr:
        if curr.next and curr.val == curr.next.val:
            while curr.next and curr.val == curr.next.val:
                curr = curr.next
            prev.next = curr.next
        else:
            prev = prev.next
        curr = curr.next

    return dummy.next

def main():
    # Create a sorted linked list with duplicates
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(3)
    head.next.next.next.next = ListNode(4)
    head.next.next.next.next.next = ListNode(4)
    head.next.next.next.next.next.next = ListNode(5)

    # Call the remove_duplicates_from_sorted_list_ii function
    new_head = remove_duplicates_from_sorted_list_ii(head)

    # Print the modified linked list
    while new_head:
        print(new_head.val, end=" ")
        new_head = new_head.next

if __name__ == "__main__":
    main()