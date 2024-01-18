import math

# Establece las instancias de una clase para así pdoer trabajar con todas ellas mientras están asignadas a un mismo ensayo


class Vickers():
    def __init__(self):
        self.resultado = None
        self.diameter = None
        self.force = None

    def __str__(self) -> str:
        return str((self.resultado, self.force, self.diameter))

# Calcular el resultadoado del ensayo utilizando la fórmula HV = F/D^2

    def vickers_resultado(self):
        self.resultado = round(k*(self.force/self.diameter**2), 3)
        return self.resultado

    # Calcular la fuerza utilizada en el ensayo mediante la fórmula principal HV = F/D^2

    def vickers_force(self):
        self.force = round((self.resultado/k)*self.diameter**2, 3)
        return self.force

    def vickers_diameter(self):
        self.diameter = round(
            math.sqrt(self.resultado/(self.force*k)), 3)
        return self.diameter

# Establecer los valores para las instancias de la clase, ninguno de ellos es obligarotio


def vickers_valores(self, **kwargs):
    for key, value in kwargs.items():
        if value is not None:
            if key == 'diameter2' and kwargs['diameter2'] is not None:
                # Si se dan dos valores para el diámetro, se calcula la media
                self.diameter = (kwargs['diameter1'] + kwargs['diameter2']) / 2
            elif key == 'diameter1':
                self.diameter = self.diameter1
            else:
                setattr(self, key, value)


def vickers_valores(self, **kwargs):
    for key, value in kwargs.items():
        if value is not None:
            if key == 'diameter2' and kwargs.get('diameter2') is not None:
                # Si se dan dos valores para el diámetro, se calcula la media
                self.diameter = (kwargs['diameter1'] + kwargs['diameter2']) / 2
            elif key == 'diameter1':
                # Si solo se da un valor para el diámetro, se asigna directamente
                self.diameter = kwargs['diameter1']
            else:
                setattr(self, key, value)


# Extraer todos los datos faltantes del ensayo


def vickers_ensayo(self):
    # Comprobar que no todos los valores son None
    if self.force != None and self.diameter != None and self.resultado != None:
        # Bucle que se ejecuta si cualquiera de las instancias de la clase son None, en caso de hacerlo se ejecuta hasta que todas tengan un valor
        while self.force == None or self.diameter == None or self.resultado == None:
            if self.resultado == None:
                self.vickers_resultado()
            if self.force == None:
                self.vickers_force()
            if self.diameter == None:
                self.vickers_diameter()
        return self


k = 1.8544
# Variables necesarias para el correcto funcionamiento del problema
if __name__ == "__main__":
    vickers_instance = Vickers()
    vickers_valores(vickers_instance, diameter1=0.45, force=50)
    vickers_ensayo(vickers_instance)
    print(vickers_instance)


#Por Juan Carlos Alonso
