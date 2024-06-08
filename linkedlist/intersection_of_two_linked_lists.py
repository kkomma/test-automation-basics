class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def getIntersectionNode(headA, headB):
    # Find the lengths of both linked lists
    lenA, lenB = 0, 0
    currA, currB = headA, headB
    while currA:
        lenA += 1
        currA = currA.next
    while currB:
        lenB += 1
        currB = currB.next
    
    # Move the longer linked list's pointer ahead by the difference in lengths
    if lenA > lenB:
        for _ in range(lenA - lenB):
            headA = headA.next
    else:
        for _ in range(lenB - lenA):
            headB = headB.next
    
    # Traverse both linked lists until they intersect
    while headA != headB:
        headA = headA.next
        headB = headB.next
    
    return headA

# Test the function
if __name__ == "__main__":
    # Create the first linked list: 1 -> 2 -> 3 -> 4 -> 5
    headA = ListNode(1)
    headA.next = ListNode(2)
    headA.next.next = ListNode(3)
    headA.next.next.next = ListNode(4)
    headA.next.next.next.next = ListNode(5)
    
    # Create the second linked list: 6 -> 7 -> 4 -> 5
    headB = ListNode(6)
    headB.next = ListNode(7)
    headB.next.next = headA.next.next.next  # Intersection point
    
    intersection = getIntersectionNode(headA, headB)
    if intersection:
        print("Intersection found at node with value:", intersection.val)
    else:
        print("No intersection found")