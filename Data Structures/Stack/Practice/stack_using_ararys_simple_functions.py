stack=[]
top=-1
def push(item):
    stack.append(item)
    return stack
def pop():
    del stack[-1]
    return stack

def isEmpty():
    if len(stack)==0:
        return True
    else:
        return False

def size():
    return len(stack)

push(1)
push(2)
print(stack)
pop()

print(stack)
print(isEmpty())
    
