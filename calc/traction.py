import math

class Traction():
    def __init__(self) -> None:
        self._result = None
        self._long1 = None
        self._long2 = None
        self._force = None
        self._area = None
        self._tens = None
        self._alar = None

    @property
    def result(self):
        return self._result
    
    @result.setter
    def result(self, n_result):
        self._result = n_result
    
    @property
    def long1(self):
        return self._long1
    
    @long1.setter
    def long1(self, n_long1):
        self._long1 = n_long1

    @property
    def long2(self):
        return self._long2
    
    @long2.setter
    def long2(self, n_long2):
        self._long2 = n_long2

    @property
    def force(self):
        return self._force
    
    @force.setter
    def force(self, n_force):
        self._force = n_force

    @property
    def area(self):
        return self._area
    
    @area.setter
    def area(self, n_area):
        self._area = n_area

    @property
    def tens(self):
        return self._tens
    
    @tens.setter
    def tens(self, n_tens):
        self._tens = n_tens

    @property
    def alar(self):
        return self._alar
    
    @alar.setter
    def alar(self, n_alar):
        self._alar = n_alar

    def __str__(self) -> str:
        return str((self.tens, self._long1,self._long2,self._force, self._area, self._alar))
    
traction_instance = Traction()

def tens(traction_instance):
    traction_instance.tens = traction_instance.force / 