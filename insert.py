class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
    
class SLL:
    def __init__(self):
        self.head=None
    
    def begining(self,data):
        nb = Node(data)
        nb.next=self.head
        self.head=nb
        
    def end(self,data):
        ne = Node(data)
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=ne
        
    def position(self,pos,data):
        np = Node(data)
        temp = self.head
        for i in  range(pos-1):
            temp=temp.next
        np.data=data
        np.next=temp.next
        temp.next=np
        
        
    
    def display(self):
        temp=self.head
        
        if temp is None:
            print("Empty")
            
        while temp:
            print(temp.data,"-->",end=" ")
            temp=temp.next

        
    
l=SLL()
n1=Node(10)
l.head=n1
n2=Node(50)
n1.next=n2
n3=Node(90)
n4=Node(70)
n2.next=n3
n3.next=n4

l.begining(56)
l.begining(78)

l.end(199)

l.position(4,29)
l.position(6,1)

l.display()