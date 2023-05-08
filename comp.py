from tkinter import *
from tkinter import messagebox
import tk as tk
import mysql.connector
from suds.client import Client



window = Tk()
window.title("SignUp")
window.geometry('925x500+300+0')
window.configure(bg='#F4EBD5')
window.resizable(False,False)



def compinfos():
    codeentry = code.get()
    namedentry = name.get()
    yearentry = year.get()
    sectorentry = sector.get()
    descrentry = descr.get('1.0', 'end')

    #conn = mysql.connector.connect(
     #   host="localhost",
      #  database="wool",
       # username="root",
        #password="",
    #)


    if codeentry!="Code" and namedentry != "Nom de votre compagnie" and yearentry != "Année de fondation"  and sectorentry != "Secteur" and descrentry != "" :
        client = Client('http://localhost:8000/?wsdl')
        result = client.service.new_commerce(codeentry, namedentry, yearentry, sectorentry, descrentry)
        messagebox.showinfo('Infos', result)

        #try:
         #   cursor = conn.cursor()
          #  cursor.execute("""
           # INSERT INTO commerce (code, commerce_name, year_fond, sector, descr) VALUES (%s, %s, %s, %s, %s);
            #""", (codeentry, namedentry, yearentry, sectorentry, descrentry))
            #conn.commit()


        #except mysql.connector.Error as e:
         #   print("Erreur", e)
          #  raise ValueError("Impossible de se connecter")

    else:
        messagebox.showerror('Invalid', 'Remplissez tous les champs')





frame = Frame(window, bg='#FEFEFA')
frame.pack(fill=BOTH, expand=YES)
imgs = PhotoImage(file='relogin.png')
Label(frame, image=imgs, border=0, bg='white').place(x=15, y=10)

heading = Label(frame,text='Parler nous de votre affaire', fg="#57a1f8", bg='white', font=('Microsoft Yahei UI Light', 19, 'bold'))
heading.place(x=350, y=20)

#-------------Code pour identifier la compagnie------------#
def on_enter(e):
    code.delete(0,'end')

def on_leave(e):
    if code.get()=='':
        code.insert(0,'Code')


code_label = Label(frame, text="Entrer le code de votre companie", fg="#57a1f8", bg='white', font=('Microsoft Yahei UI Light', 12, 'bold'))
code_label.place(x=70, y=80)

code = Entry(frame,width=25,fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light', 11))
code.place(x=75, y=110)
code.insert(0, 'Code')
code.bind("<FocusIn>",on_enter)
code.bind("<FocusOut>",on_leave)

Frame(frame, width=295, height=2, bg='grey').place(x=70,y=135)



#-------------NOM de la compagnie------------#
def on_enter(e):
    name.delete(0,'end')

def on_leave(e):
    if name.get()=='':
        name.insert(0,'Nom de votre compagnie')

name_label = Label(frame, text="Entrer le nom de votre compagnie", fg="#57a1f8", bg='white', font=('Microsoft Yahei UI Light', 12, 'bold'))
name_label.place(x=420, y=80)

name = Entry(frame,width=25,fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light', 11))
name.place(x=425, y=110)
name.insert(0, 'Nom de votre compagnie')
name.bind("<FocusIn>",on_enter)
name.bind("<FocusOut>",on_leave)

Frame(frame, width=295, height=2, bg='grey').place(x=420,y=135)



#-------------Année de fondation de la compagnie------------#
def on_enter(e):
    year.delete(0,'end')

def on_leave(e):
    if year.get()=='':
        year.insert(0,'Année de fondation')

year_label = Label(frame, text="Entrer l'année de votre compagnie", fg="#57a1f8", bg='white', font=('Microsoft Yahei UI Light', 12, 'bold'))
year_label.place(x=420, y=185)

year = Entry(frame,width=25,fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light', 11))
year.place(x=425, y=215)
year.insert(0, 'Année de fondation')
year.bind("<FocusIn>",on_enter)
year.bind("<FocusOut>",on_leave)

Frame(frame, width=295, height=2, bg='grey').place(x=420,y=235)


#-------------Année de fondation de la compagnie------------#
def on_enter(e):
    sector.delete(0,'end')

def on_leave(e):
    if sector.get()=='':
        sector.insert(0,'Secteur')

sector_label = Label(frame, text="Entrer le secteur d'activité", fg="#57a1f8", bg='white', font=('Microsoft Yahei UI Light', 12, 'bold'))
sector_label.place(x=70, y=185)

sector = Entry(frame,width=25,fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light', 11))
sector.place(x=75, y=215)
sector.insert(0, 'Secteur')
sector.bind("<FocusIn>",on_enter)
sector.bind("<FocusOut>",on_leave)

Frame(frame, width=295, height=2, bg='grey').place(x=70,y=235)




#-------------Description de la compagnie------------#
def on_enter(e):
    descr.delete(0,'end')

def on_leave(e):
    if descr.get()=='':
        descr.insert(0,'Description de votre compagnie')

descr_label = Label(frame, text="Décrivez votre compagnie", fg="#57a1f8", bg='white', font=('Microsoft Yahei UI Light', 12, 'bold'))
descr_label.place(x=50, y=285)

descr = Text(frame,width=40,fg='black', height=5, border=2,  font=('Microsoft Yahei UI Light', 11))
descr.place(x=55, y=315)


button = Button(frame, fg='white', bg='#0CAFFF', width=20, height=1, text="Soumettre",font=('Microsoft Yahei UI Light', 11, 'bold'), borderwidth=2, relief="groove", command=compinfos)
button.place(x=420,y=315)


quest = PhotoImage(file='white.png')
Label(frame,image=quest,  background='black').place(x=420, y=400)
quest_label = Label(frame, text="Vous pouvez modifier ces informations par la suite ",fg="#333333", bg='white', font=('Microsoft Yahei UI Light', 8, 'bold' ))
quest_label.place(x=445, y=400)


#button_frame = Frame(frame)
#button_frame.place(x=420,y=315)

#v_text = Label(button_frame, text="Valider")
#v_text.pack(fill=BOTH,expand=YES)
#icon = PhotoImage(file='sd.png')

#valid = Button(button_frame, image=icon, text="Valider", height=25, width=25, fg='white', bg='green' )
#valid.pack(fill=BOTH,expand=YES)




window.mainloop()