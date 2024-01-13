#Establece las instancias de una clase para así pdoer trabajar con todas ellas mientras están asignadas a un mismo ensayo
class Rockwell():
    def __init__(self) -> None:
        self._h2 = None
        self._h3 = None
        self._e = None
        self._result = None

    @property
    def h2(self):
        return self._h2
    
    @h2.setter
    def h2(self, n_h2):
        self._h2 = n_h2
    
    @property
    def h3(self):
        return self._h3
    
    @h3.setter
    def h3(self, n_h3):
        self._h3 = n_h3

    @property
    def e(self):
        return self._e
    
    @e.setter
    def e(self, n_e):
        self._e = n_e

    @property
    def result(self):
        return self._result
    
    @result.setter
    def result(self, n_result):
        self._result = n_result

    def result_b(self):
        self.result = 130 - self.e
    def result_c(self):
        self.result = 100 - self.e
    
