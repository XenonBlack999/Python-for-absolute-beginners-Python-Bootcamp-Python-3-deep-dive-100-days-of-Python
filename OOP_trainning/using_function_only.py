class Soilder:
    def __init__(self, name, kage, position):
        self.name = name
        self.kage = kage
        self.position = position
        
    def soilder_position(self):
        return f"This is our Great General,His name was {self.name},He serve for {self.kage},with {self.position} Position"
    
latyarbalu = Soilder("MinHtinNawYaHtar", "Ah Loung Min Tayar", "Field marshal")
tainkyarminkaung = Soilder("Tain Kyar Min Kaung", "Sin Phyu Sin", "Field marshal")


print(latyarbalu.soilder_position())
print(tainkyarminkaung.soilder_position())
