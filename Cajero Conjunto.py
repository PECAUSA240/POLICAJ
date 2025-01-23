import random

# Clase principal del cajero
class CajeroAutomatico:
    def __init__(self, saldo_inicial=0):
        self.saldo = saldo_inicial
        self.historial_transferencias = []

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

    def test_transferir_dinero(self, cuenta_destino, monto):
        if monto <= 0:
            print("El monto debe ser mayor que cero.")
            return
        if monto > self.saldo:
            print("Saldo insuficiente para realizar la transferencia.")
            return
        self.saldo -= monto
        print(f"Has transferido ${monto:.2f} a la cuenta {cuenta_destino}.")
        self.historial_transferencias.append((cuenta_destino, monto))

    def mostrar_historial_transferencias(self):
        if not self.historial_transferencias:
            print("No hay transferencias realizadas.")
        else:
            print("\nHistorial de Transferencias:")
            for idx, (cuenta, monto) in enumerate(self.historial_transferencias, 1):
                print(f"{idx}. Cuenta: {cuenta} - Monto: ${monto:.2f}")

# Funciones auxiliares
def generar_numero_cuenta():
    return random.randint(100000, 999999)

def validar_numeros(input_str, longitud_esperada):
    if longitud_esperada > 0 and len(input_str) != longitud_esperada:
        return False
    if not input_str.isdigit():
        return False
    return True

def registro_usuarios():
    print("--- Registro de Usuario ---")
    id_usuario = input("Ingrese su número de identificación (solo números): ")
    while not validar_numeros(id_usuario, 10):
        print("Error: Solo se permiten números de 10 dígitos. Intente nuevamente.")
        id_usuario = input("Ingrese su número de identificación (solo números): ")

    numero_cuenta = generar_numero_cuenta()
    print(f"Su número de cuenta generado es: {numero_cuenta}")

    contrasena = input("Ingrese una contraseña (solo números): ")
    while not validar_numeros(contrasena, 6):
        print("Error: Solo se permiten números de 6 dígitos. Intente nuevamente.")
        contrasena = input("Ingrese una contraseña (solo números): ")

    print("Registro exitoso. Puede iniciar sesión ahora.")
    return id_usuario, numero_cuenta, contrasena

def inicio_sesion(usuarios):
    print("--- Inicio de Sesión ---")
    while True:
        id_usuario = input("Ingrese su número de identificación: ")
        if not validar_numeros(id_usuario, 10):
            print("Error: Solo se permiten números de 10 dígitos. Intente nuevamente.")
            continue

        numero_cuenta = input("Ingrese su número de cuenta: ")
        if not validar_numeros(numero_cuenta, 6):
            print("Error: Solo se permiten números de 6 dígitos. Intente nuevamente.")
            continue

        contrasena = input("Ingrese su contraseña: ")
        if not validar_numeros(contrasena, 6):
            print("Error: Solo se permiten números de 6 dígitos. Intente nuevamente.")
            continue

        for usuario in usuarios:
            if (usuario["id_usuario"] == id_usuario and
                str(usuario["numero_cuenta"]) == numero_cuenta and
                usuario["contrasena"] == contrasena):
                print("Inicio de sesión exitoso. ¡Bienvenido al sistema!")
                return usuario

        print("Error: Credenciales incorrectas. Intente nuevamente.")

def menu_principal():
    usuarios = []

    # Registro e inicio de sesión
    id_usuario, numero_cuenta, contrasena = registro_usuarios()
    usuarios.append({"id_usuario": id_usuario, "numero_cuenta": numero_cuenta, "contrasena": contrasena, "cajero": CajeroAutomatico(saldo_inicial=500)})
    usuario_actual = inicio_sesion(usuarios)

    cajero = usuario_actual["cajero"]

    # Menú principal
    while True:
        print("\n--- Menú Principal ---")
        print("1. Consultar saldo")
        print("2. Depositar dinero")
        print("3. Retirar dinero")
        print("4. Transferir dinero")
        print("5. Ver historial de transferencias")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            cajero.consultar_saldo()
        elif opcion == "2":
            try:
                monto = float(input("Ingrese el monto a depositar: "))
                cajero.depositar_dinero(monto)
            except ValueError:
                print("Error: Por favor, ingrese un monto válido.")
        elif opcion == "3":
            try:
                monto = float(input("Ingrese el monto a retirar: "))
                cajero.retirar_dinero(monto)
            except ValueError:
                print("Error: Por favor, ingrese un monto válido.")
        elif opcion == "4":
            cuenta_destino = input("Ingrese el número de cuenta destino: ")
            if not validar_numeros(cuenta_destino, 6):
                print("Error: Número de cuenta no válido. Debe ingresar 6 dígitos.")
                continue
            try:
                monto = float(input("Ingrese el monto a transferir: "))
                cajero.transferir_dinero(cuenta_destino, monto)
            except ValueError:
                print("Error: Por favor, ingrese un monto válido.")
        elif opcion == "5":
            cajero.mostrar_historial_transferencias()
        elif opcion == "6":
            print("Gracias por usar el cajero automático. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

# Ejecutar el programa
if __name__ == "__main__":
    menu_principal()
