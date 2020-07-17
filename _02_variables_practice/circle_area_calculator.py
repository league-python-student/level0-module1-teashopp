import turtle
from tkinter import simpledialog, Tk
import math

# Goal: Write a Python program that asks the user for the radius 
#       of a circle and displays the area of that circle.
#       The formula for the area of a circle is πr^2.
#       See example image in package to check your output.

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    
    # Ask the user for the radius in pixels and store it in a variable
    # simpledialog.askinteger()
    num = simpledialog.askinteger(None, 'Give me an integer:')
    # Make a new turtle
    ethan=turtle.Turtle()
    ethan.width(10)
    ethan.speed(5)
    ethan.color('blue')
    # Have your turtle draw a circle with the correct radius
    # my_turtle.circle()
    ethan.circle(num, 360, 50)#
    # Call the turtle .penup() method
    ethan.penup()
    # Move your turtle to a new x,y position using .goto()
    ethan.goto(100, 100)
    # Calculate the area of your circle and store it in a variable, you can use math.pi
    area = math.pi*num**2
    # Write the area of your circle using the turtle .write() method
    # myTurtle.write(arg="area = " + str(area), move=True, align='left', font=('Arial',8,'normal'))
    ethan.write('area = '+str(area), True, 'left', ('Arial', 8, 'normal'))
    # Hide your turtle
    ethan.hideturtle()
    # Call turtle.done()
    turtle.done()
    window.mainloop()