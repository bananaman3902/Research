# I clarified the purpose of each function to apply the seperation of concerns principle
class Average:
    # define a function to intitialize the list and average value. this function uses DRY which allows you to use this same function for a given list regardless of whether the list has items in it or not
    def __init__(self,valuelist):
        self.valuelist=valuelist
        total=0
        for value in valuelist:
            total=total+value
        if len(valuelist)!=0:
            self.average=total/len(valuelist)
        else:
            self.average=0
    
    # define a function to add a value to the list
    def add_value(self,value):
        total=self.average*len(self.valuelist)
        self.valuelist.append(value)
        self.average=(total+value)/len(self.valuelist)
    
    # define a function to print the values
    def print_value(self):
        print(self.average)

# call the functions and print the returning values
inst=Average([2])
inst.add_value(1)
inst.print_value()
