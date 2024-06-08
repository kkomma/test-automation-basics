class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_k_group(head, k):
    # Check if the list is empty or k is 1
    if not head or k == 1:
        return head
    
    # Create a dummy node to serve as the new head
    dummy = ListNode(0)
    dummy.next = head
    
    # Initialize pointers
    prev = dummy
    curr = head
    count = 0
    
    # Count the number of nodes in the list
    while curr:
        count += 1
        curr = curr.next
    
    # Reverse the nodes in k-group
    while count >= k:
        curr = prev.next
        nxt = curr.next
        
        for _ in range(1, k):
            curr.next = nxt.next
            nxt.next = prev.next
            prev.next = nxt
            nxt = curr.next
        
        prev = curr
        count -= k
    
    return dummy.next

def main():
    # Create a linked list
    head = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node6 = ListNode(6)
    node7 = ListNode(7)
    
    head.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    node6.next = node7
    
    # Reverse nodes in k-group
    k = 3
    new_head = reverse_k_group(head, k)
    
    # Print the reversed linked list
    while new_head:
        print(new_head.val, end=" ")
        new_head = new_head.next

if __name__ == "__main__":
    main()