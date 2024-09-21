import random
import tkinter as tk
from tkinter import messagebox
import hashlib


class UIView:
    def __init__(self, root):
        self.root = root

    def limpiar_consola(self):
        # No es necesario en una interfaz gráfica
        pass

    def press_enter(self):
        # No se necesita en una UI
        pass

    def mostrar_menu(self):
        # El menú ya se maneja con botones, no se necesita esta implementación
        pass

    def solicitar_datos_usuario(self):
        # Ventana para solicitar los datos del usuario
        self.new_window = tk.Toplevel(self.root)
        self.new_window.title("Registrar Usuario")

        tk.Label(self.new_window, text="Identificación:").pack()
        identificacion = tk.Entry(self.new_window)
        identificacion.pack()

        tk.Label(self.new_window, text="Nombres:").pack()
        nombres = tk.Entry(self.new_window)
        nombres.pack()

        tk.Label(self.new_window, text="Edad:").pack()
        edad = tk.Entry(self.new_window)
        edad.pack()

        def submit():
            id_value = identificacion.get()
            nombre_value = nombres.get()
            try:
                edad_value = int(edad.get())
            except ValueError:
                edad_value = None

            if not id_value or not nombre_value or edad_value is None:
                messagebox.showerror(
                    "Error",
                    "Todos los campos son obligatorios y la edad debe ser numérica.",
                )
            else:
                self.user_data = (id_value, nombre_value, edad_value)
                self.new_window.destroy()

        submit_button = tk.Button(self.new_window, text="Registrar", command=submit)
        submit_button.pack(pady=10)

        self.root.wait_window(self.new_window)
        return self.user_data

    def seleccionar_usuario(self, usuarios):
        # Ventana para seleccionar un usuario de una lista
        if not usuarios:
            messagebox.showerror(
                "Error", "No hay usuarios disponibles para seleccionar."
            )
            return None

        self.new_window = tk.Toplevel(self.root)
        self.new_window.title("Seleccionar Usuario")

        var = tk.StringVar(value="")

        tk.Label(self.new_window, text="Seleccione un usuario:").pack()

        for usuario in usuarios:
            radio_button = tk.Radiobutton(
                self.new_window,
                text=f"{usuario.nombres} (ID: {usuario.identificacion})",
                variable=var,
                value=usuario.identificacion,
            )
            radio_button.pack()

        def submit():
            if not var.get():
                messagebox.showerror("Error", "Debe seleccionar un usuario.")
            else:
                self.selected_user = next(
                    (u for u in usuarios if u.identificacion == var.get()), None
                )
                self.new_window.destroy()

        submit_button = tk.Button(self.new_window, text="Seleccionar", command=submit)
        submit_button.pack(pady=10)

        self.root.wait_window(self.new_window)
        return self.selected_user

    def solicitar_datos_cuenta(self, usuario):
        # Ventana para solicitar los datos de una cuenta
        self.new_window = tk.Toplevel(self.root)
        self.new_window.title("Crear Cuenta")

        tk.Label(
            self.new_window,
            text="ID de la cuenta (deje en blanco para generar automáticamente):",
        ).pack()
        id_cuenta = tk.Entry(self.new_window)
        id_cuenta.pack()

        tk.Label(self.new_window, text="Tipo de cuenta:").pack()

        # Radio buttons for "Ahorros" and "Corriente"
        tipo_cuenta_var = tk.StringVar(value="Ahorros")  # Set default value

        tk.Radiobutton(
            self.new_window, text="Ahorros", variable=tipo_cuenta_var, value="Ahorros"
        ).pack(anchor="w")
        tk.Radiobutton(
            self.new_window,
            text="Corriente",
            variable=tipo_cuenta_var,
            value="Corriente",
        ).pack(anchor="w")

        tk.Label(self.new_window, text="Monto de apertura:").pack()
        monto_apertura = tk.Entry(self.new_window)
        monto_apertura.pack()

        def submit():
            import random

            stringToHashRand = usuario.identificacion + str(random.random())
            hashRand = hashlib.md5(stringToHashRand.encode()).hexdigest()[:8]
            cuenta_id = id_cuenta.get() or hashRand
            tipo = tipo_cuenta_var.get()  # Get the selected value from the RadioButton
            try:
                monto = float(monto_apertura.get())
            except ValueError:
                monto = None

            if not tipo or monto is None:
                messagebox.showerror(
                    "Error",
                    "Todos los campos son obligatorios y el monto debe ser numérico.",
                )
            else:
                self.cuenta_data = (cuenta_id, tipo, monto)
                self.new_window.destroy()

        submit_button = tk.Button(self.new_window, text="Crear", command=submit)
        submit_button.pack(pady=10)

        self.root.wait_window(self.new_window)
        return self.cuenta_data

    def seleccionar_cuenta(self, cuentas, mensaje="Seleccione una cuenta:"):
        # Ventana para seleccionar una cuenta
        if not cuentas:
            messagebox.showerror(
                "Error", "No hay cuentas disponibles para seleccionar."
            )
            return None

        self.new_window = tk.Toplevel(self.root)
        self.new_window.title("Seleccionar Cuenta")

        var = tk.StringVar(value="")

        tk.Label(self.new_window, text=mensaje).pack()

        for cuenta in cuentas:
            radio_button = tk.Radiobutton(
                self.new_window,
                text=f"{cuenta.id_cuenta} - Saldo: {cuenta.saldo}",
                variable=var,
                value=cuenta.id_cuenta,
            )
            radio_button.pack()

        def submit():
            if not var.get():
                messagebox.showerror("Error", "Debe seleccionar una cuenta.")
            else:
                self.selected_cuenta = next(
                    (c for c in cuentas if c.id_cuenta == var.get()), None
                )
                self.new_window.destroy()

        submit_button = tk.Button(self.new_window, text="Seleccionar", command=submit)
        submit_button.pack(pady=10)

        self.root.wait_window(self.new_window)
        return self.selected_cuenta

    def solicitar_datos_transaccion_origen(self, usuario):
        # Ventana para seleccionar la cuenta origen de la transacción
        return self.seleccionar_cuenta(usuario.cuentas, "Seleccione la cuenta origen:")

    def solicitar_datos_transaccion_destino(self, usuario):
        # Ventana para seleccionar la cuenta destino y monto
        cuenta_destino = self.seleccionar_cuenta(
            usuario.cuentas, "Seleccione la cuenta destino:"
        )

        if not cuenta_destino:
            return None, None

        self.new_window = tk.Toplevel(self.root)
        self.new_window.title("Ingresar Monto de la Transacción")

        tk.Label(self.new_window, text="Ingrese el monto de la transacción:").pack()
        monto = tk.Entry(self.new_window)
        monto.pack()

        def submit():
            try:
                monto_value = float(monto.get())
                if monto_value <= 0:
                    raise ValueError
                self.transaccion_data = (cuenta_destino, monto_value)
                self.new_window.destroy()
            except ValueError:
                messagebox.showerror(
                    "Error", "El monto debe ser un número válido mayor que 0."
                )

        submit_button = tk.Button(self.new_window, text="Confirmar", command=submit)
        submit_button.pack(pady=10)

        self.root.wait_window(self.new_window)
        return self.transaccion_data

    def mostrar_mensaje(self, mensaje):
        # Mostrar un mensaje en una ventana emergente
        messagebox.showinfo("Mensaje", mensaje)

    def mostrar_usuarios(self, usuarios):
        # Mostrar la lista de usuarios en una ventana
        self.new_window = tk.Toplevel(self.root)
        self.new_window.title("Usuarios Registrados")

        if not usuarios:
            tk.Label(self.new_window, text="No hay usuarios registrados.").pack()
        else:
            for usuario in usuarios:
                tk.Label(self.new_window, text=usuario.mostrar_informacion()).pack()

        close_button = tk.Button(
            self.new_window, text="Cerrar", command=self.new_window.destroy
        )
        close_button.pack(pady=10)

    def mostrar_transacciones(self, transacciones):
        # Mostrar la lista de transacciones en una ventana
        self.new_window = tk.Toplevel(self.root)
        self.new_window.title("Transacciones")

        if not transacciones:
            tk.Label(self.new_window, text="No hay transacciones registradas.").pack()
        else:
            for transaccion in transacciones:
                tk.Label(self.new_window, text=transaccion.mostrar_informacion()).pack()

        close_button = tk.Button(
            self.new_window, text="Cerrar", command=self.new_window.destroy
        )
        close_button.pack(pady=10)
