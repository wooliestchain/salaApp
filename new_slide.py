from tkinter import *
from suds.client import Client
from tkinter import messagebox
from datetime import datetime






window = Tk()
window.title("Home")
window.geometry('925x700+350+20')
window.configure(bg='#F4EBD5')
window.resizable(False, False)


#Fenêtre d'acceuill
home_wind = Frame(window, width=1000, height=1000)
home_wind.place(x=200,y=0)
stat_lab = Label(home_wind, text="Vos Chiffres", fg="#151922", font=('Microsoft Yahei UI Light', 15, 'bold'))
stat_lab.place(x=0, y=25)
client = Client('http://localhost:8000/?wsdl')

result = client.service.max_month()

mvp_month = PhotoImage(file='mvp.png')
mvp_label = Label(home_wind,image=mvp_month)
mvp_label.place(x=20,y=485)

month_text = Label(home_wind, text="Le mois le plus lucratif est le mois de ", font=('Microsoft Yahei UI Light', 15, 'bold'))
month_text.place(x=100, y=485)
month_lab = Label(home_wind, text=result, font=('Microsoft Yahei UI Light', 15, 'bold'), fg='green')
month_lab.place(x=475, y=485)

result = client.service.max_month_sales()

month_sales_lab = Label(home_wind, text="Avec des recettes s'élevant à: ", font=('Microsoft Yahei UI Light', 15, 'bold'))
month_sales_lab.place(x=100, y=515)
month_sales = Label(home_wind, text=result, font=('Microsoft Yahei UI Light', 15, 'bold'), fg='green')
month_sales.place(x=400,y=515)

brand = PhotoImage(file='mvp.png')
brand_label = Label(home_wind, image=brand)
brand_label.place(x=20, y=220)

most_sales_product_lab = Label(home_wind, text="Le produit le plus vendu est: ", font=('Microsoft Yahei UI Light', 15, 'bold'))
most_sales_product_lab.place(x=100, y=220)
result = client.service.mvp_recette_service()
most_sales_product = Label(home_wind, text=result, font=('Microsoft Yahei UI Light', 15, 'bold'), fg='#FFAE42' )
most_sales_product.place(x=400, y=220)

most_sales_product_lab_qt = Label(home_wind, text="Pour une quantité de: ", font=('Microsoft Yahei UI Light', 15, 'bold'))
most_sales_product_lab_qt.place(x=100, y=255)
result = client.service.mvp_recette_service_qt()
most_sales_product_qt = Label(home_wind, text=result, font=('Microsoft Yahei UI Light', 15, 'bold'), fg='#FFAE42' )
most_sales_product_qt.place(x=325, y=255)



most_sales_product_lab_vt = Label(home_wind, text="Et des recettes s'élevant à: ", font=('Microsoft Yahei UI Light', 15, 'bold'))
most_sales_product_lab_vt.place(x=100, y=290)
result = client.service.mvp_recette_service_vt()
most_sales_product_vt = Label(home_wind, text=result, font=('Microsoft Yahei UI Light', 15, 'bold'), fg='#FFAE42' )
most_sales_product_vt.place(x=370, y=290)


mvp = PhotoImage(file='mvp.png')
mvp_label = Label(home_wind,image=mvp)
mvp_label.place(x=20,y=370)

day_mvp_label = Label(home_wind, text="La meilleure date: ", font=('Microsoft Yahei UI Light', 15, 'bold'))
day_mvp_label.place(x=100, y=370)
result = client.service.get_max_date_sales()
day_mvp_sales = Label(home_wind, text=result, font=('Microsoft Yahei UI Light', 15, 'bold'), fg='#588BAE' )
day_mvp_sales.place(x=290, y=370)

day_mvp_label_vt = Label(home_wind, text="Avec des recettes s'élevant à: ", font=('Microsoft Yahei UI Light', 15, 'bold'))
day_mvp_label_vt.place(x=100, y=405)
result = client.service.get_max_date_sales_vt()
day_mvp_sales_vt = Label(home_wind, text=result, font=('Microsoft Yahei UI Light', 15, 'bold'), fg='#588BAE' )
day_mvp_sales_vt.place(x=400, y=405)

