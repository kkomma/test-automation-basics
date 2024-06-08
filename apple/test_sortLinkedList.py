import unittest

from sortLinkedList import ListNode, sortLinkedList

class TestSortLinkedList(unittest.TestCase):
    def test_sortLinkedList(self):
        # Test case 1: Empty linked list
        head = None
        sorted_head = sortLinkedList(head)
        self.assertIsNone(sorted_head)

        # Test case 2: Linked list with a single node
        head = ListNode(5)
        sorted_head = sortLinkedList(head)
        self.assertEqual(sorted_head.val, 5)
        self.assertIsNone(sorted_head.next)

        # Test case 3: Linked list with multiple nodes in ascending order
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(3)
        head.next.next.next = ListNode(4)
        sorted_head = sortLinkedList(head)
        self.assertEqual(sorted_head.val, 1)
        self.assertEqual(sorted_head.next.val, 2)
        self.assertEqual(sorted_head.next.next.val, 3)
        self.assertEqual(sorted_head.next.next.next.val, 4)
        self.assertIsNone(sorted_head.next.next.next.next)

        # Test case 4: Linked list with multiple nodes in descending order
        head = ListNode(4)
        head.next = ListNode(3)
        head.next.next = ListNode(2)
        head.next.next.next = ListNode(1)
        sorted_head = sortLinkedList(head)
        self.assertEqual(sorted_head.val, 1)
        self.assertEqual(sorted_head.next.val, 2)
        self.assertEqual(sorted_head.next.next.val, 3)
        self.assertEqual(sorted_head.next.next.next.val, 4)
        self.assertIsNone(sorted_head.next.next.next.next)

        # Test case 5: Linked list with multiple nodes in random order
        head = ListNode(3)
        head.next = ListNode(1)
        head.next.next = ListNode(4)
        head.next.next.next = ListNode(2)
        sorted_head = sortLinkedList(head)
        self.assertEqual(sorted_head.val, 1)
        self.assertEqual(sorted_head.next.val, 2)
        self.assertEqual(sorted_head.next.next.val, 3)
        self.assertEqual(sorted_head.next.next.next.val, 4)
        self.assertIsNone(sorted_head.next.next.next.next)

if __name__ == '__main__':
    unittest.main()