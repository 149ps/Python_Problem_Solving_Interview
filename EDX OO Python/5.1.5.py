class Person:
    def __init__(self, name, age, father=None, mother=None):
        self.name = name
        self.age = age
        self.father = father
        self.mother = mother
    
class Dad:
    def __init__(self,name,father=None,mother=None):
        self.name=name
        self.age=53
        self.father=None
        self.mother=None
        
       
        

class Mom:
    def __init__(self,name,mother=None,father=None):
        self.name=name
        self.age=53
        self.father=None
        self.mother=None
        


#Write your code here!
george_p=Person("George P. Burdell",25,Dad("Mr. Burdell"),Mom("Mrs. Burdell"))


print(george_p.name)
print(george_p.mother.name)
print(george_p.father.name)