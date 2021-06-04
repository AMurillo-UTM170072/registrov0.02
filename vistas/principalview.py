try:
    import Tkinter as Tk # python 2
except ModuleNotFoundError:
    import tkinter as Tk# python 3
from getpass import getuser
from PIL import Image ,ImageTk 
class ventana:
    def __init__(self, raiz):
        self.frame=Tk.Frame(raiz)
        self.conteneodr0=Tk.Frame(raiz,bg="white")
        self.conteneodr0.pack()
        self.imagenF=Tk.PhotoImage(file=r"C:/Users/"+getuser()+"/Desktop/registrov0.01/recursos/Imagenes/fondoP.png")
        self.imagenR=Image.open("C:/Users/"+getuser()+"/Desktop/registrov0.01/recursos/Imagenes/registro.gif")
        self.ImgR=ImageTk.PhotoImage(self.imagenR)
        self.imagenV=Image.open("C:/Users/"+getuser()+"/Desktop/registrov0.01/recursos/Imagenes/ver.gif")
        self.ImgV=ImageTk.PhotoImage(self.imagenV)
        self.fondo=Tk.Label(self.conteneodr0,image=self.imagenF)
        self.contenedor=Tk.Frame(self.conteneodr0, bg="white")
        self.contenedor.pack(side="left")
        self.botonR=Tk.Button(self.contenedor,text="Registrar")
        self.botonR.config(image=self.ImgR,bg="white")
        self.botonR.pack(side="left")
        self.botonV=Tk.Button(self.contenedor,text="Ver registros")
        self.botonV.config(image=self.ImgV,bg="white")
        self.botonV.pack(side="right")
        self.fondo.pack()
        self.frame.pack()
    
        
