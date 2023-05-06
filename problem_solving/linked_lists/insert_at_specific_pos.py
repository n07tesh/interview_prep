class Node:
    def __init__(self,data=None,next=None):
        self.data  = data
        self.next = next

class LinkedList:
    def __init__(self,):
        self.head = None
    
    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data)
            return
        # node = Node(data)
        # self.head = node
        itr = self.head
        list_ = ''
        while itr.next:
            list_ += str(itr.data) + '-->'
            itr = itr.next
        itr.next = Node(data)
        print(list_)
        return

    def insert_val(self,data):
        self.head = None
        for _ in data:
            self.insert_at_end(_)
    
    def insert_at(self,data):
        node = Node(data)
        self.head = node

        itr = self.head
        list_ = ''
        while itr:
            list_ += str(itr.data) + '-->'
            itr = itr.next
            print(list_)
    
    def get_length(self,):
        count = 0
        itr = self.head
        while itr:
            itr = itr.next
            count +=1
        return count

    def insert_at_pos(self,index,data):
        if index < 0 or index > self.get_length():
            raise Exception('Invalid index')
        if index == 0:
            self.insert_at(data)
            return
        count = 0
        itr = self.head
        list_ = ''
        while itr:
            list_ += str(itr.data) + '-->'
            if count == index-1:
                node = Node(data,itr.next)
                itr.next = node
                break
            itr = itr.next
            count +=1
        print(list_)
if __name__=='__main__':
    ll = LinkedList()
    ll.insert_val([1,3,5,7,9])
    # ll.insert_at_pos(0,1)
    # ll.insert_at_pos(1,2)
    # ll.insert_at_pos(2,3)
    ll.insert_at_pos(3,4)
    print()