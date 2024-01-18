class Clase():
    def __init__(self, test1, test2) -> None:
        self.test1 = test1
        self.test2 = test2
        self.test3 = self.test1/self.test2

    def __init__(self, test1):
        self.test1 = test1
        self.test2 = test1
        self.test1 = test1

    def __init__(self, test2):
        self.test1 = test2
        self.test2 = test2*2
        self.test3 = self.test2*3

    def __str__(self) -> str:
        return str(self.test1, self.test2, self.test3)


clase = Clase(test1=2, test2=3)

print(clase)
