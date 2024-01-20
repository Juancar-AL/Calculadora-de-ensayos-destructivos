import math
import numpy

# Establece la clase que se va a inicializar


class Charpy():
    def __init__(self) -> None:
        self.altura_inicial = None
        self.altura_final = None
        self.longitud = None

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
        return str(self.resultado, self.altura_inicial, self.altura_final, self.energia_potencial1, self.energia_potencial2, self.var_energia_potencial, self.lado, self.entalla, self.area, self.masa)

    """Resultado {self.resultado}\nAltura inicial {self.altura_inicial}\nAltura final {self.altura_final}\n 
Energía potencial 1 {self.energia_potencial1}\nEnergía potencial 2 {self.energia_potencial2}\nVariación energía potencial  {self.var_energia_potencial}\n
Lado {self.lado}\nEntalla {self.entalla}\nArea {self.area}\nMasa {self.masa}\n """


def c_altura_inicial(self):
    try:
        if self.longitud != None and self.angulo_alpha != None:
            self.altura_inicial = round(
                self.longitud - (math.cos(self.angulo_alpha) * self.longitud), 3)
            return self.altura_inicial
        self.altura_inicial = round(self.altura_final -
                                    ((self.resultado*self.area)/(self.masa * 9.81)), 3)
        return self.altura_inicial
    except TypeError:
        pass


def c_altura_final(self):
    try:
        self.altura_final = round(
            self.longitud - (math.cos(self.angulo_beta) * self.longitud), 3)
        return self.altura_final
    except TypeError:
        pass


def c_energia_potencial_1(self):
    try:
        self.energia_potencial1 = round(
            self.masa * 9.81 * self.altura_inicial, 3)
        return self.energia_potencial1
    except TypeError:
        pass


def c_energia_potencial_2(self):
    try:
        self.energia_potencial2 = round(
            self.masa * 9.81 * self.altura_final, 3)
        return self.energia_potencial2
    except TypeError:
        pass


def c_var_entergia_potencial(self):
    try:
        self.var_energia_potencial = round(
            self.energia_potencial1 - self.energia_potencial2, 3)
        return self.var_energia_potencial
    except TypeError:
        try:
            self.var_energia_potencial = round(
                self.masa * 9.81 * (self.altura_inicial-self.altura_final), 3)
        except TypeError:
            pass
    finally:
        return self.var_energia_potencial


def c_resultado(self):
    try:
        self.resultado = round(self.var_energia_potencial/self.area, 4)
        return self.resultado
    except TypeError:
        pass


def c_area(self):
    try:
        self.area = self.lado * (self.lado - self.entalla)
        return self.area
    except TypeError:
        try:
            self.area = round(self.var_energia_potencial / self.resultado, 3)
            return self.area
        except TypeError:
            pass


def charpy_valores(self, **kwargs):
    for key, value in kwargs.items():
        if value is not None:
            setattr(self, key, value)


def charpy_ensayo(self):
    for i in range(100):
        c_altura_inicial(self)
        c_altura_final(self)
        c_energia_potencial_1(self)
        c_energia_potencial_2(self)
        c_var_entergia_potencial(self)
        c_area(self)
        c_resultado(self)


if __name__ == "__main__":
    print("Por Juan Carlos Alonso")
