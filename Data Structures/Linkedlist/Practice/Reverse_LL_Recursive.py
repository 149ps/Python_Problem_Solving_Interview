class node:
    def __init__(self,data=None):
        self.next=None
        self.data=data
    
class linked_list:
    def __init__(self):
        self.head=node()
    
    def append(self,data):
        new_node=node(data)
        cur_node=self.head
        while (cur_node.next!=None):
            cur_node=cur_node.next
            print(cur_node.data)
        cur_node.next=new_node
        
    
    def display(self):
        elements=[]
        cur_node=self.head
        while(cur_node.next!=None):
            cur_node=cur_node.next
            elements.append(cur_node.data)
        print(elements)
    
    def reverseRecursive(self,prev_node,cur_node):
        if cur_node:
            self.reverseRecursive(cur_node,cur_node.next)
            print(cur_node.data)
            cur_node.next=prev_node
        else:
            self.head.next=prev_node
        
        
lst1=linked_list()
lst1.append(1)
lst1.append(3)
lst1.append(5)
lst1.append(7)

lst1.reverseRecursive(None,lst1.head)

            
        
         