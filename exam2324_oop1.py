#2023/2024 m/g
#1. uzdevums
class Doktorats:
    def __init__(self, nosaukums="N/A", pacients=0):
        self.nosaukums = nosaukums
        self.pacients = pacients
    def ievade(self):
        self.nosaukums = input("Ievadi Nosaukumu ")
        try:
            self.pacients = int(input("Ievadi pacientu skaitu "))
        except:
            self.pacients=0
        finally:
            print("Ievade veiksmīga", self.pacients)

    def izvade(self):
        addition=""
        if (self.pacients%10 !=1):
            addition="s"
        print(f"Dokotrāts {self.nosaukums} apkalpo {self.pacients} pacientu{addition}")

d1 = Doktorats("Zemlejas", 300)
d1.ievade()
d1.izvade()
d1.izvade()
d2 = Doktorats()
d2.ievade()
d2.izvade()
d2.izvade()
