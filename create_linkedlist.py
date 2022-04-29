class Node:
    def __init__(self,data=None):
        self.data=data
        self.next=None
        
class  single_Linkedlist:
    def __init__(self):
        self.head=None
    
    def display(self):
        if self.head  is None:
            print('LINKED LIST IS EMPTY')
        else:
            temp=self.head
            while temp:
                print(temp.data,"-->",end="  ")
                temp=temp.next
                
L=single_Linkedlist()
n=Node(10)
L.head=n
n1=Node(30)
L.head.next=n1
n2=Node(20)
n1.next=n2
n3=Node(70)
n2.next=n3
L.display()
        
        