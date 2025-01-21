def menu_cajero():
    while True:
        print("\n=== Menú del Cajero Automático ===")
        print("1. Retirar dinero")
        print("2. Depositar dinero")
        print("3. Consultar saldo")
        print("4. Transferir dinero")
        print("5. Ver historial de transferencias")
        print("6. Salir")

        try:
            opcion = int(input("Seleccione una opción (1-6): "))
            if opcion < 1 or opcion > 6:
                print("Por favor, elija una opción válida (1-6).")
                continue

            if opcion == 6:
                print("Gracias por usar el cajero automático. ¡Hasta luego!")
                break

            print(f"Ha seleccionado la opción {opcion}.")
            # Aquí puedes agregar las funciones correspondientes según la opción
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número del 1 al 6.")

# Ejecutar el menú
menu_cajero()