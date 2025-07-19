#%%
import random
def batata_refri(minha_funcao):
    def nova_funcao(*args):
        print(f"🍟 Fazendo a batata frita")
        minha_funcao(*args)
        print(f"🥤 Servindo o refrigerante")
        sobremesas = ["🧇 Waffle", "🥧 Torta de maçã", "🍫 Chocolate", "🎂 Bolo de chocolate", "🍉 Melancia", "🍩 Donuts"]
        print(f"🍬 Sobremesa do dia: {random.choice(sobremesas)}")
    return nova_funcao
        
@batata_refri
def fazer_hamburguer():
    print(f"🍔 Hamburguer pronto")

fazer_hamburguer()
# %%
@batata_refri
def fazer_pedido(pedido):
    print(f"🍔 Pedido feito: {pedido}")
pedido_usuario = input("Qual lanche gostaria de comer hoje?")
fazer_pedido(pedido_usuario)