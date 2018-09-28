class node:
    def __init__(self,data=None):
        self.data=data
        self.next=None
"""    
class linked_list:
    def __init__(self):
        self.head=node()
"""    
class stack:
    def __init__(self):
        self.head=node()
        
    def push(self,item):
        new_item=node(item)
        cur_pointer=self.head
        new_item.next=cur_pointer.next
        cur_pointer.next=new_item
    
    def pop(self):
        if self.isempty():
            raise Exception("Stack Empty")
        cur_pointer=self.head.next
        self.head.next=cur_pointer.next
        return cur_pointer
    
    def isempty(self):
        if self.head.next==None: return True
    
    def display(self):
        elements=[]
        cur_node=self.head
        while cur_node.next!=None:
            cur_node=cur_node.next
            elements.append(cur_node.data)
        print(elements)

s=stack()

s.push(1)
s.push(2)
s.push(5)
s.pop()
s.display()
s.isempty()

    
    
        
    
        
            
        
        
    
    
    

