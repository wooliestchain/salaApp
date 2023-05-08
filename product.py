import sqlite3
from typing import List

class Product:
    def __init__(self,  product_name: str, product_categorie:str, product_prix:float):
        self.product_name = product_name
        self.product_categorie = product_categorie
        self.product_prix = product_prix
        self.sales = []

        self.conn = sqlite3.connect('app.db')
        self.c = self.conn.cursor()

        self.c.execute('''
        CREATE TABLE IF NOT EXISTS products
        (product_id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_name TEXT NOT NULL,
        product_categorie TEXT NOT NULL,
        product_prix REAL);
        ''')
        self.conn.commit()

    def add_product_to_database(self):
        self.c.execute(
            "INSERT INTO products (product_name, product_categorie, product_prix) VALUES (?,?,?)",
            ( self.product_name, self.product_categorie, self.product_prix))
        self.conn.commit()



    def set_price(self, product_prix):
        self.product_prix = product_prix

    def set_name(self, product_name):
        self.product_name = product_name

    def set_cat(self, product_categorie):
        self.product_categorie = product_categorie

    def get_price(self) -> float:
        return self.product_prix
    
    def get_name(self) -> str:
        return self.product_name
    
    def get_cat(self) -> str:
        return self.product_categorie


node = Product("jbhhu", "ihihi",46.65)
#class Merchant:
 #   def __int__(self, nom, numero, lieu, jours:list, horaire  ):