





class Silla:
    #metodo == "funcion"
    #atributo de clase.
    respaldo = True  
    def __init__(self,cant_patas:int, material:str, color:str, precio:float):
        #atributos normales
        self.cant_patas = cant_patas
        self.material = material
        self.color = color
        self.precio = precio
        
    def __str__(self):
        pass

    def mostrar_silla(self):
        print(f"""
Patas: {self.cant_patas}
Material: {self.material}
Color: {self.color}
Precio: {self.precio}
""")

silla_ikea = Silla(4,"madera","rojo",1000)
silla_china = Silla(3,"plstico","negro",500)
print(silla_ikea.mostrar_silla())