total_label = Label(home_wind, text="Total des Recettes", font=('Microsoft Yahei UI Light', 18, 'bold'))
total_label.place(x=270, y=65)
result = client.service.total_rec()
total_rec = Label(home_wind, text=result, font=('Microsoft Yahei UI Light', 25, 'bold'), fg='#101D6B' )
total_rec.place(x=320, y=100)

money = PhotoImage(file='money-bag.png')
money_label = Label(home_wind, image=money)
money_label.place(x=450, y=108)


#Représente les conteneurs de chaque fenêtre
exp = Frame(window, width=1000, height=1000, bg='#FEFEFA')
exp1 = Frame(window, width=1000, height=1000, bg='#FEFEFA')
exp2 = Frame(window, width=1000, height=1000, bg='white')

#-----------------*FENETRE VENTES---------------------------
def add_sale_function():
    now = datetime.now().date()
    year = now.year
    month = now.month
    day = now.day

    product_entry = product_name.get()
    amount_entry  = amount.get()
    quant_entry = quant.get()

    if product_entry!="Nom du Produit" and amount_entry != "Prix Unitaire" and quant_entry != "Quantité vendue":
        client_add = Client('http://localhost:8000/?wsdl')
        result_add = client_add.service.add_sale(product_entry, amount_entry, quant_entry, now, year, month, day)

        result_next = client.service.recette_a_day(now)
        sales_day = Label(exp, text=result_next, font=('Microsoft Yahei UI Light', 15, 'bold'), fg="green", bg='white')
        sales_day.place(x=350, y=330)

        result_tot = client.service.total_rec()
        total_rec = Label(home_wind, text=result_tot, font=('Microsoft Yahei UI Light', 25, 'bold'), fg='#101D6B')
        total_rec.place(x=320, y=100)
        messagebox.showinfo('Infos', result_add)


    else:
        messagebox.showerror('Invalid', 'Remplissez tous les champs')


def search_function():
    spec_date_entry = spec_date.get()
    if spec_date_entry!="":
        client_spec = Client('http://localhost:8000/?wsdl')

        result_spec = client_spec.service.recette_a_day(spec_date_entry)

        title_spec = Label(exp,text="Les recettes pour le "+spec_date_entry+" sont",font=('Microsoft Yahei UI Light', 15, 'bold'), fg="#151922", bg='white')
        title_spec.place(x=45, y=500)
        sales_spec = Label(exp,text=result_spec,font=('Microsoft Yahei UI Light', 16, 'bold'), fg="green", bg='white')
        sales_spec.place(x=45, y=530)




title_label = Label(exp, text="Enregistrer une vente", font=('Microsoft Yahei UI Light', 15, 'bold'), fg="#57a1f8", bg='white')
title_label.place(x=275, y=15)


def on_enter(e):
    product_name.delete(0,'end')

def on_leave(e):
    if product_name.get()=='':
        product_name.insert(0,'Nom du Produit')

product_label = Label(exp, text="Entrer le nom du produit", font=('Microsoft Yahei UI Light', 12, 'bold'), fg="#57a1f8", bg='white')
product_label.place(x=40, y=70)

product_name = Entry(exp,font=('Microsoft Yahei UI Light', 11, 'bold'), width=25,fg='black', border=0, bg='white')
product_name.insert(0, 'Nom du Produit')
product_name.place(x=45, y=100)
product_name.bind("<FocusIn>",on_enter)
product_name.bind("<FocusOut>",on_leave)
Frame(exp, width=295, height=2, bg='grey').place(x=40,y=120)


def on_enter(e):
    amount.delete(0,'end')

def on_leave(e):
    if amount.get()=='':
        amount.insert(0,'Prix Unitaire')


amount_label = Label(exp, text="Entrer le prix unitaire", font=('Microsoft Yahei UI Light', 12, 'bold'), fg="#57a1f8", bg='white')
amount_label.place(x=400, y=70)

