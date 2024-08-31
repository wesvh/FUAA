import os
import hashlib


class CLIView:
    @staticmethod
    def limpiar_consola():
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")

    @staticmethod
    def press_enter():
        input("Presione Enter para continuar...")

    @staticmethod
    def mostrar_menu():
        CLIView.limpiar_consola()
        print("Sistema de Ahorro CLI")
        print("1. Registrar Usuario")
        print("2. Crear Cuenta")
        print("3. Mostrar Usuarios")
        print("4. Realizar Transacción")
        print("5. Revisar Transacciones")
        print("6. Salir")

    @staticmethod
    def solicitar_datos_usuario():
        CLIView.limpiar_consola()
        identificacion = input("Ingrese la identificación del usuario: ")
        nombres = input("Ingrese los nombres del usuario: ")
        edad = int(input("Ingrese la edad del usuario: "))
        return identificacion, nombres, edad

    @staticmethod
    def seleccionar_usuario(usuarios):
        CLIView.limpiar_consola()
        print("Seleccione un usuario:")
        for i, usuario in enumerate(usuarios, start=1):
            print(f"{i}. {usuario.nombres} (ID: {usuario.identificacion})")
        opcion = int(input("Ingrese el número de usuario: "))
        if (opcion - 1) < 0 or (opcion - 1) >= len(usuarios):
            return CLIView.seleccionar_usuario(usuarios)
        return usuarios[opcion - 1]

    @staticmethod
    def solicitar_datos_cuenta(usuario):
        CLIView.limpiar_consola()
        id_cuenta = input(
            "Ingrese el ID de la cuenta (o deje en blanco para generar automáticamente): "
        )
        if not id_cuenta:
            id_cuenta = hashlib.md5(usuario.identificacion.encode()).hexdigest()[
                :8
            ]  # Generar ID de cuenta con hash
            print(f"ID de cuenta generado automáticamente: {id_cuenta}")
        tipo_cuenta = input("Ingrese el tipo de cuenta (Ahorros/Corriente): ")
        monto_apertura = float(input("Ingrese el monto de apertura: "))
        return id_cuenta, tipo_cuenta, monto_apertura

    @staticmethod
    def seleccionar_cuenta(cuentas, mensaje="Seleccione una cuenta:"):
        CLIView.limpiar_consola()
        print(mensaje)
        for i, cuenta in enumerate(cuentas, start=1):
            print(f"{i}. {cuenta.id_cuenta} - Saldo: {cuenta.saldo}")
        opcion = int(input("Ingrese el número de cuenta: "))
        if (opcion - 1) < 0 or (opcion - 1) >= len(cuentas):
            return CLIView.seleccionar_cuenta(cuentas, mensaje)
        return cuentas[opcion - 1]

    @staticmethod
    def solicitar_datos_transaccion_origen(usuario):
        CLIView.limpiar_consola()
        cuenta_origen = CLIView.seleccionar_cuenta(
            usuario.cuentas, "Seleccione la cuenta origen:"
        )
        return cuenta_origen

    @staticmethod
    def solicitar_datos_transaccion_destino(usuario):
        CLIView.limpiar_consola()
        cuenta_destino = CLIView.seleccionar_cuenta(
            usuario.cuentas, "Seleccione la cuenta destino:"
        )
        monto = float(input("Ingrese el monto de la transacción: "))
        return cuenta_destino, monto

    @staticmethod
    def mostrar_mensaje(mensaje):
        CLIView.limpiar_consola()
        print(mensaje)

    @staticmethod
    def mostrar_usuarios(usuarios):
        CLIView.limpiar_consola()
        if not usuarios:
            print("No hay usuarios registrados.\n")
        else:
            for usuario in usuarios:
                usuario.actualizar_cuentas()
                print(usuario.mostrar_informacion())
                print()

    @staticmethod
    def mostrar_transacciones(transacciones):
        CLIView.limpiar_consola()
        if not transacciones:
            print("No hay transacciones registradas.\n")
        else:
            for transaccion in transacciones:
                print(transaccion.mostrar_informacion())
                print()
