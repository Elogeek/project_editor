from tkinter import *
# permet de stocker les objets files qui ne tiennent pas dans une instance de classe.
savedFile = {1: ""}

# Création de la fenêtre principale
class Win:
    def __init__(self, master, content):
        self.master = master
        self.content = content

    def create(self):
        self.master = Tk()
        self.master.title("Editeur de Texte")
        self.master.geometry("700x550")

    def add_text(self):
        self.content = Text(self.master)
        self.content.pack(expand=1, fill='both')

    def generate(self):
        self.master.mainloop()

    # Définition des actions des menus
    # actions du menu Fichier
    def quitter(self):
        self.master.quit()

    def nouveau(self):
        import os
        os.popen("python main.py")

    def fopen(self):
        file = self.master.filename = filedialog.askopenfilename(initialdir="/", title="Select File", filetypes=(
        ("Text Files", "*.txt"), ("all files", "*.*")))

        fp = open(file, "r")
        r = fp.read()
        self.content.insert(1.0, r)

    def saveAs(self):
        # create save dialog
        fichier = self.master.filename = filedialog.asksaveasfilename(initialdir="/", title="Enregistrer Sous\
        ", filetypes=(("Fichier Texte", "*.txt"), ("Tous les fichiers", "*.*")))
        fichier = fichier + ".txt"

        savedFile[1] = fichier
        f = open(fichier, "w")
        s = self.content.get("1.0", END)
        f.write(s)
        f.close()

    def save(self):
        if (savedFile[1] == ""):
            self.saveAs()
        else:
            f = open(savedFile[1], "w")
            s = self.content.get("1.0", END)
            f.write(s)
            f.close()


    # actions du menu Edition
    def copy(self):
        self.content.clipboard_clear()
        self.content.clipboard_append(self.content.selection_get())

    def past(self):
        self.content.insert(INSERT, self.content.clipboard_get())

    def cut(self):
        self.copy()
        self.content.delete("sel.first", "sel.last")

    # actions du menu Outils
    # actions du menu Aide

    # Création des menus
    def add_menu(self):
        # Création de la barre des menus
        menuBar = Menu(self.master)

        # Création du menu Fichier
        menuFichier = Menu(menuBar, tearoff=0)
        menuBar.add_cascade(label="Fichier", menu=menuFichier)
        menuFichier.add_command(label="Nouveau", command=self.nouveau)
        menuFichier.add_command(label="Ouvrir", command=self.fopen)
        menuFichier.add_command(label="Enregistrer", command=self.save)
        menuFichier.add_command(label="Enregistrer sous", command=self.saveAs)
        menuFichier.add_command(label="Quitter", command=self.quitter)
        self.master.config(menu=menuBar)

        #Création du Menu Edition
        menuEdition = Menu(menuBar, tearoff=0)
        menuBar.add_cascade(label="Edition ", menu=menuEdition)
        menuEdition.add_command(label="Annuler")
        menuEdition.add_command(label="Rétablir")

        menuEdition.add_command(label="Copier", command=self.copy)
        menuEdition.add_command(label="Couper", command=self.cut)
        menuEdition.add_command(label="Coller", command=self.past)

        # Création du Menu Options
        menuOutils = Menu(menuBar, tearoff=0)
        menuBar.add_cascade(label="Outils", menu=menuOutils)
        menuOutils.add_command(label="Préférences")

        # Création du Menu Aide
        menuAide = Menu(menuBar, tearoff=0)
        menuBar.add_cascade(label="Aide", menu=menuAide)
        menuAide.add_command(label="A propos")