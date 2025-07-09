#%%
import random

numero_aleatorio = random.randint(1,15)
tentativas_max = 3

def testa_num():
    for i in range(1, tentativas_max + 1):
        tentativas_restantes = tentativas_max - i
        chute = int(input("Digite um número entre 1 e 15: "))
        
        if chute < numero_aleatorio:
            print("Muito baixo, tente novamente")
        elif chute > numero_aleatorio:
            print("Muito alto, tente novamente")
        else:
            print(f"Você acertou, parabéns. O número era {numero_aleatorio}")
            break
        if tentativas_restantes > 0:
            print(f"Você ainda tem {tentativas_restantes} tentativa(s) restante(s)")
        else:
            print(f"Suas tentativas acabaram. O número era {numero_aleatorio}")
    else:
        print(f"Você não acertou, o número era {numero_aleatorio}")

testa_num()