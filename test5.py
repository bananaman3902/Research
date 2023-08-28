a=input("enter: ")

# isdigit() checks if the variable a can function as a number
if(a.isdigit()):
    if(float(a)>0):
        print('pos')
    elif(float(a)==0):
        print('0')
    elif(float(a)<0):
        print('neg')
else:
    print('enter number plz')
