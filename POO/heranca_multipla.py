#%%
class Animal:
    def __init__(self, nome):
        self.nome = nome 
    def emitirSom(self):
        pass
    
class Mamifero(Animal):
    def amamentar(self):
        return f"{self.nome} está amamentando"
    
class Voar(Animal):
    def voar(self):
        return f"{self.nome} está voando"

class Morcego(Mamifero, Voar):
    def emitirSom(self):
        return f"Morcegos emitem sons ultrassônicos"
    
morcego = Morcego(nome="batman")

print(f"O nome do morcego é {morcego.nome}")
print(f"Som do morcego: {morcego.emitirSom()}")
print(f"Morcego amamentando: {morcego.amamentar()}")
print(f"Morcego voando: {morcego.voar()}")