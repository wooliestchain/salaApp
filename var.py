import tkinter as tk
from tkinter import ttk


class LoadingScreen:
    def __init__(self, master):
        self.master = master
        self.top = tk.Toplevel(master)
        self.top.title("Chargement...")
        self.top.transient(master)
        self.top.grab_set()
        ttk.Label(self.top, text="Veuillez patienter...").pack(padx=50, pady=50)

    def close(self):
        self.top.destroy()
        self.master.focus_set()


# Création de la fenêtre principale
root = tk.Tk()
root.title("Ma fenêtre")

# Création de la fenêtre de chargement
loading_screen = LoadingScreen(root)

# Simulation d'un temps de chargement
# Remplacez cette partie par votre propre code de chargement
import time

time.sleep(5)

# Fermeture de la fenêtre de chargement
loading_screen.close()

# Affichage de la fenêtre principale
root.mainloop()
