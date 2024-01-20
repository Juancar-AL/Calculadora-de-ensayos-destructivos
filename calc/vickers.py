import math

# Establece las instancias de una clase para así pdoer trabajar con todas ellas mientras están asignadas a un mismo ensayo


class Vickers():
    def __init__(self):
        self.resultado = None
        self.diametro = None
        self.fuerza = None

    def __str__(self) -> str:
        return str((self.resultado, self.fuerza, self.diametro))

# Calcular el resultadoado del ensayo utilizando la fórmula HV = F/D^2


def vickers_resultado(self):
    try:
        self.resultado = round(k*(self.fuerza/self.diametro**2), 3)
        return self.resultado
    except:
        pass
# Calcular la fuerza utilizada en el ensayo mediante la fórmula principal HV = F/D^2


def vickers_fuerza(self):
    try:
        self.fuerza = round((self.resultado/k)*self.diametro**2, 3)
        return self.fuerza
    except:
        pass


def vickers_diametro(self):
    try:
        self.diametro = round(
            math.sqrt(self.resultado/(self.fuerza*k)), 3)
        return self.diametro
    except:
        pass
# Establecer los valores para las instancias de la clase, ninguno de ellos es obligarotio


def vickers_valores(self, **kwargs):
    for key, value in kwargs.items():
        if value is not None:
            if key == 'diametro2' and kwargs['diametro2'] is not None:
                # Si se dan dos valores para el diámetro, se calcula la media
                self.diametro = (kwargs['diametro1'] + kwargs['diametro2']) / 2
            elif key == 'diametro1':
                # Si solo se da un valor para el diámetro, se asigna directamente
                self.diametro = kwargs['diametro1']
            else:
                setattr(self, key, value)


# Extraer todos los datos faltantes del ensayo


def vickers_ensayo(self):
    for i in range(3):
        vickers_diametro(self)
        vickers_fuerza(self)
        vickers_resultado(self)


k = 1.8544
# Variables necesarias para el correcto funcionamiento del problema
if __name__ == "__main__":
    vickers_instance = Vickers()
    vickers_valores(vickers_instance, diametro1=0.45, fuerza=50)
    vickers_ensayo(vickers_instance)
    print(vickers_instance)


# Por Juan Carlos Alonso
