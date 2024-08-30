
#Ejercicio:

"""
Una papelería vende cuadernos y lápices. Los cuadernos pueden ser de 50 hojas o de 100 hojas. Los lápices pueden ser de grafito o de colores. El precio de venta es igual al precio de compra multiplicado por 1.30 que corresponde al margen de ganancia. La papelería requiere construir un programa que le permita registrar y visualizar por lo menos dos artículos de ítem. Todos los cuadernos son marca HOJITAS y los lápices son marca RAYAS ya que la papelería es un distribuidor exclusivo.

"""

class Articulo:

    #Constructor
    def __init__(self, tipo, especificacion, precio_compra):
        self.__tipo = tipo
        self.__especificacion = especificacion
        self.__precio_compra = precio_compra
        self.__marca = self.__asignar_marca()
        self.__precio_venta = self.__calcular_precio_venta()

    # Método privado para asignar la marca
    def __asignar_marca(self):
        if self.__tipo == "Cuaderno":
            return "HOJITAS"
        elif self.__tipo == "Lápiz":
            return "RAYAS"
        else:
            return "Desconocido"
    
    # Método privado para calcular el precio de venta
    def __calcular_precio_venta(self):
        return round(self.__precio_compra * 1.30, 2)
    
    # Método para mostrar la información del artículo
    def mostrar_informacion(self):
        print(f"Tipo: {self.__tipo}")
        print(f"Especificación: {self.__especificacion}")
        print(f"Marca: {self.__marca}")
        print(f"Precio de Compra: ${self.__precio_compra:.2f}")
        print(f"Precio de Venta: ${self.__precio_venta:.2f}")

# Ejemplo de uso del programa

# Paso 2: Crear instancias de la clase Articulo
articulo1 = Articulo(tipo="Cuaderno", especificacion="100 hojas", precio_compra=2.00)
articulo2 = Articulo(tipo="Lápiz", especificacion="Grafito", precio_compra=0.50)

# Paso 3: Mostrar la información de los artículos
articulo1.mostrar_informacion()
print()  # Línea en blanco para separar la salida
articulo2.mostrar_informacion()
