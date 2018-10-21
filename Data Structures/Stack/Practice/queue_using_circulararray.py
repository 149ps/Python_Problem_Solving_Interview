class queue:
    
    def __init__(self):
        self.a=[]
        self.front=0
        self.rear=0
        self.n=10
    
    def enqueue(self,item):
        self.rear=(self.rear+1) % self.n
        if (self.front==self.rear):
            raise Exception('Queue is full')
            if self.rear==0:
                self.rear=self.n-1
            else:
                self.rear-=1
        else:
            self.a.append(item)
            return item
            
    def dequeue(self):
        if (self.front==self.rear):
            raise Exception("Queue is empty")
        else:
            self.front=(self.front+1) % self.n
            item=self.a[self.front-1]
            self.a.remove(item)
        return item
    
    def display(self):
        print(self.a)

q=queue()
q.enqueue(1)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
q.enqueue(7)
q.display()
print(q.dequeue())
q.display()

    
    

            