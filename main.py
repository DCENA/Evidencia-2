print("SISTEMA DE MONITOREO AGROTECH COOP")

while True:
    print("\nMENÚ PRINCIPAL")
    print("1. Gestión de Campos")
    print("2. Gestión de Parcelas")
    print("3. Gestión de Sensores")
    print("4. Consultar Datos")
    print("5. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        while True:
            print("\nGESTIÓN DE CAMPOS")
            print("1. Ver Campos")
            print("2. Agregar Campo")
            print("3. Modificar Campo")
            print("4. Eliminar Campo")
            print("5. Volver al menú principal")
            menu_interno = input("Seleccione una opción de campo: ")

            if menu_interno == "1":
                print("Mostrando campos registrados...")
            elif menu_interno == "2":
                print("Agregando nuevo campo...")
            elif menu_interno == "3":
                print("Modificando campo existente...")
            elif menu_interno == "4":
                print("Eliminando campo...")
            elif menu_interno == "5":
                break
            else:
                print("Opción inválida. Intente nuevamente.")

    elif opcion == "2":
        while True:
            print("\nGESTIÓN DE PARCELAS")
            print("1. Ver Parcelas")
            print("2. Agregar Parcela")
            print("3. Modificar Parcela")
            print("4. Eliminar Parcela")
            print("5. Volver al menú principal")
            menu_interno = input("Seleccione una opción de parcela: ")

            if menu_interno == "1":
                print("Mostrando parcelas registradas...")
            elif menu_interno == "2":
                print("Agregando nueva parcela...")
            elif menu_interno == "3":
                print("Modificando parcela existente...")
            elif menu_interno == "4":
                print("Eliminando parcela...")
            elif menu_interno == "5":
                break
            else:
                print("Opción inválida. Intente nuevamente.")

    elif opcion == "3":
        while True:
            print("\nGESTIÓN DE SENSORES")
            print("1. Ver Tipos de Sensores")
            print("2. Ver Sensores Instalados")
            print("3. Asignar Sensor a Parcela")
            print("4. Eliminar Sensor")
            print("5. Volver al menú principal")
            menu_interno = input("Seleccione una opción de sensores: ")

            if menu_interno == "1":
                print("Mostrando tipos de sensores disponibles...")
            elif menu_interno == "2":
                print("Mostrando sensores instalados...")
            elif menu_interno == "3":
                print("Asignando sensor a parcela...")
            elif menu_interno == "4":
                print("Eliminando sensor...")
            elif menu_interno == "5":
                break
            else:
                print("Opción inválida. Intente nuevamente.")

    elif opcion == "4":
        print("\nConsultando datos recopilados desde sensores...")

    elif opcion == "5":
        print("Saliendo del sistema. ¡Hasta luego!")
        break

    else:
        print("Opción inválida. Intente nuevamente.")