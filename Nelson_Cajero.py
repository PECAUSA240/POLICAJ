class CajeroAutomatico:
    def __init__(self, saldo_inicial=0):
        self.saldo = saldo_inicial

    def consultar_saldo(self):
        print(f"Saldo actual: ${self.saldo:.2f}")

    def depositar_dinero(self, monto):
        if monto > 0:
            self.saldo += monto
            print(f"Has depositado ${monto:.2f}. Saldo actual: ${self.saldo:.2f}")
        else:
            print("El monto debe ser mayor que cero.")

    def retirar_dinero(self, monto):
        if monto > self.saldo:
            print("Saldo insuficiente para realizar el retiro.")
        elif monto <= 0:
            print("El monto debe ser mayor que cero.")
        else:
            self.saldo -= monto
            print(f"Has retirado ${monto:.2f}. Saldo actual: ${self.saldo:.2f}")

def menu_cajero():
    cajero = CajeroAutomatico(saldo_inicial=500)  # Saldo inicial predeterminado
    while True:
        print("\n--- Cajero Automático ---")
        print("1. Consultar saldo")
        print("2. Depositar dinero")
        print("3. Retirar dinero")
        print("4. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            cajero.consultar_saldo()
        elif opcion == "2":
            try:
                monto = float(input("Ingresa el monto a depositar: "))
                cajero.depositar_dinero(monto)
            except ValueError:
                print("Por favor, ingresa un monto válido.")
        elif opcion == "3":
            try:
                monto = float(input("Ingresa el monto a retirar: "))
                cajero.retirar_dinero(monto)
            except ValueError:
                print("Por favor, ingresa un monto válido.")
        elif opcion == "4":
            print("Gracias por usar el cajero automático. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

# Ejecutar el menú del cajero automático
menu_cajero()
