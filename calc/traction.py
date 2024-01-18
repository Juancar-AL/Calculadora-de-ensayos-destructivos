import math


class Traction():
    def __init__(self) -> None:
        self.deformacion_unitaria = None
        self.longitud_inicial = None
        self.area = None
        self.longitud_final = None
        self.fuerza = None
        self.tension = None
        self.modulo_young = None

    def __str__(self) -> str:
        return str((self.tension, self.longitud_inicial, self.longitud_final, self.deformacion_unitaria, self.fuerza, self.area, self.modulo_young))


def trac_tension(self):
    self.tension = round(self.fuerza / self.area, 3)
    return self.tension


def trac_fuerza(self):
    self.fuerza = round(self.tension * self.area, 3)
    return self.fuerza


def trac_area(self):
    self.area = round(self.tension * self.tension, 3)
    return self.area


def trac_deformacion_unitaria(self):
    self.deformacion_unitaria = round(
        (self.longitud_final-self.longitud_inicial)/self.longitud_inicial, 3)
    return self.deformacion_unitaria


def hooke_tension(self):
    self.tension = round(self.modulo_young*self.deformacion_unitaria, 3)
    return self.tension


def hooke_modulo_young(self):
    self.modulo_young = round(self.tension / self.deformacion_unitaria, 3)
    return self.modulo_young


def hooke_deformacion_unitaria(self):
    self.deformacion_unitaria = round(self.tension/self.modulo_young, 3)
    return self.deformacion_unitaria


def trac_valores(self, **kwargs):
    for key, value in kwargs.items():
        setattr(self, key, value)


def trac_ensayo(self, proportional=False, tension=False, deformacion_unitaria=False, modulo_young=False, area=False, fuerza=False):
    if self.tension == None and self.fuerza == None and self.deformacion_unitaria == None and self.area == None and self.longitud_inicial == None and self.longitud_final == None and self.modulo_young == None:
        pass
    else:
        if proportional:
            if self.tension == None and self.deformacion_unitaria != None and self.modulo_young != None and tension:
                hooke_tension(self)
                return self.tension
            if self.tension != None and self.deformacion_unitaria == None and self.modulo_young != None and deformacion_unitaria:
                hooke_deformacion_unitaria(self)
                return self.deformacion_unitaria
            if self.tension != None and self.deformacion_unitaria != None and self.modulo_young == None and modulo_young:
                hooke_modulo_young(self)
                return self.modulo_young
        else:
            if self.tension == None and self.fuerza != None and self.area != None and tension:
                trac_tension(self)
                return self.tension
            elif self.tension != None and self.fuerza != None and self.area == None and area:
                trac_area(self)
                return self.area
            elif self.tension != None and self.fuerza == None and self.area != None and fuerza:
                trac_fuerza(self)
                return self.fuerza
            elif self.deformacion_unitaria == None and self.longitud_inicial != None and self.longitud_final != None and deformacion_unitaria:
                trac_deformacion_unitaria(self)
                return self.deformacion_unitaria


if __name__ == "__main__":
    traction_instance = Traction()

#Por Juan Carlos Alonso Luengo
