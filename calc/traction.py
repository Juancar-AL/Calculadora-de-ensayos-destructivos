import math

class Traction():
    def __init__(self) -> None:
        self._elong = None
        self._long1 = None
        self._area = None
        self._long2 = None
        self._force = None
        self._tens = None
        self._const = None

    @property
    def elong(self):
        return self._elong
    
    @elong.setter
    def elong(self, n_elong):
        self._elong = n_elong
    
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
    def area(self):
        return self._area
    
    @area.setter
    def area(self, n_area):
        self._area = n_area

    @property
    def force(self):
        return self._force
    
    @force.setter
    def force(self, n_force):
        self._force = n_force

    @property
    def tens(self):
        return self._tens
    
    @tens.setter
    def tens(self, n_tens):
        self._tens = n_tens

    @property
    def const(self):
        return self._const
    
    @const.setter
    def const(self, n_const):
        self._const = n_const

    def __str__(self) -> str:
        return str((self.tens, self._long1,self._long2, self._elong, self._force, self._area, self.const))
    
def trac_tens(self):
    self.tens = self.force / self.area
    return self.tens
def trac_force(self):
    self.force = self.tens * self.area
    return self.force
def trac_area(self):
    self.area = self.tens * self.tens
    return self.area
def trac_elong(self):
    self.elong = (self.long2-self.long1)/self.long1
    return self.elong
def hooke_tens(self):
    self.tens = self.const*self.elong
    return self.tens
def hooke_const(self):
    self.const = self.tens / self.elong
    return self.const
def hooke_elong(self):
    self.elong = self.tens/self.const
    return self.elong

def trac_valores(self, tension = None, force = None, elong = None, area = None, long1 = None, long2 = None, const = None):
    self.tens = tension
    self.force = force
    self.elong = elong
    self.area = area
    self.long1 = long1
    self.long2 = long2
    self.const = const
def trac_ensayo(self, proportional = False, tens = False, elong = False, const = False, area = False, force = False):
    if self.tens ==None and self.force ==None  and self.elong ==None and self.area ==None and self.long1 ==None and self.long2 ==None and self.const == None:
        pass
    else:
        if proportional:
            if self.tens == None and self.elong != None and self.const != None and tens:
                hooke_tens()
            if self.tens != None and self.elong == None and self.const != None and elong:
                hooke_elong()
            if self.tens != None and self.elong != None and self.const == None and const:
                hooke_const()
        else:
            if self.tens == None and self.force != None and self.area != None and tens:
                trac_tens()
            elif self.tens != None and self.force != None and self.area == None and area:
                trac_tens()
            elif self.tens != None and self.force == None and self.area != None and force:
                trac_force()
            elif self.elong == None and self.long1 != None and self.long2 != None and elong:
                trac_elong()
        return self

if __name__ == "__main__":    
    traction_instance = Traction()
    trac_valores(traction_instance, area= 80, elong=35, const=192.3)
    #traction_instance.trac_ensayo(force=  True, proportional=True)
    print(traction_instance)

#Por Juan Carlos Alonso Luengo
