# tkinter is the standard method for gui coding
from tkinter import *

def button_pressed():
    print("function called")

# this function is only called when the program is run directly by the python interpreter, which is mostly just a part of the standard design of python gui code
if __name__=="__main__":
    gui=Tk()
    gui.configure(background="light blue")
    # this sets the name on the title bar
    gui.title("test_gui")
    # this sets the default size of the window
    gui.geometry("450x500")

    # this is just a testing label
    text=Label(gui,text="text",bg="light blue",height=4,width=14)
    # this places the text on a grid, which can prevent overlapping of different objects. grids are very effective at positioning objects, and for the padding, while the value given for padding will be used in both directions, you can use a tuple to give each side a different value
    text.grid(row=0,column=2,padx=175,pady=(125,50))
    # this is just a testing button
    button=Button(gui,text="call function",bg='white',command=lambda:button_pressed(),height=4,width=14)
    # this sets the button on the same grid, but below the text
    button.grid(row=1,column=2)
    
    gui.mainloop()
    # mainloop() is called when the application is ready to run, meaning that the application will be run with an infinite loop from the start of the function to the mainloop() for as long as the window is open
