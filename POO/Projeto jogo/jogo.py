import random

class Personagem:
    def __init__(self, nome, vida, nivel):
        self.__nome = nome
        self.__vida = vida
        self.__nivel = nivel
        
    def get_nome(self):
        return self.__nome
    
    def get_vida(self):
        return self.__vida
    
    def get_nivel(self):
        return self.__nivel
    
    def exibir_detalhes(self):
        return f"Nome: {self.get_nome()}\nVida: {self.get_vida()}\nNível: {self.get_nivel()}"
    
    def receber_dano(self, dano):
        self.__vida -= dano
        if self.__vida < 0:
            self.__vida = 0

    def atacar(self, alvo):
        dano = random.randint(self.get_nivel() * 3, self.get_nivel() * 4)
        alvo.receber_dano(dano)
        print(f"{self.get_nome()} atacou o {alvo.get_nome()} e causou {dano} de dano")
                    
class Heroi(Personagem):
    def __init__(self, nome, vida, nivel, habilidade):
        super().__init__(nome, vida, nivel)
        self.__habilidade = habilidade
    
    def get_habilidade(self):
        return self.__habilidade
    
    def exibir_detalhes(self):
        detalhes = super().exibir_detalhes()
        return f"{detalhes}\nHabilidade: {self.get_habilidade()}\n"
    
    def ataque_especial(self, alvo):
        dano = random.randint(self.get_nivel() * 5, self.get_nivel() * 7)
        alvo.receber_dano(dano)
        print(f"{self.get_nome()} usou a habilidade especial {self.get_habilidade()} em {alvo.get_nome()} e causou {dano} de dano")
        
class Inimigo(Personagem):
    def __init__(self, nome, vida, nivel, tipo):
        super().__init__(nome, vida, nivel)
        self.__tipo = tipo
    
    def get_tipo(self):
        return self.__tipo
    
    def exibir_detalhes(self):
        detalhes = super().exibir_detalhes()
        return f"{detalhes}\nTipo: {self.get_tipo()}\n"
    
class Jogo: # Classe que organiza o jogo
    def __init__(self):
        self.heroi = Heroi(nome="Odysseu",vida=100,nivel=5,habilidade="Último romântico")
        self.inimigo = Inimigo(nome="Poseidon",vida=80,nivel=3,tipo="Água")

    def iniciar_combate(self):
        print("Iniciando combate")
        while self.heroi.get_vida() > 0 and self.inimigo.get_vida():
            print("\nDetalhes dos personagens!\n")    
            print(self.heroi.exibir_detalhes())
            print(self.inimigo.exibir_detalhes())
            input("Pressione ENTER para atacar")
            escolha = input("Escolha (1- Ataque normal; 2- Ataque Especial): \n")
            if escolha == "1":
                self.heroi.atacar(self.inimigo)
            elif escolha == "2":
                self.heroi.ataque_especial(self.inimigo)
            else:
                print("Escolha inválida. Tente novamente")
                
            if self.inimigo.get_vida() > 0:
                self.inimigo.atacar(self.heroi)
                
        if self.heroi.get_vida() > 0:
            print("Parabéns, você venceu a batalha!")
        else:
            print("Você foi derrotado")
        
        
jogo = Jogo()
jogo.iniciar_combate()