amount = Entry(exp,font=('Microsoft Yahei UI Light', 11, 'bold'), width=25,fg='black', border=0, bg='white')
amount.insert(0, 'Prix Unitaire')
amount.place(x=405, y=100)
amount.bind("<FocusIn>",on_enter)
amount.bind("<FocusOut>",on_leave)
Frame(exp, width=295, height=2, bg='grey').place(x=400,y=120)



def on_enter(e):
    quant.delete(0,'end')

def on_leave(e):
    if quant.get()=='':
        quant.insert(0,'Quantité vendue')


quant_label = Label(exp, text="Entrer la quantité ", font=('Microsoft Yahei UI Light', 12, 'bold'), fg="#57a1f8", bg='white')
quant_label.place(x=40, y=150)

quant = Entry(exp,font=('Microsoft Yahei UI Light', 11, 'bold'), width=25,fg='black', border=0, bg='white')
quant.insert(0, 'Quantité vendue')
quant.place(x=45, y=180)
quant.bind("<FocusIn>",on_enter)
quant.bind("<FocusOut>",on_leave)
Frame(exp, width=295, height=2, bg='grey').place(x=40,y=200)


add_sales = Button(exp, text="Valider", bg='#32CD32', fg='white', width=25,font=('Microsoft Yahei UI Light', 11, 'bold'), command=add_sale_function)
add_sales.place(x=400, y=170)

sales_day_label = Label(exp, text="Total des ventes du jour",font=('Microsoft Yahei UI Light', 15, 'bold'), fg="#57a1f8", bg='white')
sales_day_label.place(x=275, y=300)

now = datetime.now().date()

result = client.service.recette_a_day(now)
sales_day = Label(exp, text=result,font=('Microsoft Yahei UI Light', 15, 'bold'), fg="green", bg='white')
sales_day.place(x=350, y=330)

spec_sales_label = Label(exp, text="Obtenir les recettes pour une date (YY-JJ-MM)",font=('Microsoft Yahei UI Light', 15, 'bold'), fg="#57a1f8", bg='white')
spec_sales_label.place(x=40, y=380)

spec_date = Entry(exp,font=('Microsoft Yahei UI Light', 11, 'bold'), width=25,fg='black', border=0, bg='white' )
spec_date.place(x=45, y=430)
Frame(exp, width=200, height=2, bg='grey').place(x=40,y=450)


spec_button = Button(exp, text="Rechercher", fg='blue', width=25, command=search_function)
spec_button.place(x=300, y=430)

#---------------------------------Fenetre PRODUIT------------------------------
def search_prod():
    prod_entry = prod_name.get()
    if prod_entry!="":
        client_prod = Client('http://localhost:8000/?wsdl')

        result_prod = client_prod.service.product_infos_name(prod_entry)

        name_res = Label(exp1, text=result_prod, font=('Microsoft Yahei UI Light', 12, 'bold'), fg="#57a1f8", bg='white')
        name_res.place(x=200,y=230)

        result_vt = client_prod.service.product_infos_vt(prod_entry)
        vt_res = Label(exp1, text=result_vt, font=('Microsoft Yahei UI Light', 12, 'bold'), fg="#57a1f8", bg='white')
        vt_res.place(x=300,y=230)

        result_nbventes = client_prod.service.product_infos_nbventes(prod_entry)
        nbventes_res = Label(exp1, text=result_nbventes, font=('Microsoft Yahei UI Light', 12, 'bold'), fg="#57a1f8", bg='white')
        nbventes_res.place(x=400, y=230)

        result_qtventes = client_prod.service.product_infos_qtventes(prod_entry)
        qt_res = Label(exp1, text=result_qtventes, font=('Microsoft Yahei UI Light', 12, 'bold'), fg="#57a1f8",bg='white')
        qt_res.place(x=500, y=230)



    else :


        name_res = Label(exp1, text="", font=('Microsoft Yahei UI Light', 12, 'bold'), fg="#57a1f8", bg='white')
        name_res.place(x=200,y=230)

        vt_res = Label(exp1, text="", font=('Microsoft Yahei UI Light', 12, 'bold'), fg="#57a1f8", bg='white')
        vt_res.place(x=300,y=230)

        nbventes_res = Label(exp1, text="", font=('Microsoft Yahei UI Light', 12, 'bold'), fg="#57a1f8", bg='white')
        nbventes_res.place(x=400, y=230)

        qt_res = Label(exp1, text="", font=('Microsoft Yahei UI Light', 12, 'bold'), fg="#57a1f8",bg='white')
        qt_res.place(x=500, y=230)







