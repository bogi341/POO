class Car:
    def __init__(self,culoarea,brand,putere,avd,pret):
        self.culoarea=culoarea
        self.brand=brand
        self.putere=putere
        self.avd=avd
        self.pret=pret
        self.presiune_roti=[2.5,2.5,2.5,2.5]

    def __eq__(self, other):
        return self.brand == other.brand and self.putere == other.putere

    def __str__(self):
        return f'Masina {self.brand} de culoarea {self.culoarea} are puterea {self.putere} costa {self.pret}'

    def umfla_cauciucuri(self,presiune):
        for x in range(0,4):
            self.presiune_roti[i]+= presiune

    def desumfla_cauciucuri(self,presiune):
        for i in range (0,4):
            self.presiune_roti[i]-= presiune

    def afisare_presiune(self):
        for x in self.presiune_roti:
            print(x)


c1=Car("rosu","Ferrari",600,True,200000)
print(c1)
c1.umfla_cauciucuri(1)
c1_afisare_presiune()
c1_desumfla_cauciucuri(2)
c1.afisare_presiune()
c2=Car("albastru","Ferrari",610,False,210000)
print(c1==c2)
