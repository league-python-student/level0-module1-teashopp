# Write a Python program that asks the user for the radius of a circle.
# Next, ask the user if they would like to calculate the area or circumference of a circle.
# If they choose area, display the area of the circle using the radius.
# Otherwise, display the circumference of the circle using the radius.

#Area = πr^2
#Circumference = 2πr 


from tkinter import simpledialog, messagebox, Tk
import math


if __name__ == '__main__':
    window = Tk()
    window.withdraw()


re = simpledialog.askinteger(None, 'Give me an integer:')

ra = simpledialog.askstring(None, 'Would you like to find the area or circumference?')


if ra == 'area':
    messagebox.showinfo(None, 'The area of the circle is ' + str( math.pi*int(re)**2 ) )
    
else:
    messagebox.showinfo(None, 'The circumference of the circle is ' + str(math.pi*int(re)*2))
    
    
    
window.mainloop()