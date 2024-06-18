from abc import ABC, abstractmethod

class Empleado(ABC):
    def __init__(self, nombre):
        self.nombre = nombre

    @abstractmethod
    def calcular_salario(self):
        pass

    @abstractmethod
    def mostrar_informacion(self):
        pass

class EmpleadoTiempoCompleto(Empleado):
    def __init__(self, nombre, salario_base):
        super().__init__(nombre)
        self.salario_base = salario_base

    def calcular_salario(self):
        return self.salario_base

    def mostrar_informacion(self):
        print(f"Empleado a tiempo completo: {self.nombre}")

class EmpleadoMedioTiempo(Empleado):
    def __init__(self, nombre, horas_trabajadas, tarifa_por_hora):
        super().__init__(nombre)
        self.horas_trabajadas = horas_trabajadas
        self.tarifa_por_hora = tarifa_por_hora

    def calcular_salario(self):
        return self.horas_trabajadas * self.tarifa_por_hora

    def mostrar_informacion(self):
        print(f"Empleado a medio tiempo: {self.nombre}")

class Contratista(Empleado):
    def __init__(self, nombre, tarifa_por_proyecto):
        super().__init__(nombre)
        self.tarifa_por_proyecto = tarifa_por_proyecto

    def calcular_salario(self):
        return self.tarifa_por_proyecto

    def mostrar_informacion(self):
        print(f"Contratista: {self.nombre}")


empleados = [
    EmpleadoTiempoCompleto("Ana", salario_base=50000),
    EmpleadoMedioTiempo("Carlos", horas_trabajadas=20, tarifa_por_hora=25),
    Contratista("Eva", tarifa_por_proyecto=1500)
]
def listar(lista):
    for empleado in lista:
        empleado.mostrar_informacion()
        print(f"Salario: ${empleado.calcular_salario()}")

listar(empleados)