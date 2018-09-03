class node:
    def __init__(self,data=None):
        self.data=data
        self.next=None

class linked_list:
    def __init__(self):
        self.head=node()
    
    def insertAtBegin(self,data):
        new_node=node(data)
        cur_node=self.head
        if not cur_node.next==None:
            new_node.next=cur_node.next
        cur_node.next=new_node
    
    
    def append(self,data):
        new_node=node(data)
        cur_node=self.head
        while (cur_node.next!=None):
            cur_node=cur_node.next
        cur_node.next=new_node
        
    def insertAtEnd(self,data):
        new_node=node(data)
        cur_node=self.head
        while (cur_node.next!=None):
            cur_node=cur_node.next
        cur_node.next=new_node
    
    def insertAnywhere(self,data):
        new_node=node(data)
        cur_node=self.head
        cur_node=cur_node.next
        while(cur_node.data!=3):
            cur_node=cur_node.next
        new_node.next=cur_node.next
        cur_node.next=new_node
    
    def display(self):
        elements=[]
        cur_node=self.head
        while(cur_node.next!=None):
            cur_node=cur_node.next
            elements.append(cur_node.data)
        print(elements)    
        
        
    

lst1=linked_list()
lst1.display()
lst1.append(1)
lst1.append(3)
lst1.append(5)
lst1.append(7)
lst1.display()
lst1.insertAtBegin(2)
lst1.display()
lst1.insertAtEnd(21)
lst1.display()
lst1.insertAnywhere(4)
lst1.display()