from models.transaccion import Transaccion


class TransactionController:
    def __init__(self):
        self.transacciones = []

    def agregar_transaccion(
        self, tipo_transaccion, monto, fecha, cuenta_origen, cuenta_destino=None
    ):
        id_transaccion = f"T-{len(self.transacciones)+1}"
        transaccion = Transaccion(
            id_transaccion,
            tipo_transaccion,
            monto,
            fecha,
            cuenta_origen,
            cuenta_destino,
        )
        self.transacciones.append(transaccion)
        cuenta_origen.agregar_transaccion(transaccion)
        if cuenta_destino:
            cuenta_destino.agregar_transaccion(transaccion)
        return transaccion

    def obtener_transacciones(self):
        return self.transacciones
