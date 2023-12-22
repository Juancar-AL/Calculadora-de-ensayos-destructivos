#Establece las instancias de una clase para así pdoer trabajar con todas ellas mientras están asignadas a un mismo ensayo
class Rockwell():
    def __init__(self) -> None:
        self._h2 = None
        self._h3 = None
        self._e = None

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