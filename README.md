# Sistema de Ahorro en Python

Este proyecto implementa un sistema de ahorro básico en Python utilizando los principios de la Programación Orientada a Objetos (OOP), con un enfoque en la herencia. 

## Funcionalidades
- **Usuarios**: Los usuarios pueden tener múltiples cuentas bancarias.
- **Cuentas**: Se implementan dos tipos de cuentas, `CuentaAhorros` y `CuentaCorriente`, que heredan de una clase base `Cuenta`.
- **Transacciones**: Las cuentas pueden realizar transacciones como depósitos, retiros, y transferencias. Las transacciones son manejadas por las subclases `TransaccionDeposito`, `TransaccionRetiro`, y `TransaccionTransferencia`, que heredan de una clase base `Transaccion`.

## Arquitectura
- **Herencia**: Se utiliza herencia para especializar las clases `Cuenta` y `Transaccion`, lo que permite una estructura de código más limpia y extensible.
- **Interacción**: Las cuentas asociadas a los usuarios son responsables de realizar las transacciones, siguiendo los principios de encapsulación y responsabilidad única.

## Estudiantes
- **Esteban Villada Henao** - Grupo: 202460-6A - 62
- **Cristian Murillo Soto** - Grupo: 61_2 - 6028_9-6096

Este proyecto es una implementación práctica de conceptos clave de OOP en Python, demostrando cómo la herencia puede ser utilizada para construir aplicaciones modulares y fáciles de mantener.
