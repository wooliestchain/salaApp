from tkinter import *
from tkinter import messagebox
from suds.client import Client


window = Tk()
window.title("Home")
window.geometry('925x700+350+20')
window.configure(bg='#F4EBD5')
window.resizable(False,False)


def on_first_button():
    first_lab = Label(window, text="First")
    first_lab.place(x=300, y=100)

def on_second_button():
    first_lab = Label(window, text="First")
    first_lab.place(x=300, y=200)

slide_bar = Frame(window, width=200,height=800, bg='#666666')
slide_bar.place(x=0, y=0)

imgs = PhotoImage(file='relogin.png')
Label(slide_bar, image=imgs, border=0, bg='white').place(x=40, y=10)

first_button = Button(slide_bar,width=25, height=0, text="Premier", fg='white', bg='black', command=on_first_button)
first_button.place(x=5, y=100)



second_button = Button(slide_bar, width=25, height=0, text="Second", fg='white', bg='black', command=on_second_button)
second_button.place(x=5, y=200)

window.mainloop()
