import math

#Establece las instancias de una clase para así pdoer trabajar con todas ellas mientras están asignadas a un mismo ensayo
class Brinell():
    def __init__(self) -> None: #Estas variables serán establecidas al momento de crear un objeto con esta clase, a todas se les asignará None ya que posteriormente se les asignarán unos valores
        self._diameter = None
        self._force = None
        self._indentation_diameter = None
        self._result = None
        self._hardness_constant = None
        self._fiability = None
    
    #Funciones que serán las encargadas de asignar los valores posteriormente a las instancias
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
        return str((self._result, self._diameter,self._indentation_diameter,self._force, self._hardness_constant, self._fiability))


brinell_instance = Brinell()

# Calcular el resultado del ensayo mediante la fórmula principal
def result(brinell_instance):
    brinell_instance.result = round(brinell_instance.force/(((math.pi*brinell_instance.diameter)/2)*(brinell_instance.diameter-math.sqrt(brinell_instance.diameter**2-brinell_instance.indentation_diameter**2))), 3)
    return brinell_instance.result

# Calcular el diámetro del indentadordor utilizando la fórmula principal 
def brinell_indentation_d(brinell_instance):
    surface = brinell_instance.force / brinell_instance.result #Calcular la superficie mediante la fórmula principal HB = F/S 
    brinell_instance.indentation_diameter = round(math.sqrt(brinell_instance.diameter**2-((brinell_instance.diameter-(2*surface)/(math.pi*brinell_instance.diameter))**2)), 3 )
    return brinell_instance.indentation_diameter

# Calcular la fuerza utilizando la constante y el diámetro del indentador F = K * D^2
def brinell_force_1(brinell_instance):
    brinell_instance.force = round(brinell_instance.hardness_constant * brinell_instance.diameter**2, 2)
    return brinell_instance.force

# Calcular el diámetro dejado por el ensayo utilizando la constante y la fuerza utilizada F = K * D^2
def brinell_diameter(brinell_instance):
    brinell_instance.diameter = round(math.sqrt(brinell_instance.force/brinell_instance.hardness_constant), 3)
    return brinell_instance.diameter

#Calcular la fuerza utilizando la fórmula principal del ensayo HB = F/S
def brinell_force_2(brinell_instance):
    brinell_instance.force = round(((math.pi*brinell_instance.diameter)/2)*(brinell_instance.diameter-math.sqrt(brinell_instance.diameter**2-brinell_instance.indentation_diameter**2))*brinell_instance.result, 3)
    return brinell_instance.force

#Comprobar si los resultados dados por el ensayo son fiables o no utilizando los diámetros D/4 < d < D/2
def f_brinell_d(brinell_instance):
    brinell_instance.fiability = (brinell_instance.diameter/4 < brinell_instance.indentation_diameter < brinell_instance.diameter/2)
    return brinell_instance.fiability

#Calcular la constante del ensayo
def hardness_constant(brinell_instance):
        brinell_instance.hardness_constant = round(brinell_instance.force / brinell_instance.diameter**2, 3)
        return brinell_instance.hardness_constant

#Establecer los valores para las instancias de la clase, ninguno de ellos es obligarotio
def valores(brinell_instance, force = None, diameter = None, indentation_diameter = None, result = None, hardness_constant = None):
    brinell_instance.force = force
    brinell_instance.diameter = diameter
    brinell_instance.indentation_diameter = indentation_diameter
    brinell_instance.result = result
    brinell_instance.hardness_constant = hardness_constant


#Extraer todos los datos faltantes del ensayo
def ensayo(brinell_instance):
    if sum(1 for var in [brinell_instance.result, brinell_instance.force, brinell_instance.diameter,brinell_instance.indentation_diameter, brinell_instance.hardness_constant, brinell_instance.fiability]if var is not None) >= 2: # Comprobar si se han rellenado más de 2 variables, en caso de que si se ejecuta el código
        while brinell_instance.result == None or brinell_instance.force == None or brinell_instance.diameter == None or brinell_instance.indentation_diameter == None or brinell_instance.hardness_constant == None or brinell_instance.fiability == None: #Bucle que se ejecuta si cualquiera de las instancias de la clase son None, en caso de hacerlo se ejecuta hasta que todas tengan un valor
            if brinell_instance.result == None and brinell_instance.force != None and brinell_instance.diameter != None and brinell_instance.indentation_diameter != None: 
                result(brinell_instance)
            elif brinell_instance.result != None and brinell_instance.force != None and brinell_instance.diameter == None and brinell_instance.indentation_diameter != None:
                brinell_diameter(brinell_instance)
            elif brinell_instance.result != None and brinell_instance.force != None and brinell_instance.diameter != None and brinell_instance.indentation_diameter == None:
                brinell_indentation_d(brinell_instance)
            elif brinell_instance.force == None and brinell_instance.hardness_constant != None:
                brinell_force_1(brinell_instance)
            elif brinell_instance.force == None and brinell_instance.hardness_constant == None:
                brinell_force_2(brinell_instance)
            elif brinell_instance.fiability == None and brinell_instance.diameter != None and brinell_instance.indentation_diameter != None:
                f_brinell_d(brinell_instance)
            elif brinell_instance.hardness_constant == None and brinell_instance.diameter != None and brinell_instance.force != None:
                hardness_constant(brinell_instance)
        return brinell_instance           
    else:
        raise Exception("Se han de dar más de 2 datos del problema")
        

#Por Juan Carlos Alonso
