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
    
    def get(self,index):
        if index>=self.length():
            return None
        cur_index=0
        cur_node=self.head
        while True:
            cur_node=cur_node.next
            if cur_index==index:
                return cur_node.data
            cur_index+=1
    
    def deleteNode(self,index):
        if index>=self.length():
            print("Error: Index is out of range.")
            return
        cur_index=0
        cur_node=self.head
        while True:
            last_node=cur_node
            cur_node=cur_node.next
            if cur_index==index:
                last_node.next=cur_node.next
                print(cur_node.data,"is deleted")
                return
            cur_index+=1
        
            
    def length(self):
        cur_node=self.head
        count=0
        while cur_node!=None:
            count=count+1
            cur_node=cur_node.next
        return count
    
    def deleteAtbegin(self):
        """
        cur_node=self.head
        last_node=cur_node.next
        cur_node.next=last_node.next
        return """
        cur_node=self.head
        cur_node.next=cur_node.next.next
        return
    
    def deleteAtlast(self):
        cur_node=self.head
        while cur_node.next.next!=None:
            cur_node=cur_node.next
        cur_node.next=None
        return
    
    def moveTofront(self):
        cur_node=self.head
        first_node=cur_node
        second_node=cur_node.next
        while cur_node.next.next!=None:
            cur_node=cur_node.next
        cur_node.next.next=second_node
        first_node.next=cur_node.next
        cur_node.next=None
        return
                
    

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
lst1.moveTofront()
lst1.display()
