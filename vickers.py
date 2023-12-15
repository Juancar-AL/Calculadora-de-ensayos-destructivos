import math

class Vickers():
    def __init__(self):
        self._result = None
        self._diameter = None
        self._force = None
        

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
    
vickers_instance = Vickers()
k = 1.8544

#Calculate the result of the test
def result(vickers_instance):
    vickers_instance.result = round(k*(vickers_instance.force/vickers_instance.diameter**2),3 )
    return vickers_instance.result

#Calculate the force of the test
def vickers_force(vickers_instance):
    vickers_instance.force = round((vickers_instance.result/k)*vickers_instance.diameter**2, 3)
    return vickers_instance.force


def vickers_diameter(vickers_instance):
    vickers_instance.diameter = round(math.sqrt(vickers_instance.result/(vickers_instance.force*k)), 3)
    return vickers_instance.diameter

def valores(vickers_instance, force = None, diameter1 = None, diameter2 = None, result = None):
    vickers_instance.force = force
    vickers_instance.diameter = (diameter1+diameter2)/2
    vickers_instance.result = result

def ensayo(vickers_instance):
    while vickers_instance.force == None or vickers_instance.diameter == None or vickers_instance.result == None:
        if vickers_instance.result == None:
            result(vickers_instance)
        if vickers_instance.force == None:
            vickers_force(vickers_instance)
        if vickers_instance.diameter == None:
            vickers_diameter(vickers_instance)
    return vickers_instance
    
