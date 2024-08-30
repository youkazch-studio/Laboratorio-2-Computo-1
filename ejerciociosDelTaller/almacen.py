
#Ejercicio:

"""
Un almacén vende dispositivos electrónicos (celulares, tablets y portá- tiles). Todos PHR que es una nueva marca que está entrando en el mer- cado. Se requiere almacenar sus 6 principales características. Todos son productos importados y su precio de venta es igual al precio de compra multiplicado por 1.7 que corresponde a su margen de ganancia.

"""

class DispositivoElectronico:
    #Constructor:
    def __init__(self, tipo, modelo, procesador, memoria, almacenamiento, precio_compra):
        self.__tipo = tipo  # Celular, Tablet o Portátil
        self.__modelo = modelo
        self.__procesador = procesador
        self.__memoria = memoria
        self.__almacenamiento = almacenamiento
        self.__precio_compra = precio_compra

        # Características fijas
        self.__marca = "PHR"
        self.__origen = "Importado"

        # Cálculo del precio de venta
        self.__precio_venta = self.__calcular_precio_venta()

    # Método privado para calcular el precio de venta
    def __calcular_precio_venta(self):
        return round(self.__precio_compra * 1.7, 2)

    # Método para mostrar la información del dispositivo
    def mostrar_informacion(self):
        print(f"Tipo: {self.__tipo}")
        print(f"Modelo: {self.__modelo}")
        print(f"Procesador: {self.__procesador}")
        print(f"Memoria RAM: {self.__memoria} GB")
        print(f"Almacenamiento: {self.__almacenamiento} GB")
        print(f"Marca: {self.__marca}")
        print(f"Origen: {self.__origen}")
        print(f"Precio de Compra: ${self.__precio_compra:.2f}")
        print(f"Precio de Venta: ${self.__precio_venta:.2f}")

# Ejemplo de uso del programa

# Paso 2: Crear instancias de la clase DispositivoElectronico
dispositivo1 = DispositivoElectronico(tipo="Celular", modelo="X100", procesador="Snapdragon 888", memoria=8, almacenamiento=128, precio_compra=500)
dispositivo2 = DispositivoElectronico(tipo="Tablet", modelo="T200", procesador="Apple M1", memoria=8, almacenamiento=256, precio_compra=800)

# Paso 3: Mostrar la información de los dispositivos
dispositivo1.mostrar_informacion()
print()  # Línea en blanco para separar la salida
dispositivo2.mostrar_informacion()
