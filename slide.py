from tkinter import *

window = Tk()
window.title("Home")
window.geometry('925x700+350+20')
window.configure(bg='#F4EBD5')
window.resizable(False,False)

# Liste de cadres pour chaque page de contenu
content_frames = []
for i in range(4):
    content_frames.append(Frame(window, bg="white"))

# Fonction pour afficher le contenu de chaque page
def show_content(frame_index):
    for i, frame in enumerate(content_frames):
        if i == frame_index:
            frame.grid(row=0, column=1)
        else:
            frame.grid_forget()

# Boutons de navigation
navigation_bar = Frame(window, width=200, height=800, bg='#666666')
navigation_bar.grid(row=0, column=0)

first_button = Button(navigation_bar, width=25, height=0, text="Premier", fg='white', bg='black', command=lambda: show_content(0))
first_button.grid(row=0, column=0, pady=10)

second_button = Button(navigation_bar, width=25, height=0, text="Second", fg='white', bg='black', command=lambda: show_content(1))
second_button.grid(row=1, column=0, pady=10)

third_button = Button(navigation_bar, width=25, height=0, text="Troisième", fg='white', bg='black', command=lambda: show_content(2))
third_button.grid(row=2, column=0, pady=10)

fourth_button = Button(navigation_bar, width=25, height=0, text="Quatrième", fg='white', bg='black', command=lambda: show_content(3))
fourth_button.grid(row=3, column=0, pady=10)

# Contenu de chaque page
first_content = Label(content_frames[0], text="Contenu de la première page", bg="white")
first_content.pack(pady=50)

second_content = Label(content_frames[1], text="Contenu de la deuxième page", bg="white")
second_content.pack(pady=50)

third_content = Label(content_frames[2], text="Contenu de la troisième page", bg="white")
third_content.pack(pady=50)

fourth_content = Label(content_frames[3], text="Contenu de la quatrième page", bg="white")
fourth_content.pack(pady=50)

# Affichage initial de la première page
content_frames[0].grid(row=0, column=1)

window.mainloop()
