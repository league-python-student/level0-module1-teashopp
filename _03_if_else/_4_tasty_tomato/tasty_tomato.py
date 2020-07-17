from tkinter import simpledialog, messagebox, Tk, Canvas

windowWidth = 600
windowHeight = 600

root = Tk()

canvas = Canvas(root, width=windowWidth, height=windowHeight, bg="#DDDDDD")
canvas.grid()

#1. Ask the user what color tomato they would like and save their response   
#   You can give them up to three choices 
response = simpledialog.askstring(None, 'Would you like a red, green, or yellow tomato?')

#2. use if-else statements to draw the tomato in the color that they chose
#   you can modify the code below or draw your own tomato
if response == 'red':
    canvas.create_oval(200, 200, 525, 450, fill='red', outline="")
    messagebox.showinfo(None, 'The classic.')
elif response == 'green':
    canvas.create_oval(200, 200, 525, 450, fill='green', outline="")
    messagebox.showinfo(None, 'Perfect for frying.')
else:    
    canvas.create_oval(200,200,525,450, fill='yellow', outline = '')
    messagebox.showinfo(None, 'A beautiful addition to salads.')



root.mainloop()