new_lab = Label(exp1, text="Obtenir les informations sur un produit", font=('Microsoft Yahei UI Light', 15, 'bold'), fg="#57a1f8", bg='white')
new_lab.place(x=200,y=15)

prod_label = Label(exp1, text="Entrer le nom du produit", font=('Microsoft Yahei UI Light', 12, 'bold'), fg="#57a1f8", bg='white')
prod_label.place(x=40, y=70)
prod_name = Entry(exp1,font=('Microsoft Yahei UI Light', 11, 'bold'), width=25,fg='black', border=0, bg='white')
prod_name.insert(0,'Nom du produit')
prod_name.bind("<FocusIn>",on_enter)
prod_name.bind("<FocusOut>",on_leave)
prod_name.place(x=45, y=100)
Frame(exp1, width=295, height=2, bg='grey').place(x=40,y=120)

prod_button = Button(exp1,text="Rechercher", width=25,fg='white', border=0, bg='blue', command=search_prod)
prod_button.place(x=350, y=100)

nom_produit = Label(exp1, text="Produit", font=('Microsoft Yahei UI Light', 12, 'bold'), fg="#151922", bg='white')
nom_produit.place(x=200, y=200)

sales_produit = Label(exp1, text="Recettes", font=('Microsoft Yahei UI Light', 12, 'bold'), fg="#151922", bg='white')
sales_produit.place(x=300, y=200)

ventes_produit = Label(exp1, text="Ventes", font=('Microsoft Yahei UI Light', 12, 'bold'), fg="#151922", bg='white')
ventes_produit.place(x=400, y=200)

quantite_produit = Label(exp1, text="Quantité", font=('Microsoft Yahei UI Light', 12, 'bold'), fg="#151922", bg='white')
quantite_produit.place(x=500, y=200)






# Initialisation des widgets
third_lab = Label(exp2, text="Contenu du troisième bouton")
slide_bar = Frame(window, width=200, height=800, bg='#666666')

third_lab.place(x=500, y=100)


imgs = PhotoImage(file='relogin.png')
Label(slide_bar, image=imgs, border=0, bg='white').place(x=40, y=10)


def home_place():
    exp.place_forget()
    exp1.place_forget()
    exp2.place_forget()

    home_wind.place(x=200,y=0)

# Fonction pour afficher le contenu du premier bouton
def on_first_button():
    # Supprime le contenu précédent s'il existe
    home_wind.place_forget()
    exp1.place_forget()
    exp2.place_forget()
    # Affiche le contenu du premier bouton
    exp.place(x=200, y=0)

# Fonction pour afficher le contenu du second bouton
def on_second_button():
    # Supprime le contenu précédent s'il existe
    home_wind.place_forget()
    exp.place_forget()
    exp2.place_forget()
    # Affiche le contenu du second bouton
    exp1.place(x=200, y=0)


def on_third_button():
    # Supprime le contenu précédent s'il existe
    home_wind.place_forget()
    exp.place_forget()
    exp1.place_forget()
    # Affiche le contenu du second bouton
    exp2.place(x=200, y=0)

# Configuration des boutons
home_button = Button(slide_bar, width=25, height=0, text="Acceuil", fg='white', bg='black', command=home_place)
first_button = Button(slide_bar, width=25, height=0, text="Ventes", fg='white', bg='black', command=on_first_button)
second_button = Button(slide_bar, width=25, height=0, text="Produits", fg='white', bg='black', command=on_second_button)
third_button = Button(slide_bar, width=25, height=0, text="Commerce", fg='white', bg='black', command=on_third_button)

# Placement des widgets dans la fenêtre
slide_bar.place(x=0, y=0)
home_button.place(x=5, y=100)
first_button.place(x=5, y=200)
second_button.place(x=5, y=300)
third_button.place(x=5, y=400)

window.mainloop()
