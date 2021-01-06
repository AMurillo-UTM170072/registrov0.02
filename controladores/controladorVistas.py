try:
    import Tkinter as Tk
except ModuleNotFoundError:
    import tkinter as Tk

from getpass import getuser
from PIL import Image, ImageTk
from modelos import modelo_Vistas as modelado
from vistas import principalview as view

class Controlador:
    def __init__(self):
        self.raiz =Tk.Tk()
        self.modelo=modelado.modelo()
        self.vista= view.ventana(self.raiz)

    def run(self):
        self.raiz.title("Registro de pascua Juvenil Parroquia de Nuestra señora de guadalupe")
        self.raiz.iconbitmap("C:/Users/"+getuser()+"/Desktop/registrov0.01recursos/Imagenes/cxto.ico")
        self.raiz.geometry("1000x600")
        self.raiz.deiconify()
        self.raiz.mainloop()

    def run1(self):
        self.raiz.title("Registro de pascua Juvenil Parroquia de Nuestra señora de guadalupe")
        self.raiz.iconbitmap('C:/Users/aurelio/Desktop/registrov0.01/recursos/Imagenes/cxto.ico')
        self.raiz.geometry("1000x600")
        self.raiz.mainloop()
