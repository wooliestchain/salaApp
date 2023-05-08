import tkinter as tk


class NavigationBar(tk.Frame):
    def __init__(self, parent, content_frame):
        super().__init__(parent)
        self.parent = parent
        self.content_frame = content_frame  # La frame où le contenu sera affiché
        self.configure(bg="grey")  # Couleur de fond de la barre de navigation

        # Création des boutons de la barre de navigation
        self.button1 = tk.Button(self, text="Accueil", bg="grey", fg="white", command=self.show_home)
        self.button2 = tk.Button(self, text="Profil", bg="grey", fg="white", command=self.show_profile)
        self.button3 = tk.Button(self, text="Paramètres", bg="grey", fg="white", command=self.show_settings)
        self.button4 = tk.Button(self, text="Aide", bg="grey", fg="white", command=self.show_help)

        # Placement des boutons dans la barre de navigation
        self.button1.pack(side=tk.TOP, fill=tk.X)
        self.button2.pack(side=tk.TOP, fill=tk.X)
        self.button3.pack(side=tk.TOP, fill=tk.X)
        self.button4.pack(side=tk.TOP, fill=tk.X)

        # Configuration de l'espacement entre les boutons
        self.spacing = tk.Frame(self, height=10, bg="grey")
        self.spacing.pack(side=tk.TOP, fill=tk.X)

    def show_home(self):
        self.content_frame.configure(bg="white")
        content = tk.Label(self.content_frame, text="Page d'accueil")
        content.pack(side=tk.TOP, padx=10, pady=10)

    def show_profile(self):
        self.content_frame.configure(bg="white")
        content = tk.Label(self.content_frame, text="Profil utilisateur")
        content.pack(side=tk.TOP, padx=10, pady=10)

    def show_settings(self):
        self.content_frame.configure(bg="white")
        content = tk.Label(self.content_frame, text="Paramètres de l'application")
        content.pack(side=tk.TOP, padx=10, pady=10)

    def show_help(self):
        self.content_frame.configure(bg="white")
        content = tk.Label(self.content_frame, text="Aide et support")
        content.pack(side=tk.TOP, padx=10, pady=10)


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("400x400")

    # Contenu de la fenêtre principale
    content_frame = tk.Frame(root, bg="white")
    content_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    content = tk.Label(content_frame, text="Contenu de la fenêtre principale")
    content.pack(side=tk.TOP, padx=10, pady=10)

    # Création de la barre de navigation
    nav_bar = NavigationBar(root, content_frame)
    nav_bar.pack(side=tk.LEFT, fill=tk.Y)

    root.mainloop()
