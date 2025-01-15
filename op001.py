class Dzivnieks:
    def __init__(self, name, kajas, skanja):
        self.name = name
        self.kajas = kajas
    def skanja(self):
        print("random animal noise")

d1 = Dzivnieks("Kakis", 4, "mjau")
print(d1.name, d1.kajas)