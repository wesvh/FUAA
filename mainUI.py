from datetime import date
from controllers.user_controller import UserController
from controllers.account_controller import AccountController
from views.ui_view import UIView
import tkinter as tk


def registrar_usuario(ui_view: UIView, user_controller: UserController):
    identificacion, nombres, edad = ui_view.solicitar_datos_usuario()
    mensaje = user_controller.registrar_usuario(identificacion, nombres, edad)
    ui_view.mostrar_mensaje(mensaje)


def crear_cuenta(
    ui_view: UIView,
    user_controller: UserController,
    account_controller: AccountController,
):
    usuarios = user_controller.obtener_usuarios()
    if usuarios:
        usuario = ui_view.seleccionar_usuario(usuarios)
        if not usuario:
            ui_view.mostrar_mensaje("Error: Usuario no válido.")
            return
        id_cuenta, tipo_cuenta, monto_apertura = ui_view.solicitar_datos_cuenta(usuario)
        mensaje = account_controller.crear_cuenta(
            id_cuenta, tipo_cuenta, date.today(), monto_apertura, usuario
        )
        ui_view.mostrar_mensaje(mensaje)
    else:
        ui_view.mostrar_mensaje("Error: No hay usuarios registrados.")


def mostrar_usuarios(ui_view: UIView, user_controller: UserController):
    usuarios = user_controller.obtener_usuarios()
    ui_view.mostrar_usuarios(usuarios)


def realizar_transaccion(
    ui_view: UIView,
    user_controller: UserController,
    account_controller: AccountController,
):
    usuarios = user_controller.obtener_usuarios()
    if usuarios:
        usuario = ui_view.seleccionar_usuario(usuarios)
        if usuario.cuentas:
            cuenta_origen = ui_view.solicitar_datos_transaccion_origen(usuario)
            usuario_destino = ui_view.seleccionar_usuario(usuarios)
            if usuario_destino.cuentas:
                cuenta_destino, monto = ui_view.solicitar_datos_transaccion_destino(
                    usuario_destino
                )
                if cuenta_destino == cuenta_origen:
                    ui_view.mostrar_mensaje(
                        "Error: No se puede transferir a la misma cuenta."
                    )
                    return
                mensaje = account_controller.realizar_transaccion(
                    cuenta_origen.id_cuenta, cuenta_destino.id_cuenta, monto
                )
                ui_view.mostrar_mensaje(mensaje)
            else:
                ui_view.mostrar_mensaje(
                    "Error: El usuario destino no tiene cuentas asociadas."
                )
        else:
            ui_view.mostrar_mensaje("Error: El usuario no tiene cuentas asociadas.")
    else:
        ui_view.mostrar_mensaje("Error: No hay usuarios registrados.")


def revisar_transacciones(
    ui_view: UIView,
    user_controller: UserController,
    account_controller: AccountController,
):
    usuarios = user_controller.obtener_usuarios()
    if usuarios:
        usuario = ui_view.seleccionar_usuario(usuarios)
        if usuario.cuentas:
            cuenta = ui_view.seleccionar_cuenta(
                usuario.cuentas, "Seleccione la cuenta para revisar transacciones:"
            )
            transacciones = cuenta.obtener_transacciones()
            if transacciones:
                ui_view.mostrar_transacciones(transacciones)
            else:
                ui_view.mostrar_mensaje(
                    "No hay transacciones registradas para esta cuenta."
                )
        else:
            ui_view.mostrar_mensaje("Error: El usuario no tiene cuentas asociadas.")
    else:
        ui_view.mostrar_mensaje("Error: No hay usuarios registrados.")


def main():
    root = tk.Tk()
    root.geometry("400x400")
    root.title("Sistema de Ahorro UI")

    user_controller = UserController()
    account_controller = AccountController()
    ui_view = UIView(root)

    "make a label to Show the title"
    tk.Label(root, text="Sistema de Ahorro", font=("Helvetica", 16)).pack(pady=10)
    tk.Label(root, text="Modelos de Programacion", font=("Helvetica", 16)).pack(pady=5)
    tk.Label(
        root,
        text="Desarrollado por: Esteban Villada Henao grupo 202460-6A - 62 \n Cristian Murillo Soto 202460-6A - 61 ",
        font=("Helvetica", 12),
    ).pack(pady=5)

    # Menú gráfico con botones
    tk.Button(
        root,
        text="Registrar Usuario",
        command=lambda: registrar_usuario(ui_view, user_controller),
    ).pack(pady=5)
    tk.Button(
        root,
        text="Crear Cuenta",
        command=lambda: crear_cuenta(ui_view, user_controller, account_controller),
    ).pack(pady=5)
    tk.Button(
        root,
        text="Mostrar Usuarios",
        command=lambda: mostrar_usuarios(ui_view, user_controller),
    ).pack(pady=5)
    tk.Button(
        root,
        text="Realizar Transacción",
        command=lambda: realizar_transaccion(
            ui_view, user_controller, account_controller
        ),
    ).pack(pady=5)
    tk.Button(
        root,
        text="Revisar Transacciones",
        command=lambda: revisar_transacciones(
            ui_view, user_controller, account_controller
        ),
    ).pack(pady=5)
    tk.Button(root, text="Salir", command=root.quit).pack(pady=20)

    root.mainloop()


if __name__ == "__main__":
    main()
