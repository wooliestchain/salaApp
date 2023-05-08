import sqlite3
import uuid


from product import Product
from datetime import datetime

class Sales:
    def __init__(self, product_name: str, amount: float, quantity: int, date: datetime.date = datetime.now().date(),
                 year: int = datetime.now().year, month: int = datetime.now().month, day: int = datetime.now().day, sales_id: int = None
                 ):
        self.sales_id = sales_id
        self.product_name = product_name
        self.amount = amount
        self.quantity = quantity
        self.date = date
        self.month = month
        self.year = year
        self.day = day
        self.sales_id = sales_id if sales_id else str(uuid.uuid4())



        self.conn = sqlite3.connect('app.db')
        self.c = self.conn.cursor()

        self.c.execute('''
        CREATE TABLE IF NOT EXISTS sales 
        ( sales_id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_name TEXT NOT NULL,
        amount REAL, 
        quantity INTEGER, 
        date TEXT NOT NULL,
        year INTEGER NOT NULL,
        month INTEGER NOT NULL, 
        day INTEGER NOT NULL
        );
        ''')
        self.conn.commit()

#Ajoutez une vente en base de données
    def add_sale_to_database(self):
        try:
            self.c.execute(
                "INSERT INTO sales (product_name, amount, quantity, date, year, month, day) VALUES (?,?,?,?,?,?,?)",
                (self.product_name, self.amount, self.quantity, str(self.date), str(self.year), str(self.month),
                 str(self.day)))
            self.conn.commit()
            print("Vente ajouté avec succés!")
        except sqlite3.Error as e:
            print("Une erreur s'est produite lors de l'ajout dans la base:", e)

    def update_sale(self):
        try:
            a = input("Entrer le nom du produit")
        except ValueError:
            print("Veuillez entrer une valeur correcte")
            a = input("Entrer le nom du produit")

        try:
            b = float(input("Entrer le montant de la vente"))
        except ValueError:
            print("Veuillez entrer une valeur correcte")
            b = float(input("Entrer le montant de la vente"))
        try:
            c = int(input("Entrer la quantité vendue"))
        except ValueError:
            print("Veuillez entrer une valeur correcte")
            c = int(input("Entrer la quantité vendue"))

        try:
            self.c.execute(
                "UPDATE sales SET amount=?, quantity=?, product_name=? WHERE sales_id=? ",
                (a, b, c, self.sales_id)
            )
            self.conn.commit()

        except sqlite3.Error as e:
            print("Modification echoué", e)

        print(self.sales_id)
#Liste des ventes pour un produit
    def get_sales_by_product(self):
        try:
            self.c.execute(
                'SELECT product_name FROM sales WHERE product_name=?', (self.product_name,)
            )
            rows = self.c.fetchall()
            list_sales = []
            for row in rows:
                list_sales.append(row)
            print(list_sales)
        except sqlite3.Error as e:
            print("Ce produit n'a pas été vendue :", e)

#Total des recettes pour un produit
    #
    #
    #
    #
    #
    #
    #
    #



#Total , Nombre  des ventes sur le mois selectioné
    def get_total_sales_by_month_for_a_product(self):
        a = int(input("Entrer le numéro du mois"))
        try:
            self.c.execute(
                'SELECT COUNT (*) FROM sales WHERE month=? ', (a,)
            )
            rows = self.c.fetchall()
            list_sales = []
            for row in rows:
                list_sales.append(row)
                print(list_sales)
        except sqlite3.Error as e:
            print("Erreur lors de la récupération des données:", e)


#Total des recettes pour un mois
    #
    #
    #
    #
    #
    #
    #
    #
    #

#Total des recettes pour le current_month
    #
    #
    #
    #
    #
    #
    #
    #

#Total des recettes pour le past_month
    #
    #
    #
    #
    #
    #
    #
    #
    #

#Rapport entre les recettes du path_month et du current month
    #
    #
    #
    #
    #
    #
    #




#Total des recettes pour un produit sur le current_month
    #
    #
    #
    #
    #
    #

#Total des recettes pour un produit sur le past_month
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #

# Rapport entre les recettes du path_month et du current month
    #
    #
    #
    #
    #
    #
    #
    #
    #


    #Nombre de ventes pour un produit
    def count_sales_by_product(self):
        try:
            self.c.execute(
                'SELECT COUNT (*) FROM sales WHERE product_name=?', (self.product_name,)
            )
            rows = self.c.fetchall()
            if rows:
                count_sales = []
                for row in rows:
                    count_sales.append(row)

                print(f'Le produit {self.product_name} a été vendu {",".join(map(str, row))} fois')
            else:
                print(f"Aucune vente n'a été effectuée pour le produit {self.product_name}")
        except sqlite3.Error as error:
            print(f"Erreur lors du comptage des ventes pour le produit {self.product_name}: {error}")

#Moyenne des ventes mensuelles d'un produit
    #
    #
    #
    #
    #
    #
    #
    #

#Moyenne des vente annuelles d'un produit
    #
    #
    #
    #
    #
    #
    #
    #

#Total des recettes du jour
    #
    #
    #
    #
    #

#Total des recettes du jour précédent
    #
    #
    #
    #
    #
    #
    #
#Rapport, différence et hause entre les recettes du jour et celles du jour précédent
    #
    #
    #
    #
    #
    #

# Rapport, différence et hause entre les recettes du mois en cours et celles du mois précédent
    #
    #
    #
    #
    #
    #


# Rapport, différence et hause entre les recettes de l'année en cours et celles de l'année précédente
    #
    #
    #
    #
    #
    #




    def set_time(self, time: datetime.time):
        self.time = time

    def get_time(self) -> datetime.time:
        return self.time

    def set_quantity(self, quantity: int):
        self.quantity = quantity

    def get_quantity(self) -> int:
        return self.quantity

    def set_amount(self, amount: float):
        self.amount = amount

    def get_amount(self) -> float:
        return self.amount

    def set_date(self, date: datetime.date):
        self.date = date

    def get_date(self) -> datetime.date:
        return self.date

    def to_dict(self) -> dict:
        return {
            "product": self.product_name.to_dict(),
            "quantity": self.quantity,
            "amount": self.amount,
            "date": str(self.date),
            "time": str(self.time)
        }

vente1 = Sales("uuuio",145.65,8)

vente2 = Sales("regab", 1000, 10)

#vente2.get_sales_by_product()
#vente2.count_sales_by_product()
vente2.add_sale_to_database()
#vente2.update_sale()

vente2.get_sales_by_product()

vente2.get_total_sales_by_month_for_a_product()
