class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def set_next_node(self, next_node):
        self.next_node = next_node

    def get_next_node(self):
        return self.next_node

    def get_value(self):
        return self.value

    def to_string(self):
        if self.next_node is None:
            print("{ val: " + str(self.value) + " -> } ", end="")
        else:
            print("{ val: " + str(self.value) + " -> " + str(self.next_node.get_value()) + "} ", end="")



class Queue:

    def __init__(self, max_size=None, head=None,tail=None):
        self.head = head
        self.tail = tail
        self.size = 1
        self.max_size = max_size #declared as none if no value

        if self.head is not None and self.tail is not None:
            self.size += 1
            self.head.set_next_node(self.tail)
        elif self.head is None and self.tail is None:
            self.size = 0

        if max_size == 0:
            self.head = None
            self.tail = None
            print("Empty Queue, Max Size = 0")
        elif max_size == 1:
            self.tail = None
            self.head.set_next_node(None)
            print("One item in queue Max Size = 1")

    def poll(self): #retrieves and removes head
        if self.size == 0:
            print("Empty Queue")
            return
        og_head = self.head
        self.head = og_head.get_next_node()
        og_head.set_next_node(None)
        self.size -= 1
        return og_head

    def add(self, node):
        if not self.has_space():
            print("Has no space")
            return
        if self.size == 0:
            self.head = node
        elif self.size == 1:
            self.tail = node
            self.head.set_next_node(self.tail)
        else:
            self.tail.set_next_node(node)
            self.tail = node
            node.set_next_node(None)
        self.size += 1

    def is_empty(self):
        return self.size == 0

    def get_size(self):
        return self.size

    def has_space(self):
        if self.max_size is None:
            return True
        return self.size < self.max_size

    def peek(self):
        if self.head is None:
            print("List is empty")
            return
        return self.head

    def print_queue(self):
        current = self.peek()
        for i in range(self.size):
            current.to_string()
            current = current.get_next_node()
        print()

    def add_head(self, head):
        if self.size == 0:
            self.head = head
        elif self.size == 1:
            self.tail = self.head
            self.head = head
            self.head.set_next_node(self.tail)
        elif self.size >= 2:
            head.set_next_node(self.head)
            self.head = head

    def add_tail(self, tail):
        if self.size == 0:
            self.head = tail
            return
        self.tail = tail
        self.head.set_next_node(tail)