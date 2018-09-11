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
        while cur_node.next!=None:
            cur_node=cur_node.next
        cur_node.next=new_node
        return cur_node.data
       
    def reverse(self):
        next_node=None
        prev_node=None
        cur_node=self.head.next
        while (cur_node!=None):
            next_node=cur_node.next
            cur_node.next=prev_node
            prev_node=cur_node
            cur_node=next_node
        self.head.next=prev_node
        #return prev_node
    
    def display(self):
        elements=[]
        cur_node=self.head
        while (cur_node.next!=None):
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
lst1.reverse()
lst1.display()