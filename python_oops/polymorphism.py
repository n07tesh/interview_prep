'''
Polymorphism means having many forms in oops refers to the function having same name and different functionalities.
'''
class Audi:
    def description(self):
        print('This is the description function of class AUDI')
class BMW:
    def description(self):
        print('This is the description function of class BMW')
audi = Audi()
bmw = BMW()
for car in (audi,bmw):
    car.description()