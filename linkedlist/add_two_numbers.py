class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    dummy = ListNode(0)
    curr = dummy
    carry = 0

    while l1 or l2 or carry:
        sum = carry

        if l1:
            sum += l1.val
            l1 = l1.next
        if l2:
            sum += l2.val
            l2 = l2.next

        carry = sum // 10
        curr.next = ListNode(sum % 10)
        curr = curr.next

    return dummy.next

def main():
    # Test case 1
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    result = addTwoNumbers(l1, l2)
    print("Test case 1:")
    printLinkedList(result)

    # Test case 2
    l3 = ListNode(9)
    l3.next = ListNode(9)
    l3.next.next = ListNode(9)

    l4 = ListNode(1)

    result = addTwoNumbers(l3, l4)
    print("Test case 2:")
    printLinkedList(result)

def printLinkedList(head):
    curr = head
    while curr:
        print(curr.val, end=" ")
        curr = curr.next
    print()

if __name__ == "__main__":
    main()