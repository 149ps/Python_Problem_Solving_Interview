class node:
    def __init__(self,data=None):
        self.data=data
        self.next=None

class linked_list:
    def __init__(self):
        self.head=node()
        self.sentinel=node()
        self.head.next=self.sentinel
    
    def append(self,data):
        new_node=node(data)
        new_node.next=self.sentinel
        cur_node=self.sentinel
        while cur_node.next:
            cur_node=cur_node.next
        cur_node.next=new_node

    def display(self):
        elements=[]
        cur_node=self.head
        while cur_node.next:
            cur_node=cur_node.next
            elements.append(cur_node.data)
        print(elements)
    
    def length(self):
        count=0
        cur_node=self.head
        while cur_node.next:
            count+=1
            cur_node=cur_node.next
        return count
        
         
lst1=linked_list()
lst1.display()
lst1.append(1)
lst1.append(3)
lst1.append(5)
lst1.append(7)
lst1.display()
print(lst1.length())
