#Definir clase
class Transferencia:
    def __init__(self, id, remitente, destinatario, monto, fecha):
        self.id = id
        self.remitente = remitente
        self.destinatario = destinatario
        self.monto = monto
        self.fecha = fecha
    
    def __str__(self):
        return f"{self.id}\t{self.remitente}\t{self.destinatario}\t{self.monto:.2f}\t{self.fecha}"

def cls():
    """Función para limpiar la consola (dependiendo del sistema operativo)"""
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_historial(nombre_archivo):
    try:
        cls()
        with open(nombre_archivo, "r") as archivo:
            print("\nHistorial de Transferencias:")
            print("ID\tRemitente\tDestinatario\tMonto\t\tFecha")
            print("-----------------------------------------------------------")

            # Leer y mostrar cada línea del archivo
            for linea in archivo:
                datos = linea.split()
                if len(datos) != 5:  # Asegurarse de que la línea tenga el número correcto de columnas
                    #Mensaje de error en la línea
                    print(f"Error en la línea: {linea.strip()} (Formato incorrecto)")
                    continue

                id, remitente, destinatario, monto, fecha = datos[0], datos[1], datos[2], datos[3], datos[4]
                
                try:
                    monto = float(monto)  # Convertir el monto a float
                    transferencia = Transferencia(id, remitente, destinatario, monto, fecha)
                    print(transferencia)
                except ValueError:
                    print(f"Error al convertir el monto en la línea: {linea.strip()}")

    except FileNotFoundError:
        print("No se encontró el archivo de historial.")
    except Exception as e:
        print(f"Error al mostrar historial: {e}")
