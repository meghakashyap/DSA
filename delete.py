class Node:
    def  __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class linked_list:
    def __init__(self):
        self.head=None
        
    def delete_begining(self):
        temp=self.head
        self.head=temp.next
        temp.next=None
        
        
        
    def delete_end(self):
        temp=self.head.next
        prev=self.head
        while temp.next is not None:
            temp=temp.next
            prev=prev.next
        prev.next=None
    
    def delete_position(self,pos):
        temp=self.head.next
        prev=self.head
        for i in range(1,pos-1):
            temp=temp.next
            prev=prev.next
        prev.next=temp.next
        # temp.next=None


  
    def display(self):
        temp=self.head
        if temp is None:
            print('Empty')
        while temp:
            print(temp.data,"-->",end=" ")
            temp=temp.next
            
        

L=linked_list()
n1=Node(10)
L.head=n1
n2=Node(20)
n1.next=n2 
n3=Node(30)
n2.next=n3
n4=Node(40)
n3.next=n4

# L.delete_begining()
# L.delete_end()
L.delete_position(2)
L.display()