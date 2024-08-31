class Usuario:
    def __init__(self, identificacion, nombres, edad):
        self.identificacion = identificacion
        self.nombres = nombres
        self.edad = edad
        self.cuentas = []  # Lista de cuentas asociadas

    def agregar_cuenta(self, cuenta):
        self.cuentas.append(cuenta)

    def mostrar_informacion(self):
        cuentas_info = "\n".join(
            [cuenta.mostrar_informacion() for cuenta in self.cuentas]
        )
        return f"Usuario: {self.nombres}, Identificación: {self.identificacion}, Edad: {self.edad}\nCuentas:\n{cuentas_info}"

    def actualizar_cuentas(self):
        for cuenta in self.cuentas:
            cuenta.actualizar_saldo()
