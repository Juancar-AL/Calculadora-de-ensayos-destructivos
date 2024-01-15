# Establece la clase que se va a inicializar
class Charpy():
    def __init__(self) -> None:
        self._height1 = None
        self._height2 = None
        self._energyp1 = None
        self._energyp2 = None
        self._area = None
        self._result = None
        self._alpha = None
        self._beta = None
        self._long = None

    @property
    def height1(self):
        return self._height1

    @height1.setter
    def height1(self, n_height1):
        self._height1 = n_height1

    @property
    def height2(self):
        return self._height2

    @height2.setter
    def height2(self, n_heigh2):
        self._height2 = n_heigh2

    @property
    def energyp1(self):
        return self._energyp1

    @energyp1.setter
    def energyp1(self, n_energy1):
        self._energyp1 = n_energy1

    @property
    def energyp2(self):
        return self._energyp2

    @energyp2.setter
    def energyp2(self, n_energy2):
        self._energyp2 = n_energy2

    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, n_result):
        self._result = n_result

    @property
    def alpha(self):
        return self._alpha

    @alpha.setter
    def alpha(self, n_alpha):
        self._alpha = n_alpha

    @property
    def beta(self):
        return self._beta

    @beta.setter
    def beta(self, n_beta):
        self._beta = n_beta

    @property
    def long(self):
        return self._long

    @long.setter
    def long(self, n_long):
        self.long = n_long

    def __str__(self) -> str:
        return str(self._result, self._height1, self._height2, self._energyp1, self._energyp2, self._energyp2, self._alpha, self._beta, self._long, self._diference)
    
    def height_diference(self):
        
