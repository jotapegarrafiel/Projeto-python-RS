#%%
def check_status(tarefas):
    for i, tarefa in enumerate(tarefas, start=1):
        status = "✅" if tarefa["completada"] else "⏳"
        print(f"{i}. Tarefa: {tarefa['tarefa']} {status}")

def criar_tarefa(tarefas, nome_tarefa):
    tarefa = {"tarefa": nome_tarefa, "completada":False}
    tarefas.append(tarefa)
    print(f"Tarefa {nome_tarefa} adicionada com sucesso")
    return

def exibir_tarefas(tarefas):
    if not tarefas:
        print("Nenhuma tarefa registrada")
        return
    print("Atividades registradas")
    check_status(tarefas)

def atualizar_tarefas(tarefas):
    if not tarefas:
        print("Nenhuma tarefa para atualizar")
        return
    check_status(tarefas)
        
    try:
        escolha = int(input("Digite qual atividade gostaria de alterar: "))
        if 1 <= escolha <= len(tarefas):
            nova_tarefa = input("Digite a nova descrição da atividade: ")
            tarefas[escolha - 1]["tarefa"] = nova_tarefa
            print("Atividade atualizada com sucesso")
        else:
            print("Número inválido")
    except ValueError:
        print("Por favor, digite um valor válido")

def completar_tarefas(tarefas):
    if not tarefas:
        print("Nenhuma tarefa para completar")
        return
    check_status(tarefas)
    try:
        escolha = int(input("Escolha qual opção gostaria de marcar como completa: "))
        if 1 <= escolha <= len(tarefas):
            tarefas[escolha - 1]["completada"] = True
            print("Tarefa marcada como completa")
        else:
            ("Número inválido")
    except ValueError:
        print("Por favor, digite um valor válido")

def apagar_tarefas(tarefas):
    if not tarefas:
        print("Nenhuma tarefa registrada")
        return
    antes = len(tarefas)
    tarefas[:] = [t for t in tarefas if not t["completada"]]
    depois = len(tarefas)
    print(f"{antes - depois} tarefa(s) completada(s) deletada(s).")
       
tarefas = []

while True:
    print("""
        Olá, bem vindo ao seu gerenciador de atividades
        
        1. Adicionar atividade
        2. Ver tarefas
        3. Editar tarefas
        4. Completar tarefas
        5. Deletar tarefas completas
        6. Sair
        """)
    escolha = input("Digite sua escolha: ")
    if escolha == "1":
        nome_tarefa =input("Qual atividade deseja adicionar: ")
        criar_tarefa(tarefas, nome_tarefa)
    elif escolha == "2":
        exibir_tarefas(tarefas)
    elif escolha == "3":
        atualizar_tarefas(tarefas)
    elif escolha == "4":
        completar_tarefas(tarefas)
    elif escolha == "5":
        apagar_tarefas(tarefas)
    elif escolha == "6":
        print("Finalizando o programa, até a próxima 🖐")
        break
