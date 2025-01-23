import os
import re

# Clase para representar una transferencia
class Transferencia:
    def __init__(self, id, remitente, destinatario, monto, fecha):
        self.id = id
        self.remitente = remitente
        self.destinatario = destinatario
        self.monto = monto
        self.fecha = fecha

    def __str__(self):
        return f"{self.id}\t{self.remitente}\t\t{self.destinatario}\t\t{self.monto:.2f}\t{self.fecha}"

# Función para limpiar pantalla
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

# Función para validar números
def validar_numeros(input_str, longitud_esperada):
    if longitud_esperada > 0 and len(input_str) != longitud_esperada:
        return False  # Longitud incorrecta

    if not input_str.isdigit():
        return False  # Contiene caracteres no numéricos

    return True  # Entrada válida

# Función para aceptar condiciones
def aceptar_condiciones(respuesta):
    return respuesta.lower() == "acepto"

# Función para validar monto
def validar_monto(monto_str):
    if not re.match(r'^\d+(\.\d+)?$', monto_str):
        return False
    return float(monto_str) > 0

# Función para agregar una transferencia
def agregar_transferencia(nombre_archivo):
    try:
        cls()
        print("\n--- Validación de Transferencia ---")

        # Solicitar y validar número de cuenta destino
        cuenta_destino = input("Ingrese el número de cuenta destino (6 dígitos): ")
        if not validar_numeros(cuenta_destino, 6):
            print("Error: Número de cuenta no válido. Debe ingresar 6 dígitos.")
            return

        # Solicitar y validar cédula
        cedula = input("Ingrese su número de cédula (10 dígitos): ")
        if not validar_numeros(cedula, 10):
            print("Error: Número de cédula no válido. Debe ingresar 10 dígitos.")
            return

        # Mostrar condiciones y validar aceptación
        print("\nTérminos y Condiciones:")
        print("El cliente declara que los fondos de esta transacción son lícitos y no provienen de actividades ilegales.")
        confirmacion = input("Escriba 'Acepto' para continuar: ")
        if not aceptar_condiciones(confirmacion):
            print("Error: No aceptó los términos y condiciones.")
            return

        # Solicitar y validar monto
        monto_str = input("Ingrese el monto a transferir: ")
        if not validar_monto(monto_str):
            print("Error: El monto ingresado no es válido. Debe ser un número positivo.")
            return
        monto = float(monto_str)

        # Confirmar detalles y agregar al archivo
        print("\nConfirmación de Transferencia:")
        remitente = input("Ingrese el nombre del remitente: ")
        destinatario = input("Ingrese el nombre del destinatario: ")
        fecha = input("Ingrese la fecha (dd/mm/aaaa): ")

        print(f"Cuenta destino: {cuenta_destino}")
        print(f"Cédula del remitente: {cedula}")
        print(f"Monto a transferir: {monto:.2f}")
        confirmacion = input("\n¿Desea confirmar la transferencia? (Escriba 'Si' para confirmar o 'No' para cancelar): ")

        if confirmacion.lower() != "si":
            print("\nTransacción cancelada.")
            return

        # Crear objeto Transferencia y guardar en archivo
        with open(nombre_archivo, "a") as archivo:
            id = f"{cedula}-{sum(1 for _ in open(nombre_archivo, 'a+')) + 1}"  # Generar ID único
            transferencia = Transferencia(id, remitente, destinatario, monto, fecha)
            archivo.write(f"{transferencia.id} {transferencia.remitente} {transferencia.destinatario} {transferencia.monto:.2f} {transferencia.fecha}\n")

        print("\nTransferencia agregada exitosamente.")

    except Exception as e:
        print(f"Error al agregar transferencia: {e}")
