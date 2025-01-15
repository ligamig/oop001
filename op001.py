class Dzivnieks:
    def __init__(self, name, kajas, skanja):
        self.name = name
        self.kajas = kajas
    def skanja(self):
        print("random animal noise")

d1 = Dzivnieks("Gauja", 4)
d1.skanja()