#%%
class Pessoa: # Define uma classe
    def __init__(self, nome, idade): # É um método, por mais que seja um função, dentro de uma CLASSE ele se torna um MÉTODO
        self.nome = nome
        self.idade = idade
    
    def saudacao(self): # Aqui criei um método, pra ser reutilizado no futuro
        return f"Olá, meu nome é {self.nome} e tenho {self.idade} anos"
    
pessoa1 = Pessoa(nome="João", idade=23) # Criei uma variavel passando nome e idade e adicionando na classe criada
mensagem = pessoa1.saudacao() # Atribuí os valores numa variavel utilizando o MÉTODO criado anteriormente
print(mensagem) # Exibi a mensagem