import math

# Establece las instancias de una clase para así pdoer trabajar con todas ellas mientras están asignadas a un mismo ensayo


class Brinell():
    def __init__(self) -> None:  # Estas variables serán establecidas al momento de crear un objeto con esta clase, a todas se les asignará None ya que posteriormente se les asignarán unos valores
        self._diameter = None
        self._force = None
        self._indentation_diameter = None
        self._result = None
        self._hardness_constant = None
        self._fiability = None

    # Funciones que serán las encargadas de asignar los valores posteriormente a las instancias
    @property
    def diameter(self):
        return self._diameter

    @diameter.setter
    def diameter(self, n_diameter):
        self._diameter = n_diameter

    @property
    def force(self):
        return self._force

    @force.setter
    def force(self, n_force):
        self._force = n_force

    @property
    def indentation_diameter(self):
        return self._indentation_diameter

    @indentation_diameter.setter
    def indentation_diameter(self, n_indentation_diameter):
        self._indentation_diameter = n_indentation_diameter

    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, n_result):
        self._result = n_result

    @property
    def hardness_constant(self):
        return self._hardness_constant

    @hardness_constant.setter
    def hardness_constant(self, n_hardness_constant):
        self._hardness_constant = n_hardness_constant

    @property
    def fiability(self):
        return self._fiability

    @fiability.setter
    def fiability(self, n_fiability):
        self._fiability = n_fiability

    def __str__(self) -> str:
        return str((self._result, self._diameter, self._indentation_diameter, self._force, self._hardness_constant, self._fiability))

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
    self.diameter = round(math.sqrt(self.force/self.hardness_constant), 3)
    return self.diameter

# Calcular la fuerza utilizando la fórmula principal del ensayo HB = F/S


def brinell_force_2(self):
    self.force = round(((math.pi*self.diameter)/2)*(self.diameter -
                       math.sqrt(self.diameter**2-self.indentation_diameter**2))*self.result, 3)
    return self.force

# Comprobar si los resultados dados por el ensayo son fiables o no utilizando los diámetros D/4 < d < D/2


def f_brinell_d(self):
    self.fiability = (self.diameter/4 <
                      self.indentation_diameter < self.diameter/2)
    return self.fiability

# Calcular la constante del ensayo


def hardness_constant(self):
    self.hardness_constant = round(self.force / self.diameter**2, 3)
    return self.hardness_constant

# Establecer los valores para las instancias de la clase, ninguno de ellos es obligarotio


def brinell_valores(self, force=None, diameter=None, indentation_diameter=None, result=None, hardness_constant=None):
    self.force = force
    self.diameter = diameter
    self.indentation_diameter = indentation_diameter
    self.result = result
    self.hardness_constant = hardness_constant

# Extraer todos los datos faltantes del ensayo


def brinell_ensayo(self):
    # Comprobar si se han rellenado más de 2 variables, en caso de que si se ejecuta el código
    if sum(1 for var in [self.result, self.force, self.diameter, self.indentation_diameter, self.hardness_constant, self.fiability]if var is not None) >= 2:
        # Bucle que se ejecuta si cualquiera de las instancias de la clase son None, en caso de hacerlo se ejecuta hasta que todas tengan un valor
        while self.result == None or self.force == None or self.diameter == None or self.indentation_diameter == None or self.hardness_constant == None or self.fiability == None:
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
            elif self.fiability == None and self.diameter != None and self.indentation_diameter != None:
                f_brinell_d(self)
            elif self.hardness_constant == None and self.diameter != None and self.force != None:
                hardness_constant(self)
        return self
    else:
        raise Exception("Valores insuficientes para el cálculo")


if __name__ == "__main__":
    brinell_instance = Brinell()


# Por Juan Carlos Alonso
