class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def fetch_head(self):
        if self.head is None:
            print("List is empty")
        else:
            return self.head.data

    def view_list(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next

    def next_value(self, target):
        current_node = self.head
        while current_node is not None and current_node.data != target:
            current_node = current_node.next
        if current_node.next is not None:
            return current_node.next.data
        else:
            return "this is the last element on the LinkedList"

    def preceding_value(self, target):
        prev_node = None
        current_node = self.head

        while current_node is not None and current_node.data != target:
            prev_node = current_node
            current_node = current_node.next

        if prev_node is not None:
            return prev_node.data
        else:
            return "This is the first element on the Linked List"

    def add_element_to_start(self, item):
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node

    def add_element(self, item):
        new_node = Node(item)
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head

            while current_node is not None:
                if current_node.next is None:
                    current_node.next = new_node
                    break
                current_node = current_node.next

    def remove_node(self, target):
        prev_node = None
        current_node = self.head
        while current_node is not None and current_node.data != target:
            prev_node = current_node
            current_node = current_node.next
        if current_node is not None:
            if current_node is self.head:
                self.head = current_node.next
            else:
                prev_node.next = current_node.next
