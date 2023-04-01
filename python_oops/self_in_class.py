'''
Inside the class body self refers to the current class object and
it can be used to access or modify the properties and call the functions inside the class.
'''
'''
self is not a keyword, its simply the name of the first parameter of class function. 
it can have some other name but naming convention suggests using 'self'.
'''

class Rectangle:
    def area(self):
        length = self.length
        breadth = self.breadth
        self.area_ = self.length * self.breadth
        print("Area of rectangle==>",self.area_)

rec_obj = Rectangle()
rec_obj.length =2
rec_obj.breadth =3
rec_obj.area()