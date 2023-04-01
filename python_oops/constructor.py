'''
constructor is used to create objects. it is a function that executes when objects is created.
'''
# syntax
def __init__(self):
    pass

#default constructor
'''
default constructor does not accept any arguments.
it can be used without defining it.
it defined it sets default values to class members. 
'''

class Person:
    pass
person = Person()
person.name = "ritesh"
person.age = 23
print("Name",person.name)
print("Age",person.age)


#parameterized constructor
'''
the parameterized constructor accepts parameter which usually are used to set value for the objects members.
'''
class Person:
    def __init__(self,name,age):
        print("object creation")
        self.name = name
        self.age = age

    def printData(self):
        print('Name:',self.name)
        print('Age:',self.age)

person_obj =Person('nitesh',25)
person_obj.printData()