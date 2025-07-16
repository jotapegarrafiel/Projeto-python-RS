def criarContato(agenda):
    print("Novo Contato")
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    email = input("E-mail: ")
    
    contato = {
        "nome": nome,
        "telefone": telefone,
        "email": email,
        "favorito": False
    }
    agenda.append(contato)
    print("Contato adicionado! ✅")

def listarContato(agenda):
    if not agenda:
        print("Agenda vazia, adicione um contato primeiro")
        return
    
    print("Seus contatos")
    for i, contato in enumerate(agenda):
        coracao = "💙" if contato["favorito"] else ""
        print(f"{i}. {coracao} {contato["nome"]} - {contato["telefone"]} - {contato["email"]}")
    print()
    
def editarContato(agenda):
    if not agenda:
        print("Agenda vazia, tente adicionar um contato primeiro")
        return
    listarContato(agenda)
    try:
        escolha = int(input("Digite o número correspondente do contato que gostaria de editar: "))
        contato = agenda[escolha]
    except (ValueError, IndexError):
        print("Número inválido!")
        return
    
    print("Deixe o campo em branco caso não queira alterar.")
    nome = input(f"Novo nome: ({contato['nome']}): ") or contato['nome']
    telefone = input(f"Novo telefone: ({contato['telefone']}): ") or contato['telefone']
    email = input(f"Novo email: ({contato['email']}): ") or contato['email']
    
    contato["nome"] = nome
    contato["telefone"] = telefone
    contato["email"] = email
    
    print("Contato atualizado com sucesso! ✅")
    
def excluirContato(agenda):
    if not agenda:
        print("Nenhum contato adicionado. Adicione um primeiro")
        return
    listarContato(agenda)
    try:
        indice = int(input("Qual contato gostaria de excluir: "))
        contato = agenda.pop(indice)
        print(f"Contato {contato["nome"]} excluído com sucesso! 🗑")
    except (ValueError, IndexError):
        print("Número inválido!")
        return
    
def favoritoContato(agenda):
    if not agenda:
        print("Nenhum contato encontrado, adicione um primeiro!")
        return
    try:
        listarContato(agenda)
        indice = int(input("Qual contato gostaria de favoritar: "))
        agenda[indice]["favorito"] = True
        print(f"Contato {agenda[indice]["nome"]} marcado com favorito 💙")
    except (ValueError, IndexError):
        print("Número inválido")
        return
        
agenda = []
while True:
    print("""
        Olá, bem vindo a sua agenda digital, digite qual menu gostaria de acessar:
        
        1. Adicionar contato
        2. Listar contatos
        3. Editar contato
        4. Deletar contato
        5. Marcar contato favorito          
        0. Sair
        """)
    escolha = input("Digite sua escolha: ")
    
    if escolha == "1":
        criarContato(agenda)
    elif escolha == "2":
        listarContato(agenda)
    elif escolha == "3":
        editarContato(agenda)
    elif escolha == "4":
        excluirContato(agenda)
    elif escolha == "5":
        favoritoContato(agenda)
    elif escolha == "0":
        print("Saindo da agenda, até mais... 👋")
        break
    else:
        print("Opcão inválida. Tente novamente.")
    