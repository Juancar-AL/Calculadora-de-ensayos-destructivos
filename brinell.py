import math

#Establish a class in order to store all the variables and establish them all at the same time.
class Brinell():
    def __init__(self) -> None:
        self._diameter = None
        self._force = None
        self._indentation_diameter = None
        self._result = None
        self._hardness_constant = None
        self._fiability = None

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

    @property
    def indentation_diameter(self):
        return self._indentation_diameter

    @indentation_diameter.setter
    def indentation_diameter(self, n_indentation_diameter):
        self._indentation_diameter = n_indentation_diameter

    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, n_result):
        self._result = n_result

    @property
    def hardness_constant(self):
        return self._hardness_constant

    @hardness_constant.setter
    def hardness_constant(self, n_hardness_constant):
        self._hardness_constant = n_hardness_constant

    @property
    def fiability(self):
        return self._fiability
    
    @fiability.setter
    def fiability(self, n_fiability):
        self._fiability = n_fiability

    def __str__(self) -> str:
        return str((self._result, self._diameter,self._indentation_diameter,self._force, self._hardness_constant, self._fiability))


brinell_instance = Brinell()

# Calculate the result of the test
def result(brinell_instance):
    brinell_instance.result = round(brinell_instance.force/(((math.pi*brinell_instance.diameter)/2)*(brinell_instance.diameter-math.sqrt(brinell_instance.diameter**2-brinell_instance.indentation_diameter**2))), 3)
    return brinell_instance.result

# Calculate the diameter of the identator
def brinell_indentation_d(brinell_instance):
    surface = brinell_instance.force / brinell_instance.result
    brinell_instance.indentation_diameter = round(math.sqrt(brinell_instance.diameter**2-((brinell_instance.diameter-(2*surface)/(math.pi*brinell_instance.diameter))**2)), 3 )
    return brinell_instance.indentation_diameter

# Calculate the force by using the constant
def brinell_force_1(brinell_instance):
    brinell_instance.force = round(brinell_instance.hardness_constant * brinell_instance.diameter**2, 2)
    return brinell_instance.force

# Calculate the diameter by using the constant
def brinell_diameter(brinell_instance):
    brinell_instance.diameter = round(math.sqrt(brinell_instance.force/brinell_instance.hardness_constant), 3)
    return brinell_instance.diameter

#Calculate the force by using the main formula
def brinell_force_2(brinell_instance):
    brinell_instance.force = round(((math.pi*brinell_instance.diameter)/2)*(brinell_instance.diameter-math.sqrt(brinell_instance.diameter**2-brinell_instance.indentation_diameter**2))*brinell_instance.result, 3)
    return brinell_instance.force

#Check if the test results are reliable or not by using the diameter and the identator diameter
def f_brinell_d(brinell_instance):
    brinell_instance.fiability = (brinell_instance.diameter/4 < brinell_instance.indentation_diameter < brinell_instance.diameter/2)
    return brinell_instance.fiability

#Check if the test results are reliable or not by using the constant
def f_brinell_k(brinell_instance):
        brinell_instance.fiability = ((brinell_instance.hardness_constant * brinell_instance.diameter**2) == brinell_instance.force)
        return brinell_instance.fiability

#Calculate the constant of the test
def hardness_constant(brinell_instance):
        brinell_instance.hardness_constant = round(brinell_instance.force / brinell_instance.diameter**2, 3)
        return brinell_instance.hardness_constant

#Establish the attributes of the test 
def valores(brinell_instance, force = None, diameter = None, indentation_diameter = None, result = None, hardness_constant = None):
    brinell_instance.force = force
    brinell_instance.diameter = diameter
    brinell_instance.indentation_diameter = indentation_diameter
    brinell_instance.result = result
    brinell_instance.hardness_constant = hardness_constant


#Check what functions needs to be used in order to complete the test
def ensayo(brinell_instance):
    if brinell_instance.result == None and brinell_instance.force == None and brinell_instance.diameter == None and brinell_instance.indentation_diameter == None and brinell_instance.hardness_constant == None and brinell_instance.fiability == None:
        pass
    else:
        while brinell_instance.result == None or brinell_instance.force == None or brinell_instance.diameter == None or brinell_instance.indentation_diameter == None or brinell_instance.hardness_constant == None or brinell_instance.fiability == None:
            if brinell_instance.result == None and brinell_instance.force != None and brinell_instance.diameter != None and brinell_instance.indentation_diameter != None: 
                result(brinell_instance)
            elif brinell_instance.result != None and brinell_instance.force != None and brinell_instance.diameter == None and brinell_instance.indentation_diameter != None:
                brinell_diameter(brinell_instance)
            elif brinell_instance.result != None and brinell_instance.force != None and brinell_instance.diameter != None and brinell_instance.indentation_diameter == None:
                brinell_indentation_d(brinell_instance)
            elif brinell_instance.force == None and brinell_instance.hardness_constant != None:
                brinell_force_1(brinell_instance)
            elif brinell_instance.force == None and brinell_instance.hardness_constant == None:
                brinell_force_2(brinell_instance)
            # elif brinell_instance.fiability == None and brinell_instance.diameter != None and brinell_instance.hardness_constant != None and brinell_instance.force != None:
            #     f_brinell_k(brinell_instance)
            elif brinell_instance.fiability == None and brinell_instance.diameter != None and brinell_instance.indentation_diameter != None:
                f_brinell_d(brinell_instance)
            elif brinell_instance.hardness_constant == None and brinell_instance.diameter != None and brinell_instance.force != None:
                hardness_constant(brinell_instance)
        return brinell_instance

