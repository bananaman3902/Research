# SRP each class is responsible for only a single function
# open/closed. the script is closed to changing the values that make up the pre established shapes while being open to adding new objects with the same design
# LSP each shape can substitute each other
# ISP independednt size classes

# DIP base class for dictionary
class size_dip():
    def __init__(self,size):
        self.size=size
    def size_value(self):
        return self.size

class Pillar(size_dip):
    # Single Responsibility Principle (SRP): Pillar returns the established height of the pillar
    def __init__(self,height):
        self.height=height
    def size_value(self):
        return self.height

class Dome(size_dip):
    # Single Responsibility Principle (SRP): Dome returns the established radius of the dome
    def __init__(self,radius):
        self.radius=radius
    def size_value(self):
        return self.radius

class Bowl(size_dip):
    # Single Responsibility Principle (SRP): Bowl returns the established volume of the bowl
    def __init__(self,volume):
        self.volume=volume
    def size_value(self):
        return self.volume

class Main():
    # Single Responsibility Principle (SRP): Main runs the code
    def run(self):
        pillar=Pillar(20)
        dome=Dome(10)
        bowl=Bowl(5)

        print("Pillar height:",pillar.size_value())
        print("Dome radius:",dome.size_value())
        print("Bowl volume:",bowl.size_value())

main=Main()
main.run()
