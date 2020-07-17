import turtle
from tkinter import messagebox, simpledialog, Tk

# Goal: Write a Python program that asks the user whether they want to
#       draw a triangle, square, or circle and then draw that shape.

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    
    
    # Make a new turtle
    ethan = turtle.Turtle()
    # Ask the user what shape they want to draw and store it in a variable
    shp = simpledialog.askstring(None, 'What kind of shape do you want to draw?')
    # Draw the shape requested by the user using if-elif-else statements
        
    if shp == 'square':
        ethan.penup()
        ethan.goto(200,200)
        ethan.pendown()
        ethan.speed(1)
        ethan.forward(100)
        ethan.right(90)
        ethan.forward(100)
        ethan.right(90)
        ethan.forward(100)
        ethan.right(90)
        ethan.forward(100)
        messagebox.showinfo(None, 'You have fantastic choice in shapes.')
        exit()
            
    else:
        ethan.penup()
        ethan.goto(200,200)
        ethan.pendown()
        ethan.speed(1)
        ethan.forward(100)
        ethan.right(120)
        ethan.forward(100)
        ethan.right(120)
        ethan.forward(100)
        messagebox.showinfo(None, 'I hope that was right, I,m not good at shapes.')
                
    # Call the turtle .done() method
    
    ethan.done()
    window.mainloop()   