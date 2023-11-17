class Notificador:
    def __init__(self,usuario,mensaje):
        self.usuario=usuario
        self.mensaje=mensaje

    def notificar(self):
        raise NotImplementedError

class NotificadorEmail(Notificador):
    def notificar(self):
        print(f'Enviando mensaje a {self.usuario.email}')

class NotificadorSMS(Notificador):
    def notificar(self):
        print(f'Enviando SMS a {self.usuario.sms}')

class NotificadorWSP(Notificador):
    def notificar(self):
        print(f'Enviando WhatsAoo a {self.usuario.wsp}')


class NotificadorWSP(Notificador):
    def notificar(self):
        print(f'Enviando WhatsAoo a {self.usuario.wsp}')