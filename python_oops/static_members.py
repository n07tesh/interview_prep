'''
static functions and properties are declared in the class body but dnot need created instance for their usage.
'''
'''
static properties  store the value about the class. the value is specific for the class.
'''

#className.memberName = value

class car:
    def __init__(self,modelValue):
        print("object created")
        self.model = modelValue

        # increment static member:
        car.carsCount +=1

car.carsCount = 0

print("initial cars count",car.carsCount)

obj1 = car("BMW")
obj2 = car("Ford")
obj3 = car("Toyata")
print("Final cars count",car.carsCount)


#static functions



