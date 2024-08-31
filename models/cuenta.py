class Cuenta:
    def __init__(self, id_cuenta, fecha_apertura, monto_apertura, usuario):
        self.id_cuenta = id_cuenta
        self.fecha_apertura = fecha_apertura
        self.saldo = monto_apertura
        self.usuario = usuario
        self.transacciones = []  # Lista de transacciones asociadas

    def consignar(self, monto):
        self.saldo += monto

    def retirar(self, monto):
        if monto <= self.saldo:
            self.saldo -= monto
            return True
        return False

    def agregar_transaccion(self, transaccion):
        self.transacciones.append(transaccion)

    def obtener_transacciones(self):
        return self.transacciones

    def actualizar_saldo(self):
        saldo_inicial = self.saldo
        for transaccion in self.transacciones:
            if transaccion.tipo_transaccion == "Consignación":
                saldo_inicial += transaccion.monto
            elif (
                transaccion.tipo_transaccion == "Retiro"
                and saldo_inicial >= transaccion.monto
            ):
                saldo_inicial -= transaccion.monto
        self.saldo = saldo_inicial

    def mostrar_informacion(self):
        return f"Cuenta ID: {self.id_cuenta}, Fecha de apertura: {self.fecha_apertura}, Saldo: {self.saldo}"


class CuentaAhorros(Cuenta):
    def __init__(self, id_cuenta, fecha_apertura, monto_apertura, usuario):
        super().__init__(id_cuenta, fecha_apertura, monto_apertura, usuario)
        self.tipo_cuenta = "Ahorros"


class CuentaCorriente(Cuenta):
    def __init__(self, id_cuenta, fecha_apertura, monto_apertura, usuario):
        super().__init__(id_cuenta, fecha_apertura, monto_apertura, usuario)
        self.tipo_cuenta = "Corriente"
