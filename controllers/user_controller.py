from models.usuario import Usuario


class UserController:
    def __init__(self):
        self.usuarios = []

    def registrar_usuario(self, identificacion, nombres, edad):
        usuario = Usuario(identificacion, nombres, edad)
        self.usuarios.append(usuario)
        return "Usuario registrado exitosamente."

    def obtener_usuarios(self):
        return self.usuarios
