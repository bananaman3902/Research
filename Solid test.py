'''
SOLID is a set of principles for writing better software code. It helps make code easier to understand, change, and maintain over time. 
Each letter in "SOLID" stands for a principle:

S: Single Responsibility Principle (SRP) - Each part of the code should do only one thing.
O: Open/Closed Principle (OCP) - Code should be open to adding new features but closed to changing existing ones.
L: Liskov Substitution Principle (LSP) - Substituting one part of code with another shouldn't break anything.
I: Interface Segregation Principle (ISP) - Code should use small and specific parts, rather than big and general ones.
D: Dependency Inversion Principle (DIP) - High-level parts of code shouldn't depend directly on low-level parts.

SOLID is important because it helps create code that's easier to work with, adaptable to changes, and less likely to have errors. 
It promotes good practices for designing software that's flexible, maintainable, and of high quality.
'''

# Single Responsibility Principle (SRP)
# Each class has one specific role
class Pillar():
    # Single Responsibility Principle (SRP): Bowl returns the established height of the pillar
    def __init__(self,height):
        self.height=height
    def height(self):
        return self.height
class Dome():
    # Single Responsibility Principle (SRP): Bowl returns the established radius of the dome
    def __init__(self,radius):
        self.radius=radius
    def radius(self):
        return self.radius
class Bowl():
    # Single Responsibility Principle (SRP): Bowl returns the established volume of the bowl
    def __init__(self,volume):
        self.volume=volume
    def volume(self):
        return self.volume
class Main():
    # Single Responsibility Principle (SRP): Main runs the code
    def run(self):
        pillar=Pillar(20)
        dome=Dome(10)
        bowl=Bowl(5)

        print("Pillar height:",pillar.height())
        print("Dome radius:",dome)
        print("Bowl volume:",bowl)

main=Main()
main.run()
