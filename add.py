
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

    
class Linked_list:
    def __init__(self):
        self.head = None
    
    
    def insert_at_begin(self,data):
        nb = Node(data)
        nb.next=self.head
        self.head=nb
    
    def insert_at_end(self,data):
        ne = Node(data)
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = ne
    
    def position(self,pos,data):
        np = Node(data)
        temp = self.head
        for i in range(pos-1):
            temp = temp.next
        np.data=data
        np.next=temp.next
        temp.next=np
        
    def display(self):
        if self.head is None:
            print("Linked list is Empty !")
        else:
            temp = self.head
            while temp is not None:
                print(temp.data,"-->",end="  ")
                temp = temp.next



l = Linked_list()
n1 = Node(20)
l.head=n1
n2 = Node(30)
l.head.next = n2
n3 = Node(40)
n2.next = n3
n4 = Node(50)
n3.next = n4


l.insert_at_begin(5)

l.insert_at_end(29)
l.insert_at_end(59)

l.position(2,115)
l.display()
