a=input("enter option 1-3")
# this script tests and demonstrates if elif and else conditions
if(float(a)==1):
    # if this bool is true
    print("menu 1")
elif(float(a)==2):
    # if the first bool is false and this bool is true
    print("menu 2")
elif(float(a)==3):
    # if the first bool and second bool is false and this bool is true
    print("menu 3")
else:
    # if all the above bools are false
    print("invalid")
