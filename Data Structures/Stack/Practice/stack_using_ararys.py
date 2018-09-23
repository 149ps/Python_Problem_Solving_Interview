class stack:
    
    def __init__(self):
        self.s=[]
    
    def isEmpty(self):
        return len(self.s)==0
    
    def push(self,item):
        MAX=4
        if len(self.s)==MAX:
            raise Exception("Stack Overflow")
        else:
            self.s.append(item)
            return self.s
        
    def pop(self):
        if self.isEmpty():
            raise Exception("Stack Empty")
        self.s.pop()
        return self.s
        
    def display(self):
        return self.s
    
s=stack()
s.push(1)
s.push(2)
print(s.push(4))
print(s.pop())

        
        