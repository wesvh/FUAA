from datetime import date
from controllers.user_controller import UserController
from controllers.account_controller import AccountController
from views.cli_view import CLIView


def console_wrapper(func):
    def wrapper(*args, **kwargs):
        cli_view = args[0]  # El primer argumento siempre debe ser cli_view
        cli_view.limpiar_consola()
        resultado = func(*args, **kwargs)
        cli_view.press_enter()
        return resultado

    return wrapper


@console_wrapper
def registrar_usuario(cli_view: CLIView, user_controller: UserController):
    identificacion, nombres, edad = cli_view.solicitar_datos_usuario()
    mensaje = user_controller.registrar_usuario(identificacion, nombres, edad)
    cli_view.mostrar_mensaje(mensaje)


@console_wrapper
def crear_cuenta(
    cli_view: CLIView,
    user_controller: UserController,
    account_controller: AccountController,
):
    usuarios = user_controller.obtener_usuarios()
    if usuarios:
        usuario = cli_view.seleccionar_usuario(usuarios)
        id_cuenta, tipo_cuenta, monto_apertura = cli_view.solicitar_datos_cuenta(
            usuario
        )
        mensaje = account_controller.crear_cuenta(
            id_cuenta, tipo_cuenta, date.today(), monto_apertura, usuario
        )
        cli_view.mostrar_mensaje(mensaje)
    else:
        cli_view.mostrar_mensaje("Error: No hay usuarios registrados.")


@console_wrapper
def mostrar_usuarios(cli_view: CLIView, user_controller: UserController):
    usuarios = user_controller.obtener_usuarios()
    cli_view.mostrar_usuarios(usuarios)


@console_wrapper
def realizar_transaccion(
    cli_view: CLIView,
    user_controller: UserController,
    account_controller: AccountController,
):
    usuarios = user_controller.obtener_usuarios()
    if usuarios:
        usuario = cli_view.seleccionar_usuario(usuarios)
        if usuario.cuentas:
            cuenta_origen = cli_view.solicitar_datos_transaccion_origen(usuario)
            usuario_destino = cli_view.seleccionar_usuario(usuarios)
            cuenta_destino = None
            monto = 0
            if usuario_destino == usuario:
                cli_view.mostrar_mensaje(
                    "Error: No se puede transferir a la misma cuenta."
                )
                return
            if usuario_destino.cuentas:
                cuenta_destino, monto = cli_view.solicitar_datos_transaccion_destino(
                    usuario_destino
                )

            mensaje = account_controller.realizar_transaccion(
                cuenta_origen.id_cuenta, cuenta_destino.id_cuenta, monto
            )
            cli_view.mostrar_mensaje(mensaje)
        else:
            cli_view.mostrar_mensaje("Error: El usuario no tiene cuentas asociadas.")
    else:
        cli_view.mostrar_mensaje("Error: No hay usuarios registrados.")


@console_wrapper
def revisar_transacciones(
    cli_view: CLIView,
    user_controller: UserController,
    account_controller: AccountController,
):
    usuarios = user_controller.obtener_usuarios()
    if usuarios:
        usuario = cli_view.seleccionar_usuario(usuarios)
        if usuario.cuentas:
            cuenta = cli_view.seleccionar_cuenta(
                usuario.cuentas, "Seleccione la cuenta para revisar transacciones:"
            )
            transacciones = cuenta.obtener_transacciones()
            if transacciones:
                cli_view.mostrar_transacciones(transacciones)
            else:
                cli_view.mostrar_mensaje(
                    "No hay transacciones registradas para esta cuenta."
                )
        else:
            cli_view.mostrar_mensaje("Error: El usuario no tiene cuentas asociadas.")
    else:
        cli_view.mostrar_mensaje("Error: No hay usuarios registrados.")


def main():
    user_controller = UserController()
    account_controller = AccountController()
    cli_view = CLIView()

    while True:
        cli_view.mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_usuario(cli_view, user_controller)

        elif opcion == "2":
            crear_cuenta(cli_view, user_controller, account_controller)

        elif opcion == "3":
            mostrar_usuarios(cli_view, user_controller)

        elif opcion == "4":
            realizar_transaccion(cli_view, user_controller, account_controller)

        elif opcion == "5":
            revisar_transacciones(cli_view, user_controller, account_controller)

        elif opcion == "6":
            cli_view.mostrar_mensaje("Saliendo del programa.")
            break

        else:
            cli_view.mostrar_mensaje("Opción no válida, por favor intente de nuevo.\n")


if __name__ == "__main__":
    main()
