try:
    import Tkinter as Tk # python 2
except ModuleNotFoundError:
    import tkinter as Tk # python 3
from PIL import Image, ImageTk
class vistas():
    def __init__(self, root):
        self.fameP=Tk.Frame(root)
        raizhijo.title("Vista de Registro")
        raizhijo.iconbitmap("C:/Users/aurelio/Desktop/phyton_Xto/recursos/Imagenes/cxto.ico")
        raizhijo.geometry("750x100")
        contenedor0=Frame(raizhijo)
        contenedor0.pack()
        lbNombre=Label(contenedor0,text="Nombre:  ")--
        lbNombre.pack(side=LEFT)  
        txtNombre=Entry(contenedor0)
        txtNombre.pack(side=RIGHT)
        lbap=Label(contenedor0,text="Apellido Paterno:")
        lbap.pack(side=RIGHT)
        txtap=Entry(contenedor0)
        txtap.pack(side=LEFT)
        lbapm=Label(contenedor0,text="Apellido Materno:")
        lbapm.pack(side=LEFT)
        txtapm=Entry(contenedor0)
        txtapm.pack(side=RIGHT)
        contenedor1=Frame(raizhijo)
        contenedor1.pack()
        lbcel=Label(contenedor1,text="Telefono:  ")
        lbcel.pack(side=LEFT)
        txtcel=Entry(contenedor1)
        txtcel.pack(side=RIGHT)
        lbpar=Label(contenedor1,text="Parroquia")
        lbpar.pack(side=RIGHT)
        txtpar=Entry(contenedor1)
        txtpar.pack(side=LEFT)   
        lbcelR=Label(contenedor1,text="Apellido Materno:")
        lbcelR.pack(side=LEFT)
        txtref=Entry(contenedor1)
        txtref.pack(side=RIGHT)
        contenedorlista=Frame(raizhijo)
        contenedorlista.pack()
        contenedorBoton=Frame(raizhijo)
        contenedorBoton.pack()
        btnRegistar=Button(contenedorBoton,text="Registrar")
        btnRegistar.pack()
        raizhijo.mainloop()
