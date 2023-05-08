import hashlib
from tkinter import *
from tkinter import messagebox
import ast
import mysql.connector
import bcrypt

window = Tk()
window.title("SignUp")
window.geometry('925x600+300+0')
window.configure(bg='#fff')
window.resizable(False,False)



def signup():
    userentry = user.get()
    passwordentry = code.get()
    hashpass = hashlib.sha256(passwordentry.encode()).hexdigest()
    confirm_password = confirm_code.get()

    conn = mysql.connector.connect(
        host="localhost",
        database="wool",
        username="root",
        password="",
    )


    if passwordentry == confirm_password:
        try:
            cursor = conn.cursor()
            cursor.execute(
            "SELECT * FROM users WHERE username = %s",(userentry,)
            )

            #messagebox.showinfo('Signup', 'Sucessfully sign up')

            result = cursor.fetchone()
            if result is not None:
                messagebox.showinfo('Signup', 'Username already exists')
            else:
                cursor.execute("""
                INSERT INTO users (username, password) VALUES (%s, %s);
                """, (userentry, hashpass))
                conn.commit()
                text_con = Label(frame, text="Enregistrement réussi", fg='black', bg='green', border=0)
                text_con.place(x=200, y=350)


                #On détruit cette fenetre
                window.destroy()
                #On ouvre la fenetre pour continuer vers l'activité suivante
                import comp

        except mysql.connector.Error as e:
            print("Erreur", e)
            raise ValueError("Impossible de se connecter")

    else:
        messagebox.showerror('Invalid', 'Both Password should match')

img = PhotoImage(file='login.png')
Label(window, image=img, border=0, bg='white').place(x=50, y=90)

frame = Frame(window, width=350, height=390, bg='#fff')
frame.place(x=480, y=50)

heading = Label(frame,text='Sign Up', fg="#57a1f8", bg='white', font=('Microsoft Yahei UI Light', 23, 'bold'))
heading.place(x=100, y=5)


########-----------------------------
def on_enter(e):
    user.delete(0,'end')

def on_leave(e):
    if user.get()=='':
        user.insert(0,'Username')

user = Entry(frame,width=25,fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light', 11))
user.place(x=30, y=80)
user.insert(0, 'Username')
user.bind("<FocusIn>",on_enter)
user.bind("<FocusOut>",on_leave)

Frame(frame, width=295, height=2, bg='black').place(x=25,y=107)



########-----------------------------
def on_enter(e):
    code.delete(0,'end')

def on_leave(e):
    if code.get()=='':
        code.insert(0,'Password')

code = Entry(frame,width=25,fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light', 11))
code.place(x=30, y=150)
code.insert(0, 'Password')
code.bind("<FocusIn>",on_enter)
code.bind("<FocusOut>",on_leave)

Frame(frame, width=295, height=2, bg='black').place(x=25,y=177)



########-----------------------------
def on_enter(e):
    confirm_code.delete(0,'end')

def on_leave(e):
    if confirm_code.get()=='':
        confirm_code.insert(0,'Confirm Password')

confirm_code = Entry(frame,width=25,fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light', 11))
confirm_code.place(x=30, y=220)
confirm_code.insert(0, 'Confirm Password')
confirm_code.bind("<FocusIn>",on_enter)
confirm_code.bind("<FocusOut>",on_leave)

Frame(frame, width=295, height=2, bg='black').place(x=25,y=247)


#---------------

Button(frame,width=39, pady=7, text='Sign Up', bg='#57a1f8', fg='white', border=0, command=signup).place(x=35, y=280)
label = Label(frame, text='I have an account', fg='black', bg='white', font=('Microsoft Yahei UI Light', 9))
label.place(x=90, y=340)

def signin():
    # Création du cadre pour la page de connexion
    login_frame = Frame(window, width=350, height=390, bg='#fff')
    login_frame.place(x=480, y=50)

    # Ajout de widgets pour la page de connexion
    # ...

    # Masquer la fenêtre actuelle
    frame.lower()

    # Afficher la nouvelle page
    login_frame.lift()

    # Ajouter un bouton pour retourner à la page précédente
    return_button = Button(login_frame,image=img, width=25, height=25, text="Retour", command=lambda: [login_frame.lower(), frame.lift()])
    return_button.place(x=10, y=10)


signin = Button(frame, width=6, text='Sign in', border=0, bg='white', cursor='hand2', fg='#57a1f8', command=signin)
signin.place(x=200, y=340)



window.mainloop()