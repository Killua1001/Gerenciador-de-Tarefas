tarefas = []

def adicionar():
    nome = input("Digite o nome da tarefa: ")
    descricao = input("Descreva a tarefa que você precisa fazer: ")
    prioridade = input("Qual a prioridade da situação? (baixa, media, alta): ").lower()
    categoria = input("Digite a categoria da tarefa: ").lower()

    tarefa = {
        "nome": nome,
        "descricao": descricao,
        "prioridade": prioridade,
        "categoria": categoria,
        "concluida": False
    }

    tarefas.append(tarefa)
    print("Tarefa adicionada com sucesso!")

def concluir_tarefa():
    Lista_de_tarefas()
    if tarefas:
        indice = int(input("Digite o número da tarefa a ser concluída: ")) - 1
        if 0 <= indice < len(tarefas):
            tarefas[indice]["concluida"] = True
            print("Tarefa concluída com sucesso!")
        else:
            print("Índice inválido!")

def Lista_de_tarefas():
    if not tarefas:
        print("Não há tarefas disponíveis.")
        return
    for i, tarefa in enumerate(tarefas, 1):
        status = "Concluída" if tarefa["concluida"] else "Pendente"
        print(f"{i}. {tarefa['nome']} - {tarefa['descricao']} - Prioridade: {tarefa['prioridade']} - Categoria: {tarefa['categoria']} - Status: {status}")
    print()

def listar_por_prioridade():
    prioridade = input("Qual a prioridade da situação? (baixa, media, alta): ").lower()
    tarefas_filtradas = [t for t in tarefas if t["prioridade"] == prioridade]
    if tarefas_filtradas:
        for tarefa in tarefas_filtradas:
            status = "Concluída" if tarefa["concluida"] else "Pendente"
            print(f"{tarefa['nome']} - {tarefa['descricao']} - Status: {status}")
    else:
        print(f"Não há tarefas com a prioridade {prioridade}.")

def listar_por_categoria():
    categoria = input("Digite a categoria que deseja selecionar: ").lower()
    tarefas_filtradas = [t for t in tarefas if t["categoria"] == categoria]
    if tarefas_filtradas:
        for tarefa in tarefas_filtradas:
            status = "Concluída" if tarefa["concluida"] else "Pendente"
            print(f"{tarefa['nome']} - {tarefa['descricao']} - Status: {status}")
    else:
        print(f"Não há tarefas com a categoria {categoria}.")

def listar_tarefas_concluidas():
    tarefas_concluidas = [t for t in tarefas if t["concluida"]]
    if tarefas_concluidas:
        for tarefa in tarefas_concluidas:
            print(f"{tarefa['nome']} - {tarefa['descricao']} - Status: Concluída")
    else:
        print("Não há tarefas concluídas.")

def listar_tarefas_pendentes():
    tarefas_pendentes = [t for t in tarefas if not t["concluida"]]
    if tarefas_pendentes:
        for tarefa in tarefas_pendentes:
            print(f"{tarefa['nome']} - {tarefa['descricao']} - Status: Pendente")
    else:
        print("Não há tarefas pendentes.")

def mod_menu():
    print("============== Gerenciador de Tarefas =============")
    print("Op -1 Adicionar tarefa")
    print("Op -2 Listar tarefas")
    print("Op -3 Concluir tarefa")
    print("Op -4 Exibir por prioridade")
    print("Op -5 Exibir por categoria")
    print("Op -6 Listar tarefas concluídas")
    print("Op -7 Listar tarefas pendentes")
    print("Op -8 Sair do programa")
    print("============== Menu de Gerenciamento ===========")

def executar():
    while True:
        mod_menu()
        opcao = input("Escolha uma opção de 1-8: ")
        if opcao == "1":
            adicionar()
        elif opcao == "2":
            Lista_de_tarefas()
        elif opcao == "3":
            concluir_tarefa()
        elif opcao == "4":
            listar_por_prioridade()
        elif opcao == "5":
            listar_por_categoria()
        elif opcao == "6":
            listar_tarefas_concluidas()
        elif opcao == "7":
            listar_tarefas_pendentes()
        elif opcao == "8":
            print("Saindo... Até mais!")
            break
        else:
            print("Opção inválida! Escolha um número de 1 a 8.")

if __name__ == "__main__":
    executar()
