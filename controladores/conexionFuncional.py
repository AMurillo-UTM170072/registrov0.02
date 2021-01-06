from pymongo import MongoClient
class conexion:
    cliente=MongoClient("mongodb+srv://Aurelio45:root123@atolon.wwzlq.mongodb.net/Atolon?retryWrites=true&w=majority")
    coleccion=cliente.Atolon.Pruebas_Nucleares
    def consulta1(self):
        for nombres in self.cliente.database_names():
            print(nombres)
    def insetar(self):
        self.coleccion=cliente.Atolon.Pruebas_Nucleares
        vividore_R=[
            {
                "Nombre":self.nombre,
                "Apellido_Paterno":self.apellido_par,
                "Apellido_Materno":self.apellido_mat,
                "Edad":self.edad,
                "celular":self.telefono,
                "Parroquia":self.parroquia,
                "Casa de campaña":self.campaña,
                "Ocupantes":self.Nocupantes
            }
        ]
        self.coleccion.insert_one(vividore_R)
    def delete(self):
        eleminar={"Nombre":self.nombre}
        self.cliente.Atolon.Pruebas_Nucleares.delete_one(eleminar)
    def mostrar_uno(self):
        print(self.cliente.Atolon.Pruebas_Nucleares.find_one())  
    def mostrar_todo(self):
        for x in self.cliente.Atolon.Pruebas_Nucleares.find():  
            print(x) 
    def busacar_condicion(self,nombre):
        for x in self.cliente.Atolon.Pruebas_Nucleares.find({"nombre": self.nombre}):  
            print(x) 
    def contar(self):
        print(self.cliente.Atolon.Pruebas_Nucleares.count())
