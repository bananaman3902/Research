# object-oriented programming
# I clarified the purpose of each function to apply the seperation of concerns principle
class Calculator:
    # defined a function to initialize the variables. this function uses DRY which allows you to use this same function for multiple equations
    def __init__(self,a,b):
        self.a=a
        self.b=b

    # defined a function to add together the given two variables
    def add(self):
        return self.a+self.b

    # defined a function to subtract the second given variable from the first given variable
    def subtract(self):
        return self.a-self.b

    # defined a function to multiply the two given variables with eachother
    def multiply(self):
        return self.a*self.b

    # defined by a function to divide the first given variable from the second given variable
    def divide(self):
        return self.a/self.b

# the class is called and it's variables are initialized
calculator=Calculator(4,5)

# call the functions
print(calculator.add())
print(calculator.subtract())
print(calculator.multiply())
print(calculator.divide())
