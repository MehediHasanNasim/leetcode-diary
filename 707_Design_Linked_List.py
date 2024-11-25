class ListNode:
    def __init__(self, val):
        # Initializes a node with a value and pointers for the doubly linked list
        self.val = val
        self.prev = None  # Pointer to the previous node
        self.next = None  # Pointer to the next node

class MyLinkedList(object):

    def __init__(self):
        # Initializes the doubly linked list with dummy head and tail nodes
        self.left = ListNode(0)  # Dummy head node
        self.right = ListNode(0)  # Dummy tail node
        self.left.next = self.right  # Connect head to tail
        self.right.prev = self.left  # Connect tail to head

    def get(self, index):
        # Gets the value of the node at the specified index
        cur = self.left.next  # Start from the first real node
        while cur and index > 0:  # Traverse the list until the index is 0
            cur = cur.next
            index -= 1
        # Return the value if the node is valid and not the dummy tail
        if cur and cur != self.right and index == 0:
            return cur.val
        return -1  # Return -1 if the index is out of range

    def addAtHead(self, val):
        # Adds a node with the given value at the head of the list
        node, next, prev = ListNode(val), self.left.next, self.left  # Create a new node and set its pointers
        prev.next = node  # Connect the previous node to the new node
        next.prev = node  # Connect the next node to the new node
        node.next = next  # Connect the new node to the next node
        node.prev = prev  # Connect the new node to the previous node

    def addAtTail(self, val):
        # Adds a node with the given value at the tail of the list
        node, next, prev = ListNode(val), self.right, self.right.prev  # Create a new node and set its pointers
        prev.next = node  # Connect the previous node to the new node
        next.prev = node  # Connect the tail to the new node
        node.next = next  # Connect the new node to the tail
        node.prev = prev  # Connect the new node to the previous node

    def addAtIndex(self, index, val):
        # Adds a node with the given value at the specified index
        cur = self.left.next  # Start from the first real node
        while cur and index > 0:  # Traverse the list until the index is 0
            cur = cur.next
            index -= 1
        if cur and index == 0:  # Check if the index is valid
            node, next, prev = ListNode(val), cur, cur.prev  # Create a new node
            prev.next = node  # Connect the previous node to the new node
            next.prev = node  # Connect the next node to the new node
            node.next = next  # Connect the new node to the next node
            node.prev = prev  # Connect the new node to the previous node

    def deleteAtIndex(self, index):
        # Deletes the node at the specified index
        cur = self.left.next  # Start from the first real node
        while cur and index > 0:  # Traverse the list until the index is 0
            cur = cur.next
            index -= 1
        if cur and cur != self.right and index == 0:  # Check if the index is valid and not the dummy tail
            next, prev = cur.next, cur.prev  # Identify the adjacent nodes
            next.prev = prev  # Connect the next node to the previous node
            prev.next = next  # Connect the previous node to the next node

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
