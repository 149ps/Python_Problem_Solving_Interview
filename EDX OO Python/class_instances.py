class Person:
    def __init__(self,name,eyecolor,age):
        self.name=name
        self.eyecolor=eyecolor
        self.age=age
    
class Name:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
        
myperson=Person(Name("Parth","Shah"),"Black",23)
print(myperson.name.lastname,myperson.name.firstname)
print(myperson.age)
print(myperson.eyecolor)


