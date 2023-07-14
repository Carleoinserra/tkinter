import tkinter as tk
from tkinter import messagebox

class conto:
    def __init__(self, id, saldo):
        self.saldo = saldo
        self.id = id

class mach:
    def __init__(self, conti):
     self.conti = conti

    def erogaCa(self, id):

        for i in self.conti:
         if i.id == id:
             if i.saldo > 2:
              i.saldo -= 2
              stringa = "erogazione in corso"
             else:
              stringa = "credito insufficiente"
        return stringa
    def erogaThe(self):
        for i in self.conti:
         if i.id == id:
             if i.saldo > 3:
              i.saldo -= 3
              stringa = "erogazione in corso"
             else:
              stringa = "credito insufficiente"
         return stringa
    def erogaCiok(self):
        for i in self.conti:
         if i.id == id:
             if i.saldo > 3.50:
              i.saldo -= 3.50
              stringa = "erogazione in corso"
             else:
              stringa = "credito insufficiente"
         return stringa
    def erogaW(self, id):
        for i in self.conti:
         if i.id == id:
             if i.saldo > 1.50:
              i.saldo -= 1.50
              stringa = "erogazione in corso"
             else:
              stringa = "credito insufficiente"
         return stringa


c1 = conto("01", 20)
c2 = conto("02", 10)
c3 = conto("03", 10)
lista =[]
lista.append(c1)
lista.append(c2)
lista.append(c3)
m1 = mach(lista)

  #for el in m1.conti:


passw = 0
# Import Module
from tkinter import *
# function to display text when
# button is clicked
def open():

    passw = password_entry.get()
    ok = False
    for el in m1.conti:

        if el.id == passw:

            id = passw
            ok = True
    if ok == True:
     new_window = tk.Toplevel(root)
     new_window.title("Scegli il prodotto")
     new_window.geometry('600x600')
     button1 = tk.Button(new_window, text="Caffè", command=lambda: coffe(lbl1))
     button1.pack()
     button2 = tk.Button(new_window, text="The", command=open)
     button2.pack()
     button3 = tk.Button(new_window, text="Cioccolata", command=open)
     button3.pack()
     button4 = tk.Button(new_window, text="Cioccolata", command=open)
     button4.pack()
     lbl1 = Label(new_window, text="display",bg="black", fg="white")
     lbl1.pack()


# create root window
root = tk.Tk()
root.geometry('300x300')
# root window title and dimension
root.title("Macchinetta Talentform")
# Set geometry(widthxheight)
# Creazione del pulsante di login
login_button = tk.Button(root, text="Login", command=open)
login_button.pack()


# Creazione dei widget per il nome utente e la password


password_label = tk.Label(root, text="Password:")
password_label.pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()

    # Aggiungi gli elementi desiderati alla nuova finestra...
def coffe(lbl):

    lbl1 = lbl

    passw = password_entry.get()
    ok = False


    ok = True
    for el in m1.conti:
     if el.id == passw:
            # viene invocata la funzione eroga caffè su machinetta
            #questa funzione ha come parametro l'id
            # se il saldo è disponibile eroga il caffè
            # e sottrae l'importo al saldo
            # inoltre ha un valore di ritorno di tipo stringa
            stringa = m1.erogaCa(passw)
            stringa1 = "Saldo rimanente ", el.saldo
            display = stringa1, " ", stringa
            lbl1.configure(text=display)










# Execute Tkinter
root.mainloop()