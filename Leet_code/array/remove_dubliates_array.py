class Node:
    def __init__(self, data=None,):
        self.data = data
        self.next = None
class Slinkedlist:
    def __init__(self,head=None):
        self.head = None
    def linkedlist_print(self,):
        print_ = self.head
        while print_ is not None:
            print(print_.data)
            print_ = print_.next
    def atend(self,data):
        NewNode = Node(data)
        if self.head is None:
            self.head = NewNode
            return
        last = self.head
        while last.next: # True
            last = last.next
        last.next = NewNode
list_ = Slinkedlist()
list_.head = Node("Mon")
e2 = Node("Tue")
e3 = Node("wed")
list_.head.next = e2 # Link first Node to second node
e2.next = e3  # Link second Node to third node

list_.atend("Thu")
list_.linkedlist_print()
