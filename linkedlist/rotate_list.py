class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            curr_node = self.head
            while curr_node.next:
                curr_node = curr_node.next
            curr_node.next = new_node

    def rotate(self, k):
        if not self.head or not self.head.next:
            return

        curr_node = self.head
        count = 1
        while count < k and curr_node:
            curr_node = curr_node.next
            count += 1

        if not curr_node:
            return

        kth_node = curr_node

        while curr_node.next:
            curr_node = curr_node.next

        curr_node.next = self.head
        self.head = kth_node.next
        kth_node.next = None

    def display(self):
        curr_node = self.head
        while curr_node:
            print(curr_node.data, end=" ")
            curr_node = curr_node.next
        print()

def main():
    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.append(4)
    linked_list.append(5)

    print("Original Linked List:")
    linked_list.display()

    k = 2
    linked_list.rotate(k)

    print(f"Linked List after rotating by {k} positions:")
    linked_list.display()

if __name__ == "__main__":
    main()