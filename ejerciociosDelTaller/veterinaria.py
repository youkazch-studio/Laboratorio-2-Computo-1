
#Ejercicio: 
"""
Una veterinaria atiende solamente perros y los registra en una base de datos. Se requiere un programa que lea la información básica del perro (no más de 8 características) y se muestre en pantalla. En esta veterinaria todos los animales que llegan, entran con el estado inicial de NO ATEN- DIDO y cuando se registran se cambia automáticamente a ATENDIDO. Por ahora como la veterinaria solo atiende perros, basado en el peso (menos de 10kg o más de 10kg) los registra como “Perro Grande” o “Pe- rro Pequeño”.

"""

class Perro:

    #Constructor
    def __init__(self, nombre, raza, edad, peso, color, nombre_duenio, direccion, telefono):
        # Atributos privados
        self.__nombre = nombre
        self.__raza = raza
        self.__edad = edad
        self.__peso = peso
        self.__color = color
        self.__nombre_duenio = nombre_duenio
        self.__direccion = direccion
        self.__telefono = telefono
        
        # Estado inicial
        self.__estado = "NO ATENDIDO"
        
        # Clasificación de tamaño
        if self.__peso < 10:
            self.__tamano = "Perro Pequeño"
        else:
            self.__tamano = "Perro Grande"

    # Método para atender al perro
    def registrar(self):
        self.__estado = "ATENDIDO"
        
    # Método para mostrar la información del perro
    def mostrar_informacion(self):
        print(f"Nombre: {self.__nombre}")
        print(f"Raza: {self.__raza}")
        print(f"Edad: {self.__edad} años")
        print(f"Peso: {self.__peso} kg")
        print(f"Color: {self.__color}")
        print(f"Nombre del Dueño: {self.__nombre_duenio}")
        print(f"Dirección: {self.__direccion}")
        print(f"Teléfono: {self.__telefono}")
        print(f"Estado: {self.__estado}")
        print(f"Tamaño: {self.__tamano}")

# Ejemplo de uso del programa

# Paso 2: Crear una instancia de la clase Perro
perro1 = Perro(nombre="Firulais", raza="Labrador", edad=3, peso=15, color="Marrón", nombre_duenio="Mario Lopéz", direccion="Calle Falsa 123", telefono="555-1234")

# Paso 3: Registrar y mostrar la información del perro
perro1.registrar()
perro1.mostrar_informacion()
