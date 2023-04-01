'''
class is a collection of objects unlike the primitive data structure,
classes are data structure that are user define they make code more manageable.
and we declare the like below:-
'''
class Person:   # class ==> class is a keyword for class defining
    pass        # Person ==> the name of the class
                # pass ==> pass is keyword that fill the empty block of code to avoid the exception throw.

'''
object creation ==> object is an instance created from a class and
there is no memory allocation until we create the objects.
'''
pers_obj = Person() ## object creation


# set the prooperties
class Person:
    def introduce(self):
        print("I'm," ,self.name, "and I'm", self.age,"year's old")
pers_obj = Person()
pers_obj.name = "Nitesh"  # value set
pers_obj.age = 25         # value set
pers_obj.introduce() ## uses the properties of class object via the self parameter

## the class function must always have at least 1 parameter
