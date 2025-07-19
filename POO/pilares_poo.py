#%%
class animal: 
    def __init__(self, nome):
        self.nome = nome
    
    def andar(self):
        print(f"o {self.nome} andou 5m.")
    
    def emitirSom(self):
        pass
    
class Dino(animal):
    def emitirSom(self):
        return "Grrr"
class Gato(animal):
    def emitirSom(self):
        return "Miau miau"

dino = Dino("Rex")
cat = Gato("Menosso")

animais = [dino,cat]

for animal in animais:
    print(f"o {animal.nome} faz {animal.emitirSom()}")
    
# %%
class contaBancaria:
    def __init__(self, saldo):
        self.__saldo = saldo # Atributo privado usando __
        
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor     
             
    def sacar(self, valor):
        if valor > 0 and valor <= self.__saldo:
             self.__saldo -= valor
             
    def consultarSaldo(self):
        return self.__saldo
    
conta = contaBancaria(2000)
print(f"Saldo da conta bancária: {conta.consultarSaldo()}")
conta.depositar(350)
print(f"Saldo da conta bancária: {conta.consultarSaldo()}")
conta.sacar(500)
print(f"Saldo da conta bancária: {conta.consultarSaldo()}")