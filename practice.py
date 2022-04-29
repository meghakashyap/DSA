class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
    
class SLL:
    def __init__(self):
        self.head=None
    
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
n2.next=n4
n4.next=n3
l.display()