class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Queue:
    def __init__(self):
        self.head = None
        self.last = None
    def isempty(self):
        if self.head == None:
            return True
        else:
            return False
    def push(self, data):
        if self.head == None:
            self.head = Node(data)
            self.last = self.head
        else:
            newnode = Node(data)
            self.last.next = newnode
            self.last = newnode
    def pop(self):
        if self.isempty():
            return None
        else:
            x = self.head.data
            if self.head == self.last:
                self.head = None
                self.last = None
                return x
            self.head = self.head.next
            return x
