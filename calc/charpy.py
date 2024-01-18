import math
import numpy

# Establece la clase que se va a inicializar


class Charpy():
    def __init__(self) -> None:
        self.altura_inicial = None
        self.altura_final = None
        self.longitud = None
        self.var_altura = None

        self.angulo_alpha = None
        self.angulo_beta = None

        self.energia_potencial1 = None
        self.energia_potencial2 = None
        self.var_energia_potencial = None

        self.area = None
        self.resultado = None
        self.masa = None
        self.entalla = None
        self.lado = None

    def __str__(self) -> str:
        return str((self.resultado, self.altura_inicial, self.altura_final, self.longitud, self.var_altura, self.energia_potencial1, self.energia_potencial2, self.var_energia_potencial, self.angulo_alpha, self.angulo_beta, self.area, self.entalla, self.lado, self.masa))


def c_variacion_altura(self):
    self.var_altura = round(self.longitud * (math.cos(
        self.angulo_beta) - math.cos(self.angulo_alpha)), 3)
    return self.var_altura


def c_altura_inicial(self):
    self.altura_inicial = round(
        self.longitud - (math.cos(self.angulo_alpha) * self.longitud), 3)
    return self.altura_inicial


def c_altura_final(self):
    self.altura_final = round(
        self.longitud - (math.cos(self.angulo_beta) * self.longitud), 3)


def c_energia_potencial_1(self):
    self.energia_potencial1 = round(
        self.masa * 9.81 * self.altura_inicial, 3)
    return self.energia_potencial1


def c_energia_potencial_2(self):
    self.energia_potencial2 = round(
        self.masa * 9.81 * self.altura_final, 3)
    return self.energia_potencial2


def c_var_entergia_potencial(self):
    if self.energia_potencial1 and self.energia_potencial2:
        self.var_energia_potencial = round(
            self.energia_potencial1 - self.energia_potencial2, 3)
        return self.var_energia_potencial
    else:
        self.var_energia_potencial = round(
            self.masa * 9.81 * (self.altura_inicial-self.altura_final), 3)
        return self.var_energia_potencial


def c_resultado(self):
    self.resultado = round(self.var_energia_potencial/self.area, 3)
    return self.resultado


def c_area(self):
    self.area = (float(self.lado) *
                      (float(self.lado) - float(self.entalla)))
    return self.area


def charpy_valores(self, **kwargs):
    for key, value in kwargs.items():
        if value is not None:
            setattr(self, key, value)


def charpy_ensayo(self):
    for i in range(0, 1000):
        if (any(instancia is None for instancia in (self.var_altura, self.altura_inicial, self.altura_final, self.energia_potencial1, self.energia_potencial2, self.var_energia_potencial, self.area, self.resultado))):
            if self.resultado == None and self.var_energia_potencial != None and self.area != None:
                c_resultado(self)
            elif self.var_altura == None and self.longitud != None and self.angulo_beta != None and self.angulo_beta != None:
                c_variacion_altura(self)
            elif self.altura_inicial == None and self.longitud != None and self.angulo_alpha != None:
                c_altura_inicial(self)
            elif self.altura_final == None and self.longitud != None and self.angulo_beta != None:
                c_altura_final(self)
            elif self.energia_potencial1 == None and self.masa != None and self.altura_inicial != None:
                c_energia_potencial_1(self)
            elif self.energia_potencial2 == None and self.masa != None and self.altura_final != None:
                c_energia_potencial_2(self)
            elif self.var_energia_potencial == None and ((self.energia_potencial1 != None and self.energia_potencial2 != None) or (self.masa != None and self.altura_inicial != None and self.altura_final != None)):
                c_var_entergia_potencial(self)
            elif self.area == None and self.lado != None and self.entalla != None:
                c_area(self)
    print("Bucle infinito")


charpy_instance = Charpy()
charpy_valores(charpy_instance, altura_final=0.34,
               lado=0.000010, entalla=0.000002, masa=30, altura_inicial=1)
charpy_ensayo(charpy_instance)
