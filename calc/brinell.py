import math

# Establece las instancias de una clase para así pdoer trabajar con todas ellas mientras están asignadas a un mismo ensayo


class Brinell():
    def __init__(self) -> None:  # Estas variables serán establecidas al momento de crear un objeto con esta clase, a todas se les asignará None ya que posteriormente se les asignarán unos valores
        self.diameter = None
        self.force = None
        self.indentation_diameter = None
        self.result = None
        self.hardness_constant = None
        self.fiabilidad = None

    def __str__(self) -> str:
        return str((self.result, self.diameter, self.indentation_diameter, self.force, self.hardness_constant, self.fiabilidad))

# Calcular el resultado del ensayo mediante la fórmula principal


def result(self):
    self.result = round(self.force/(((math.pi*self.diameter)/2)*(self.diameter -
                                                                 math.sqrt(self.diameter**2-self.indentation_diameter**2))), 3)
    return self.result

# Calcular el diámetro del indentadordor utilizando la fórmula principal


def brinell_indentation_d(self):
    # Calcular la superficie mediante la fórmula principal HB = F/S
    surface = self.force / self.result
    self.indentation_diameter = round(math.sqrt(self.diameter**2-((self.diameter-(2*surface) /
                                                                   (math.pi*self.diameter))**2)), 3)
    return self.indentation_diameter

# Calcular la fuerza utilizando la constante y el diámetro del indentador F = K * D^2


def brinell_force_1(self):
    self.force = round(self.hardness_constant * self.diameter**2, 2)
    return self.force

# Calcular el diámetro dejado por el ensayo utilizando la constante y la fuerza utilizada F = K * D^2


def brinell_diameter(self):
    self.diameter = round(
        math.sqrt(self.force/self.hardness_constant), 3)
    return self.diameter

# Calcular la fuerza utilizando la fórmula principal del ensayo HB = F/S


def brinell_force_2(self):
    self.force = round(((math.pi*self.diameter)/2)*(self.diameter -
                                                    math.sqrt(self.diameter**2-self.indentation_diameter**2))*self.result, 3)
    return self.force

# Comprobar si los resultados dados por el ensayo son fiables o no utilizando los diámetros D/4 < d < D/2


def f_brinell_d(self):
    self.fiabilidad = (self.diameter/4 <
                       self.indentation_diameter < self.diameter/2)
    return self.fiabilidad

# Calcular la constante del ensayo


def hardness_constant(self):
    self.hardness_constant = round(self.force / self.diameter**2, 3)
    return self.hardness_constant

# Establecer los valores para las instancias de la brinell, ninguno de ellos es obligarotio


def brinell_valores(self, **kwargs):
    for key, value in kwargs.items():
        setattr(self, key, value)

# Extraer todos los datos faltantes del ensayo


def brinell_ensayo(self):
    # Comprobar si se han rellenado más de 2 variables, en caso de que si se ejecuta el código
    if sum(1 for var in [self.result, self.force, self.diameter, self.indentation_diameter, self.hardness_constant, self.fiabilidad]if var is not None) >= 2:
        # Bucle que se ejecuta si cualquiera de las instancias de la brinell son None, en caso de hacerlo se ejecuta hasta que todas tengan un valor
        while self.result == None or self.force == None or self.diameter == None or self.indentation_diameter == None or self.hardness_constant == None or self.fiabilidad == None:
            if self.result == None and self.force != None and self.diameter != None and self.indentation_diameter != None:
                result(self)
            elif self.result != None and self.force != None and self.diameter == None and self.indentation_diameter != None:
                brinell_diameter(self)
            elif self.result != None and self.force != None and self.diameter != None and self.indentation_diameter == None:
                brinell_indentation_d(self)
            elif self.force == None and self.hardness_constant != None:
                brinell_force_1(self)
            elif self.force == None and self.hardness_constant == None:
                brinell_force_2(self)
            elif self.fiabilidad == None and self.diameter != None and self.indentation_diameter != None:
                f_brinell_d(self)
            elif self.hardness_constant == None and self.diameter != None and self.force != None:
                hardness_constant(self)
        return self
    else:
        raise Exception("Valores insuficientes para el cálculo")


if __name__ == "__main__":
    brinell_instance = Brinell()
    brinell_valores(brinell_instance, force=3000,
                    diameter=3, indentation_diameter=2)
    brinell_ensayo(brinell_instance)
    print(brinell_instance)


# Por Juan Carlos Alonso
