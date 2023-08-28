# the Input() function creates a popup that takes an input from the user and sets it as the value for the variable 'a'
a=float(input("How tall is the longest length of a adult giraffe's neck (in meters) "))
if(a>2 and a<3):
    # as you can't use the + sign with strings and floats, i converted the a variable to a string with str()
    print(str(a)+"m is correct")
else:
    print("incorrect")
