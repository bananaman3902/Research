# SRP each class is responsible for only a single function
# open/closed. the script is closed to changing the values that make up the pre established shapes while being open to adding new calculations with the same design
# LSP each maths properties can substitute each other
# ISP independednt math classes

# DIP base class for dictionary
class maths_dip():
    def __init__(self,a,b):
        # set the first value
        self.a=a
        # set the second value
        self.b=b
    def calculate(self):
        # this method is abstract and will be overridden by subclasses
        pass

class add(maths_dip):
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def calculate(self):
        # add the two values together and return the result
        return self.a+self.b

class subtract(maths_dip):
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def calculate(self):
        # subtract the second value from the first value and return the result
        return self.a-self.b

class multiply(maths_dip):
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def calculate(self):
        # multiply the two values together and return the result
        return self.a*self.b

class divide(maths_dip):
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def calculate(self):
        # divide the first value by the second and return the result
        return self.a/self.b

# initialize the values and print the returned result
add=add(1,2)
print(add.calculate())

subtract=subtract(1,2)
print(subtract.calculate())

multiply=multiply(1,2)
print(multiply.calculate())

divide=divide(1,2)
print(divide.calculate())
