class CuentaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            print(f"Depósito exitoso. Saldo actual: {self.saldo}")
        else:
            print("La cantidad debe ser mayor que cero.")

    def retirar(self, cantidad):
        if cantidad > 0 and cantidad <= self.saldo:
            self.saldo -= cantidad
            print(f"Retiro exitoso. Saldo actual: {self.saldo}")
        else:
            print("Fondos insuficientes o cantidad inválida.")

# Ejemplo de uso
mi_cuenta = CuentaBancaria(titular="Juan Pérez", saldo=1000)
mi_cuenta.depositar(200)
mi_cuenta.retirar(150)

