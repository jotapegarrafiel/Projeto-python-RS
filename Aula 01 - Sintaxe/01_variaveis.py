#Tipos de variaveis
"""
String -> Utilizando "" aspas duplas 
Int -> Qualquer númreo inteiro 
Float -> Qualquer número, inteiro ou quebrado
Booleano -> True or False
List -> Utilizando [] acessado usando o índice de cada argumento
Dict -> Par de chave e valor, cada chave retorna um único valor. Utiliza-se {} e pra acessar basta colocar o valor da chave
Tuplas -> Não é possível alterar as tuplas
"""
#%%
nome = "João"
print(nome)
type(nome)

#%%
numeroInteiro = 27
print(numeroInteiro)
type(numeroInteiro)

#%%
numeroReal = 27.4
print(numeroReal)
type(numeroReal)

#%%
verdadeiro = True
print(verdadeiro)
type(verdadeiro)

#%%
lista = ["João", 27, True, ["João Pedro","Leonora", 27],{"sobrenome":"Gouvea Garrafiel"},("Paulo", 27, True)]

print(lista)
type(lista)

for i in lista:
    print(i)

#%%
dicionario ={"nome":"João",
             "sobrenome":"Garrafiel",
             "idade": 27
            }

#Percorrendo um dicionário usando o for só pra exibir o dicionario
for i in dicionario:
    print(i,"->",dicionario[i])

type(dicionario)

#%%
tuplas = ("Nome", 23, "Pedro", True,[])
print(f"Tuplas original{tuplas}")

# Tuplas não é possivel adicionar ou remover nada, mas se um elemento da tupla for mutável, nesse caso a lista é um tipo mutável, ai sim é possivel alterar

tuplas[-1].extend([34, 27, 21, 32, 65])
print(f"Tuplas com itens adicionados na lista {tuplas}")

# Cuidado ao utilizar o appende para no criar uma nova lista dentro da lista ja existente
tuplas[-1].append([999, 897])
print(f"Tuplas com uma nova lista adicionada dentro da lista ja existente{tuplas}")
#Primeiro tinha-se um tupla com um lista vazia dentro, depois eu adicionei elementos dentro da lista ainda dentro da tupla