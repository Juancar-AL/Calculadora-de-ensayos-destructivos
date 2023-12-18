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

#Variables necesarias para el correcto funcionamiento del problema    
vickers_instance = Vickers()
k = 1.8544

#Calcular el resultado del ensayo utilizando la fórmula HV = F/D^2
def result(vickers_instance):
    vickers_instance.result = round(k*(vickers_instance.force/vickers_instance.diameter**2),3 )
    return vickers_instance.result

#Calcular la fuerza utilizada en el ensayo mediante la fórmula principal HV = F/D^2
def vickers_force(vickers_instance):
    vickers_instance.force = round((vickers_instance.result/k)*vickers_instance.diameter**2, 3)
    return vickers_instance.force

#Calcular el diámetro del indentador mediante la fórmula principal HV = F/D^2
def vickers_diameter(vickers_instance):
    vickers_instance.diameter = round(math.sqrt(vickers_instance.result/(vickers_instance.force*k)), 3)
    return vickers_instance.diameter

#Establecer los valores para las instancias de la clase, ninguno de ellos es obligarotio
def valores(vickers_instance, force = None, diameter1 = None, diameter2 = None, result = None):
    vickers_instance.force = force
    vickers_instance.diameter = diameter1 if diameter2 == None else (diameter1+diameter2)/2 #Si se dan dos valores para el diámetro se calcula la media de estos
    vickers_instance.result = result

#Extraer todos los datos faltantes del ensayo
def ensayo(vickers_instance):
    if vickers_instance.force == None and vickers_instance.diameter == None and vickers_instance.result == None: #Comprobar que no todos los valores son None
        pass
    else:
        while vickers_instance.force == None or vickers_instance.diameter == None or vickers_instance.result == None: #Bucle que se ejecuta si cualquiera de las instancias de la clase son None, en caso de hacerlo se ejecuta hasta que todas tengan un valor
            if vickers_instance.result == None:
                result(vickers_instance)
            if vickers_instance.force == None:
                vickers_force(vickers_instance)
            if vickers_instance.diameter == None:
                vickers_diameter(vickers_instance)
        return vickers_instance
    
#Por Juan Carlos Alonso
