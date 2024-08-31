class Transaccion:
    def __init__(self, id_transaccion, monto, fecha, cuenta_origen):
        self.id_transaccion = id_transaccion
        self.monto = monto
        self.fecha = fecha
        self.cuenta_origen = cuenta_origen

    def mostrar_informacion(self):
        return f"Transacción ID: {self.id_transaccion}, Monto: {self.monto}, Fecha: {self.fecha}"


class TransaccionDeposito(Transaccion):
    def __init__(self, id_transaccion, monto, fecha, cuenta_origen):
        super().__init__(id_transaccion, monto, fecha, cuenta_origen)
        self.tipo_transaccion = "Consignación"


class TransaccionRetiro(Transaccion):
    def __init__(self, id_transaccion, monto, fecha, cuenta_origen):
        super().__init__(id_transaccion, monto, fecha, cuenta_origen)
        self.tipo_transaccion = "Retiro"


class TransaccionTransferencia(Transaccion):
    def __init__(self, id_transaccion, monto, fecha, cuenta_origen, cuenta_destino):
        super().__init__(id_transaccion, monto, fecha, cuenta_origen)
        self.cuenta_destino = cuenta_destino
        self.tipo_transaccion = "Transferencia"

    def mostrar_informacion(self):
        return f"Transacción ID: {self.id_transaccion}, Monto: {self.monto}, Fecha: {self.fecha}, De: {self.cuenta_origen.id_cuenta} a: {self.cuenta_destino.id_cuenta}"
