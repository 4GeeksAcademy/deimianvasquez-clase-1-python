class Human: # esta es la clase
    # constructor se inicializa al ejecutar la clase
    def __init__(self, nombre, apellido, edad, color_piel):
        self.nombre = nombre
        self.edad = edad
        self.apellido = apellido
        self.color_piel = color_piel
        self.caminando = False


    def serialize(self): # es un método de la clase
        return {
            "nombre":self.nombre,
            "apellido":self.apellido,
            "edad": self.edad,
            "color": self.color_piel
        }
    
    def saludar(self):
        print(f"Hola ¿qué tal {self.nombre} {self.apellido}? Cómo estás?")

    
    def informacion(self):
        print(f"nombre: {self.nombre} \nApellido: {self.apellido} \nEdad: {self.edad}  \ncaminando: {self.caminando}")


    def caminar(self, data):
        self.caminando = data
 


class Trabajador(Human): # herencia de clase
    def __init__(self, salario, profesion, h_nombre, h_apellido, h_edad, h_color_piel):
        super().__init__(h_nombre, h_apellido, h_edad, h_color_piel)

        self.salario = salario
        self.profesion = profesion

    
    def informacion(self):
        super().informacion() # herencia del método
        print(f"Salario: {self.salario} \nProfesión: {self.profesion}")
    
    

# clase Trabajador
trabajador_1 = Trabajador(100, "Computista", "Deimian", "Vásquez", 36, "marron"  )
trabajador_1.informacion()


print("*"*30)

# crear una instancia de la clase cuando usamos Human
human_1 = Human("Deimian", "Vásquez", 36, "marron")
# human_1.saludar()
human_1.informacion()
# human_1.caminar(True)
# human_1.informacion()

# print("*"*30)

# # instancio la clase
# human_2 = Human("Elio", "Colmenares", "25", "blanco")
# human_2.saludar()