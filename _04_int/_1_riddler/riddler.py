'''
* Write a python program that asks the user a minimum of 3 riddles.

* You can look at riddles.com if you don't already know any riddles.

* Collect the response of each riddle from the user and compare their
  answers to the correct answer. 

* Use a variable to keep track of the correctly answered riddles

* After all the riddles have been asked, tell the user how many they got correct
'''

from tkinter import messagebox, simpledialog, Tk

if __name__ == '__main__':
    window = Tk 
    window.withdraw()
    
    correct = 0
    
    
    guess0 = simpledialog.askstring(None, 'Mr and Mrs. Smith have six daughters. Each daughter has one brother. How many children to Mr and Mrs. Smith have?')
    if guess0 = 'seven' or '7':
        messagebox.showinfo(None, 'Correct!')
        correct += 1
    else:
        messagebox.showinfo(None, 'Incorrect; they have seven, six daughters and one son.')
    
        
    guess2 = simpledialog.askstring(None, 'I have one color but infinite sizes. I stay stuck to the floor, but fly so easily. I do you no harm and I feel no pain. What am I?')
    if guess2 = 'a shadow' or 'shadow':
        messagebox.showinfo(None, 'Correct!')
        correct += 1
    else:
        messagebox.showinfo(None, 'Incorrect; I am a shadow.')
        
    
    guess3 = simpledialog.askstring(None, 'If eleven plus two equals one, what does nine plus five equal?')
    if guess3 = 'two' or '2':
        messagebox.showinfo(None, 'Correct!')
        correct += 1
    else:
        messagebox.showinfo(None, 'Incorrect; nine plus five would equal two (on a clock).')
    
    
    if correct >= 2:
        messagebox.showinfo(None, 'Congratulations, you,ve scored ' + correct + ' points!')
    elif correct = 1:
        messagebox.showinfo(None, 'Ooh, you only scored one point. Better luck next time!')
    else:
        messagebox.showinfo(None, 'You didn,t get any right. Try harder.')    
        
        
window.mainloop()