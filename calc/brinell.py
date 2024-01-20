import math

# Establece las instancias de una clase para así pdoer trabajar con todas ellas mientras están asignadas a un mismo ensayo


class Brinell():
    def __init__(self) -> None:  # Estas variables serán establecidas al momento de crear un objeto con esta clase, a todas se les asignará None ya que posteriormente se les asignarán unos valores
        self.diametro = None
        self.fuerza = None
        self.huella_diametro = None
        self.resultado = None
        self.constante = None
        self.fiabilidad = None

    def __str__(self) -> str:
        return str((self.resultado, self.diametro, self.huella_diametro, self.fuerza, self.constante, self.fiabilidad))

# Calcular el resultadoado del ensayo mediante la fórmula principal


def resultado(self):
    try:
        self.resultado = round(self.fuerza/(((math.pi*self.diametro)/2)*(self.diametro -
                                                                         math.sqrt(self.diametro**2-self.huella_diametro**2))), 3)
        return self.resultado
    except:
        pass
# Calcular el diámetro del indentadordor utilizando la fórmula principal


def brinell_huella_d(self):
    # Calcular la superficie mediante la fórmula principal HB = F/S
    try:
        surface = self.fuerza / self.resultado
        self.huella_diametro = round(math.sqrt(self.diametro**2-((self.diametro-(2*surface) /
                                                                  (math.pi*self.diametro))**2)), 3)
        return self.huella_diametro
    except:
        pass

# Calcular el diámetro dejado por el ensayo utilizando la constante y la fuerza utilizada F = K * D^2


def brinell_diametro(self):
    try:
        self.diametro = round(
            math.sqrt(self.fuerza/self.constante), 3)
        return self.diametro
    except:
        pass
# Calcular la fuerza utilizando la fórmula principal del ensayo HB = F/S


def brinell_fuerza(self):
    try:
        if constante == None:
            self.fuerza = round(((math.pi*self.diametro)/2)*(self.diametro -
                                                             math.sqrt(self.diametro**2-self.huella_diametro**2))*self.resultado, 3)
            return self.fuerza
        self.fuerza = round(self.constante * self.diametro**2, 2)
        return self.fuerza
    except:
        pass
# Comprobar si los resultadoados dados por el ensayo son fiables o no utilizando los diámetros D/4 < d < D/2


def fiabilidad_brinell_d(self):
    try:
        self.fiabilidad = (self.diametro/4 <
                           self.huella_diametro < self.diametro/2)
        return self.fiabilidad
    except:
        pass

# Calcular la constante del ensayo


def constante(self):
    try:
        self.constante = round(self.fuerza / self.diametro**2, 3)
        return self.constante
    except:
        pass

# Establecer los valores para las instancias de la brinell, ninguno de ellos es obligarotio


def brinell_valores(self, **kwargs):
    for key, value in kwargs.items():
        setattr(self, key, value)

# Extraer todos los datos faltantes del ensayo


def brinell_ensayo(self):
    for i in range(6):
        brinell_diametro(self)
        brinell_fuerza(self)
        brinell_huella_d(self)
        fiabilidad_brinell_d(self)
        resultado(self)
        constante(self)


if __name__ == "__main__":
    print("Por Juan Carlos Alonso")


# Por Juan Carlos Alonso
