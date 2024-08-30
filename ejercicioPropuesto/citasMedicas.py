
"""
Ejercicio de Programación Orientada a Objetos (POO): Sistema de Gestión de Citas Médicas
"""

#Descripción del Problema:

"""En la actualidad, con el aumento de la demanda de servicios médicos, los centros de salud enfrentan dificultades para gestionar las citas médicas de manera eficiente. Muchos pacientes tienen que esperar largos períodos para obtener una cita, y la falta de organización puede llevar a la pérdida de citas o a la sobrecarga de los médicos. Un sistema que permita gestionar citas de manera organizada, asegurando que los pacientes sean atendidos según su prioridad y disponibilidad, puede mejorar significativamente la eficiencia y satisfacción tanto de los pacientes como del personal médico."""


#Objetivo del Programa:

"""El programa permite a los pacientes registrar citas médicas, asignar un médico y horario disponible, y gestionar la lista de citas de manera que se puedan visualizar y modificar las citas programadas. El sistema también debería ser capaz de priorizar a los pacientes de acuerdo a la urgencia de su caso."""

#Clase paciente
class Paciente:
    #Constructor:
    def __init__(self, nombre, edad, sintomas, prioridad):
        self.__nombre = nombre
        self.__edad = edad
        self.__sintomas = sintomas
        self.__prioridad = prioridad

    def mostrar_informacion(self):
        print(f"Nombre: {self.__nombre}, Edad: {self.__edad}, Síntomas: {self.__sintomas}, Prioridad: {self.__prioridad}")

    def obtener_prioridad(self):
        return self.__prioridad


#Clase medico
class Medico:
    def __init__(self, nombre, especialidad):
        self.__nombre = nombre
        self.__especialidad = especialidad

    def mostrar_informacion(self):
        print(f"Doctor: {self.__nombre}, Especialidad: {self.__especialidad}")


#Clase cita
class Cita:
    def __init__(self, paciente, medico, fecha, hora):
        self.__paciente = paciente
        self.__medico = medico
        self.__fecha = fecha
        self.__hora = hora

    def mostrar_informacion(self):
        print(f"Cita para {self.__paciente._Paciente__nombre} con el Dr. {self.__medico._Medico__nombre} el {self.__fecha} a las {self.__hora}")

    def obtener_prioridad(self):
        return self.__paciente.obtener_prioridad()


#Clase sistema de citas
class SistemaCitas:
    def __init__(self):
        self.__citas = []

    def agregar_cita(self, cita):
        self.__citas.append(cita)
        self.__citas.sort(key=lambda c: c.obtener_prioridad(), reverse=True)  # Ordena las citas por prioridad

    def mostrar_citas(self):
        if not self.__citas:
            print("No hay citas programadas.")
        else:
            for cita in self.__citas:
                cita.mostrar_informacion()


# Implementación del sistema

# Creación de médicos
medico1 = Medico("Dr. Juan Pérez", "Cardiología")
medico2 = Medico("Dra. María López", "Neurología")

# Creación del sistema de citas
sistema = SistemaCitas()

# Ingreso de pacientes y sus citas
while True:
    nombre = input("Ingrese el nombre del paciente: ")
    edad = int(input("Ingrese la edad del paciente: "))
    sintomas = input("Describa los síntomas del paciente: ")
    prioridad = int(input("Ingrese la prioridad (1-5) del paciente (1 = Baja, 5 = Alta): "))

    paciente = Paciente(nombre, edad, sintomas, prioridad)

    print("\nSeleccione el médico:")
    print("1. Dr. Juan Pérez (Cardiología)")
    print("2. Dra. María López (Neurología)")
    opcion_medico = int(input("Ingrese el número del médico: "))
    if opcion_medico == 1:
        medico = medico1
    else:
        medico = medico2

    fecha = input("Ingrese la fecha de la cita (dd/mm/aaaa): ")
    hora = input("Ingrese la hora de la cita (hh:mm): ")

    cita = Cita(paciente, medico, fecha, hora)
    sistema.agregar_cita(cita)

    continuar = input("¿Desea agregar otra cita? (s/n): ")
    if continuar.lower() != 's':
        break

# Mostrar citas programadas
print("\nCitas programadas:")
sistema.mostrar_citas()



#Explicacion:

"""
Clases y Encapsulamiento:

Paciente: Esta clase encapsula la información del paciente, como su nombre, edad, síntomas y prioridad. La prioridad se utiliza para organizar las citas según la urgencia.

Medico: Esta clase encapsula la información del 
médico, como su nombre y especialidad.

Cita: Esta clase encapsula la información de una cita médica, asociando un paciente con un médico en una fecha y hora específica.

Sistema de Citas:
La clase SistemaCitas gestiona una lista de citas, permitiendo agregar nuevas citas y ordenarlas según la prioridad del paciente. Este sistema es vital para la gestión de citas en un entorno con alta demanda de servicios médicos.

Interacción con el Usuario:
El programa solicita al usuario que ingrese los datos del paciente, seleccione un médico, y programe una cita. Luego, las citas se muestran ordenadas por prioridad, lo que simula la gestión de citas en un entorno real.
"""

#Problema a resolver:
"""
Este sistema de gestión de citas médicas permite a una clínica o consultorio organizar y priorizar las citas de los pacientes, mejorando la eficiencia del proceso y asegurando que los pacientes más urgentes sean atendidos primero. Esto es especialmente útil en situaciones de alta demanda médica, donde la organización y priorización son claves para brindar un servicio de calidad.
"""