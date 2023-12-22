import math

#Establece las instancias de una clase para así pdoer trabajar con todas ellas mientras están asignadas a un mismo ensayo
class Vickers():
    def __init__(self):
        self._result = None
        self._diameter = None
        self._force = None
        
    #Funciones que serán las encargadas de asignar los valores posteriormente a las instancias
    @property
    def result(self):
        return self._result
    @result.setter
    def result(self, n_result):
        self._result = n_result

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

    def __str__(self) -> str:
        return str((self.result, self.force, self.diameter))
    
    #Calcular el resultado del ensayo utilizando la fórmula HV = F/D^2
def result(self):
    self.result = round(k*(self.force/self.diameter**2),3 )
    return self.result

#Calcular la fuerza utilizada en el ensayo mediante la fórmula principal HV = F/D^2
def vickers_force(self):
    self.force = round((self.result/k)*self.diameter**2, 3)
    return self.force

#Calcular el diámetro del indentador mediante la fórmula principal HV = F/D^2
def vickers_diameter(self):
    self.diameter = round(math.sqrt(self.result/(self.force*k)), 3)
    return self.diameter

#Establecer los valores para las instancias de la clase, ninguno de ellos es obligarotio
def valores(self, force = None, diameter1 = None, diameter2 = None, result = None):
    self.force = force
    self.diameter = diameter1 if diameter2 == None else (diameter1+diameter2)/2 #Si se dan dos valores para el diámetro se calcula la media de estos
    self.result = result

#Extraer todos los datos faltantes del ensayo
def ensayo(self):
    if self.force == None and self.diameter == None and self.result == None: #Comprobar que no todos los valores son None
        pass
    else:
        while self.force == None or self.diameter == None or self.result == None: #Bucle que se ejecuta si cualquiera de las instancias de la clase son None, en caso de hacerlo se ejecuta hasta que todas tengan un valor
            if self.result == None:
                result(self)
            if self.force == None:
                vickers_force(self)
            if self.diameter == None:
                vickers_diameter(self)
        return self

#Variables necesarias para el correcto funcionamiento del problema    
if __name__ == "__main__":
    vickers_instance = Vickers()
k = 1.8544


    
#Por Juan Carlos Alonso
