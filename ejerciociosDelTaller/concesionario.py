
#Ejercicio:

"""
Un concesionario de autos vende vehículos nacionales e importados. Todos tienen 4 ruedas y capacidad para 5 pasajeros. Esta información debe registrarse siempre por razones de ley. Requiere un programa que le permita almacenar las 10 principales características de los autos. El precio de venta de cada auto es igual al precio de compra multiplicado por 1.4 que corresponde a su margen de ganancia.

"""

class Auto:
    #Constructor:
    def __init__(self, marca, modelo, año, tipo, motor, color, precio_compra, kilometraje, transmision, combustible):
        self.__marca = marca
        self.__modelo = modelo
        self.__año = año
        self.__tipo = tipo  # Nacional o Importado
        self.__motor = motor
        self.__color = color
        self.__precio_compra = precio_compra
        self.__kilometraje = kilometraje
        self.__transmision = transmision  # Automática o Manual
        self.__combustible = combustible  # Gasolina, Diesel, Eléctrico, Híbrido
        
        # Características fijas por ley
        self.__ruedas = 4
        self.__capacidad_pasajeros = 5

        # Cálculo del precio de venta
        self.__precio_venta = self.__calcular_precio_venta()

    # Método privado para calcular el precio de venta
    def __calcular_precio_venta(self):
        return round(self.__precio_compra * 1.4, 2)
    
    # Método para mostrar la información del auto
    def mostrar_informacion(self):
        print(f"Marca: {self.__marca}")
        print(f"Modelo: {self.__modelo}")
        print(f"Año: {self.__año}")
        print(f"Tipo: {self.__tipo}")
        print(f"Motor: {self.__motor}")
        print(f"Color: {self.__color}")
        print(f"Kilometraje: {self.__kilometraje} km")
        print(f"Transmisión: {self.__transmision}")
        print(f"Combustible: {self.__combustible}")
        print(f"Ruedas: {self.__ruedas}")
        print(f"Capacidad de Pasajeros: {self.__capacidad_pasajeros}")
        print(f"Precio de Compra: ${self.__precio_compra:.2f}")
        print(f"Precio de Venta: ${self.__precio_venta:.2f}")

# Ejemplo de uso del programa

# Paso 2: Crear instancias de la clase Auto
auto1 = Auto(marca="Toyota", modelo="Corolla", año=2022, tipo="Nacional", motor="1.8L", color="Blanco", precio_compra=20000, kilometraje=0, transmision="Automática", combustible="Gasolina")
auto2 = Auto(marca="BMW", modelo="X5", año=2023, tipo="Importado", motor="3.0L", color="Negro", precio_compra=60000, kilometraje=0, transmision="Automática", combustible="Gasolina")

# Paso 3: Mostrar la información de los autos
auto1.mostrar_informacion()
print()  # Línea en blanco para separar la salida
auto2.mostrar_informacion()
