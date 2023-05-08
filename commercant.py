import sqlite3
from datetime import datetime, timedelta

# Connexion à la base de données
conn = sqlite3.connect('app.db')

# Création de la table "produits"
conn.execute('''CREATE TABLE IF NOT EXISTS  produits
                 (id INTEGER PRIMARY KEY,
                  nom TEXT,
                  categorie TEXT,
                  prix REAL)''')

# Fermeture de la connexion
conn.close()




class Produit:
    def __init__(self, nom, categorie, prix):
        self.nom = nom
        self.categorie = categorie
        self.prix = prix

    def ajouter_produit(self):
        conn = sqlite3.connect('app.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO produits (nom, categorie, prix) VALUES (?, ?, ?)",
                       (self.nom, self.categorie, self.prix))
        conn.commit()
        conn.close()

prod = Produit("Banane", "Fruits", 2.50)
prod.ajouter_produit()





class Commercant():
    def __int__(self, nom, lieu_de_ventes, horaire_de_ventes,  produit, ventes):
        self.nom = nom
        self.lieu_de_vente = lieu_de_ventes
        self.horaire_de_vente = horaire_de_ventes
        self.produits = []
        self.vente = []

    def ajouter_vente(self,vente):
        self.vente.append(vente)

    def chiffres_vente_jour(self, date):
        ch = 0
        for vente in self.vente:
            if vente.date == date:
                ch += vente.montant
        return ch

    def chiffre_ventes_semaine(self,date):
        debut_semaine = date - timedelta(days=date.weekday())
        fin_semaine = debut_semaine + timedelta(days=6)
        ch = 0
        for vente in self.vente:
            if debut_semaine <= vente.date <= fin_semaine:
                ch  += vente.montant

        return ch


class Vente:
    def __int__(self, produit, quantité, prix_unit, date_vente, heure_vente, lieu):
        self.produit = []
        self.quanitié = quantité
        self.prix_unit = prix_unit
        self.date_vente = date_vente
        self.heure_vente = heure_vente
        self.lieu = lieu

