from abc import ABC,abstractmethod

class Dzivnieks(ABC):
    def __init__(self, name, kajas):
        self.name = name
        self.kajas = kajas
    @abstractmethod
    def skanja(self):
        print("random animal noise")
#        return self.skanja
    def __str__(self):
        return f"{self.name} un {self.kajas} kajas"

class Suns(Dzivnieks):
    def __init__(self, name, kajas):
        super().__init__(name, kajas)
        self.name="Komisars "+self.name
    def skanja(self):
        print("vau vau")

class Kakis(Dzivnieks):
    def __init__(self, name, kajas):
        super().__init__(name, kajas)
        self.name="Kaiminu "+self.name
    def skanja(self):
        print("meow meow rrrrrrrrrrrr")

class Govs(Dzivnieks):
    def __init__(self, name, kajas):
        super().__init__(name, kajas)
        self.name="Milkere "+self.name
    def skanja(self):
        print("moooooooooooo")

dzivniekuSaraksts = []
dzivniekuSaraksts.append(Suns("Reksis", 3))
dzivniekuSaraksts.append(Suns("Volvis", 4))
dzivniekuSaraksts.append(Suns("Jimmys", 4))
dzivniekuSaraksts.append(Kakis("Muris", 4))
dzivniekuSaraksts.append(Kakis("Juris", 5))
dzivniekuSaraksts.append(Govs("Gauja", 4))  #nevar likt Dzivnieks(), jo, ja ir import tas abstract, tad 
                                                #Can't instantiate abstract class Dzivnieks with abstract method skanja

print("####################")
for dzivnieks in dzivniekuSaraksts:
    print(dzivnieks)
    dzivnieks.skanja()


#     d1 = Dzivnieks("Gauja", 4)
# print(d1)
# d1.skanja()

# s1 = Suns("Reksis", 4)
# print(s1)
# s1.skanja()

# s2 = Kakis("Minkans", 4)
# print(s2)
# s2.skanja()

# class Suns(Dzivnieks):
#    def __init__(self, name, kajas):
#        super().__init__(name, kajas)
#        self.skanja = "vua"

# class Kakis(Dzivnieks):
#    def __init__(self, name, kajas):
#        super().__init__(name, kajas)
#        self.skanja = "mjau"
