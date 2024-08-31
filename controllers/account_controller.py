from models.cuenta import CuentaAhorros, CuentaCorriente
from models.transaccion import (
    TransaccionDeposito,
    TransaccionRetiro,
    TransaccionTransferencia,
)
from datetime import date


class AccountController:
    def __init__(self):
        self.cuentas = {}

    def crear_cuenta(
        self, id_cuenta, tipo_cuenta, fecha_apertura, monto_apertura, usuario
    ):
        if id_cuenta in self.cuentas:
            return "Error: La cuenta ya existe."

        if tipo_cuenta == "Ahorros":
            cuenta = CuentaAhorros(id_cuenta, fecha_apertura, monto_apertura, usuario)
        elif tipo_cuenta == "Corriente":
            cuenta = CuentaCorriente(id_cuenta, fecha_apertura, monto_apertura, usuario)
        else:
            return "Error: Tipo de cuenta no válido."

        self.cuentas[id_cuenta] = cuenta
        usuario.agregar_cuenta(cuenta)
        return "Cuenta creada exitosamente."

    def obtener_cuenta(self, id_cuenta):
        return self.cuentas.get(id_cuenta, None)

    def realizar_transaccion(self, id_cuenta_origen, id_cuenta_destino=None, monto=0):
        cuenta_origen = self.obtener_cuenta(id_cuenta_origen)

        if not cuenta_origen:
            return "Error: La cuenta origen no existe."

        if id_cuenta_destino:
            cuenta_destino = self.obtener_cuenta(id_cuenta_destino)
            if not cuenta_destino:
                return "Error: La cuenta destino no existe."

            if cuenta_origen.retirar(monto):
                cuenta_destino.consignar(monto)
                transaccion = TransaccionTransferencia(
                    f"T-{len(cuenta_origen.transacciones)+1}",
                    monto,
                    date.today(),
                    cuenta_origen,
                    cuenta_destino,
                )
                cuenta_origen.agregar_transaccion(transaccion)
                cuenta_destino.agregar_transaccion(transaccion)
                return "Transferencia realizada con éxito."
            else:
                return "Error: Fondos insuficientes."
        else:
            if monto > 0:
                transaccion = TransaccionDeposito(
                    f"T-{len(cuenta_origen.transacciones)+1}",
                    monto,
                    date.today(),
                    cuenta_origen,
                )
                cuenta_origen.consignar(monto)
                cuenta_origen.agregar_transaccion(transaccion)
                return "Depósito realizado con éxito."
            else:
                if cuenta_origen.retirar(monto):
                    transaccion = TransaccionRetiro(
                        f"T-{len(cuenta_origen.transacciones)+1}",
                        monto,
                        date.today(),
                        cuenta_origen,
                    )
                    cuenta_origen.agregar_transaccion(transaccion)
                    return "Retiro realizado con éxito."
                else:
                    return "Error: Fondos insuficientes."

    def revisar_transacciones(self, id_cuenta):
        cuenta = self.obtener_cuenta(id_cuenta)
        if cuenta:
            return cuenta.obtener_transacciones()
        return None
