MAX=4
class stack:
    
    def __init__(self):
        self.s=[]
    
    def isEmpty(self):
        return len(self.s)==0
    
    def push(self,item):
        if len(self.s)==4:
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
s.push(5)
print(s.push(4))
print(s.push(10))
