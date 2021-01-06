try:
    import Tkinter as Tk # python 2
except ModuleNotFoundError:
    import tkinter as Tk# python 3
from getpass import getuser
from PIL import Image, ImageTk
class ventana:
    def Vregistro (self ,raiz):
        raizhijo=Toplevel(self.raiz)
        raizhijo.title("Vista de Registro")
        raizhijo.iconbitmap("C:/Users/"+getuser()+"/Desktop/phyton_Xto/recursos/Imagenes/cxto.ico")
        raizhijo.geometry("750x100")
        contenedor0=Frame(raizhijo)
        contenedor0.pack()
        

        lbNombre=Label(contenedor0,text="Nombre:  ")
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

        lbedad=Label(contenedor1,text="edad:")
        lbedad.pack(side=LEFT)
        txtref=Entry(contenedor1)
        txtref.pack(side=LEFT)
        
        
        lbpar=Label(contenedor1,text="casa de campaña")
        lbpar.pack(side=LEFT)
        txtCasa=Entry(contenedor1)
        txtCasa.pack(side=RIGHT)

        contenedorlista=Frame(raizhijo)
        contenedorlista.pack()
        contenedorBoton=Frame(raizhijo)
        contenedorBoton.pack()
        btnRegistar=Button(contenedorBoton,text="Registrar")
        btnRegistar.pack()
        raiz.iconify()
        

    def Vconsulta():
        raizhija=Toplevel(raiz)
        raizhija.title("Consulta de Vividores")
        raizhija.iconbitmap("C:/Users/"+getuser()+"/Desktop/phyton_Xto/recursos/Imagenes/cxto.ico")
        raizhija.geometry("1000x260")
        conter=Frame(raizhija)
        conter.pack()

        lbv=Label(conter,text="Buscar por nombre de vividor")
        lbv.pack(side=LEFT)
        btnBush=Button(conter,text="Buscar")
        btnBush.pack(side=RIGHT)
        txtbN=Entry(conter)
        txtbN.pack(side=RIGHT)

        contendorB=Frame(raizhija)
        contendorB.pack()

        btnCont=Button(contendorB,text="contar")
        btnCont.pack(side=LEFT)

        txtnum=Entry(contendorB,state="disabled")
        txtnum.pack(side=RIGHT)

        lbn=Label(contendorB,text="N° vividores:  ")
        lbn.pack(side=RIGHT)

        contenerdorTabla=Frame(raizhija)
        contenerdorTabla.pack()

        Tabla=Text(contenerdorTabla,width=100,height=3)
        Tabla.pack()
        
        raizhija.iconify()
    
    def __init__(self,raiz):
        """en este bloque se puede ver que se le esta poniendo un icono,tamaño y titulo de la vista"""
        self.frame=Tk.Frame(raiz)
        imagen=PhotoImage(file="C:/Users/"+getuser()+"/Desktop/registrov0.01recursos/Imagenes/fondoP.png")
        fondo=Label(raiz,image=imagen)
        contenedor=Frame(raiz,bg="white")
        contenedor.pack(side=RIGHT)
        """https://giphy.com/stickers/examen-escribir-lapiz-KX82K17P5rYyzYQpKb para los putos gifs"""
        btnRegistrar=Button(contenedor,text="Registrar",bg="white")
        """ instaciamos un boton en el cual le pondremos 
        un color de fondo blanco"""
        imagenR=Image.open("C:/Users/"+getuser()+"/Desktop/registrov0.01recursos/Imagenes/registro.gif")
        imgR=ImageTk.PhotoImage(imagenR)
        btnRegistrar.config(image=imgR,bg="white",command=Vregistro)
        btnRegistrar.pack()
        labelR=Label(contenedor,text="Registrar",bg="white")
        labelR.pack()
        contenedor0=Frame(raiz,bg="white")
        contenedor0.pack(side=LEFT)
        btnVer=Button(contenedor0,text="consultar",bg="white", command=Vconsulta)
        imagenV0=Image.open("C:/Users/"+getuser()+"/Desktop/phyton_Xto/recursos/Imagenes/ver.gif")
        imgV=ImageTk.PhotoImage(image=imagenV0)
        btnVer.config(image=imgV,bg="white")
        btnVer.pack()
        lVer=Label(contenedor0,text="Ver registros",bg="white")
        lVer.pack()
        fondo.pack()
        #raiz.mainloop()