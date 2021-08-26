import re
from tkinter import *
from tkinter import messagebox
window = Tk()
window.title("EMAIL VALIDATOR")
window.geometry('450x400')
lbl = Label(window, text="ENTER YOUR EMAIL : ")
lbl.grid(column=0, row=0)
txt = Entry(window,width=25)
txt.grid(column=1, row=0)
email=txt.get()
regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
def check(email):
    if(re.search(regex, email)):
        return "VALID"
    else:
        return "INVALID"

def clicked():
    res = "THE EMAIL "  + txt.get() + " IS " + check(txt.get())
    messagebox.showinfo('RESULT', res)
    

btn = Button(window, text="CHECK", command=clicked)
btn.grid(column=3, row=0)
window.mainloop()
