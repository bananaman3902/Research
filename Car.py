'''
class Car:
    def __init__(self,color):
        self.color=color

    def move(self):
        action=self.color+' drive'
        return action
carColor=input('color?')
mycar=Car(color=carColor)
print(mycar.move())
'''
# I clarified the purpose of each function to apply the seperation of concerns principle
class Car:
    # define a function to intitialize the cars variables. this function uses DRY which allows you to use this same function for multiple types of cars
    def __init__(self,color,make,model,year):
        self.color=color
        self.make=make
        self.model=model
        self.year=year

    # define a function to return the car accelerating
    def accelerating(self):
        return(self.color,self.make,self.model,self.year,' accelerating')

    # define a function to return the car braking
    def braking(self):
        return(self.color,self.make,self.model,self.year,' braking')
    
    # define a function to return the car turning left
    def turn_left(self):
        return(self.color,self.make,self.model,self.year,' turning left')
    
    # define a function to return the car turning right
    def turn_right(self):
        return(self.color,self.make,self.model,self.year,' turning right')

# get input from user for the specifications of car
carColor=input('color?')
carMake=input('make?')
carModel=input('model?')
carYear=input('year?')

# call the functions and print the returning values
inst1=Car(carColor,carMake,carModel,carYear)
inst2=Car('red','nissan','sentra','1991')
print(inst1.accelerating())
print(inst2.accelerating())
print(inst2.turn_left())
print(inst2.turn_right())
print(inst1.braking())
print(inst2.braking())
print('inst1 wins')
