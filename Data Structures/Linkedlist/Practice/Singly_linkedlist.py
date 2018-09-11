class node:
    def __init__(self,data=None):
        self.data=data
        self.next=None
        
class linked_list:
    def __init__(self):
        self.head=node()
        
    def append(self,data):
        new_node=node(data)
        cur_node=self.head
        while (cur_node.next!=None):
            cur_node=cur_node.next
        cur_node.next=new_node
     
    def length(self):
        cur_node=self.head
        count=0
        while(cur_node.next!=None):
            cur_node=cur_node.next
            count=count+1
        return count
    
    def display(self):
        elements=[]
        cur_node=self.head
        while cur_node.next!=None:
            cur_node=cur_node.next
            elements.append(cur_node.data)
        print(elements)
    
    def getData(self,index):
        if index>=self.length():
            print("Inedex is out of Range.")
            return None
        cur_index=0
        cur_node=self.head
        while True:
            cur_node=cur_node.next
            if cur_index==index:
                return cur_node.data
            else:
                cur_index+=1
    
    def deleteNode(self,index):
        if index>=self.length():
            print("There is no node at ", index)
            return None
        cur_index=0
        cur_node=self.head
        while True:
            last_node=cur_node
            cur_node=cur_node.next
            if cur_index==index:
                last_node.next=cur_node.next
                print(str(cur_node.data) + " is deleted." )
                print("Now " + str(last_node.data) + " is pointing to " + str(cur_node.next.data) + " instead of " + str(cur_node.data))
                return 
            cur_index+=1
                
                
        
        

lst1=linked_list()
lst1.display()
lst1.append(1)
lst1.append(3)
lst1.append(5)
lst1.append(7)
lst1.display()
print(lst1.length())

lst1.deleteNode(2)
lst1.display()




            
            