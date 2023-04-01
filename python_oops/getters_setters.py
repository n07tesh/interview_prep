'''
getters return the value of a property.
They also make small modification of the returnal result.
'''
class square:
    __side = 5
    def get_side(self):
        return self.__side # private member
# __ prefix are meant to be accessed only inside the class body.
sqobj = square()
print(sqobj.get_side())

'''
setters allow for a property to be modified. They are important since they can provide the validation before a value is set.
'''
class Person:
    def get_age(self):
        return self.__age
    def set__age(self,value):
        if value < 0:
            value = 0
        self.__age = value
obj = Person()
obj.set__age(20)
print(obj.get_age())

obj2 = Person()
obj2.set__age(-10)
print(obj2.get_age())

