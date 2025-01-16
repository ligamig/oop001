class Dzivnieks:
    def __init__(self, name, kajas):
        self.name = name
        self.kajas = kajas
    def skanja(self):
        print("random animal noise")
#        return self.skanja
    def __str__(self):
        return f"{self.name} un {self.kajas} kajas"

class Suns(Dzivnieks):
    def __init__(self, name, kajas):
        super().__init__(name, kajas)
        self.name="Komisars"+self.name
    def skanja(self):
        print("vau vau")

d1 = Dzivnieks("Gauja", 4)
print(d1)
d1.skanja()

s1 = Suns("Reksis", 4)
print(s1)
s1.skanja()

#class Suns(Dzivnieks):
#    def __init__(self, name, kajas):
#        super().__init__(name, kajas)
#        self.skanja = "vua"

#class Kakis(Dzivnieks):
#    def __init__(self, name, kajas):
#        super().__init__(name, kajas)
#        self.skanja = "mjau"
