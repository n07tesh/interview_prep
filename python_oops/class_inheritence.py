'''
class inheritence is way to extend the class.
the new class (child class) builds or overwritten logic from the parent class (super class).
'''

# class childclass(parentclass):
#     pass
'''
overwritten method is a method that has been inherited from the parent buts its logic is changed in the child.
'''
class ParentClass:
    pass
    def funName(args):
        pass # code
class childclass(ParentClass):
    def funName(args):
        pass # overwritten method


class vehicle:
    def vehcleprice(self,months):
        pass

class Second(vehicle):
    def vehcleprice(self, months):
        return months * 10

scooter = Second()
print(scooter.vehcleprice(5))

'''
A child's class constructor can call parents class constructor via the ***super keyword***.
'''
# multilevel inheritence
'''
A class can inherit a class that inherits other class. A long chain can be formed.
'''
class A:
    def getA(self):
        return 'A'
class B:
    def getB(self):
        return 'B'
class C(A,B):
    def getC(Self):
        return 'C'
obj = C()
print(obj.getA())
print(obj.getB())
print(obj.getC())
























































