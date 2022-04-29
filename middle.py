class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

    
class Linked_list:
    def __init__(self):
        self.head = None
    
    def display(self):
        if self.head is None:
            print("Linked list is Empty !")
        else:
            temp = self.head
            c = 1
            while temp is not None:
                print(temp.data,"-->",end="  ")
                temp = temp.next
                c+=1
            count = c/2
            
            print()
            



n1 = Node(20)
Linked_list.head=n1
n2 = Node(30)
Linked_list.head.next = n2
n3 = Node(40)
n2.next = n3
n4 = Node(50)
n3.next = n4
Linked_list.display()

