from lista_tarefas import ListaTarefas

def exibir_menu():
    print("\n=== Gerenciador de Tarefas ===")
    print("1. Adicionar tarefa")
    print("2. Listar tarefas")
    print("3. Marcar tarefa como concluída")
    print("4. Remover tarefa")
    print("5. Sair")

def main():
    lista_tarefas = ListaTarefas()

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            descricao = input("Digite a descrição da tarefa: ")
            prioridade = input("Digite a prioridade (Alta, Média, Baixa): ") or "Média"
            lista_tarefas.adicionar_tarefa(descricao, prioridade)
        
        elif opcao == "2":
            lista_tarefas.listar_tarefas()
        
        elif opcao == "3":
            lista_tarefas.listar_tarefas()
            try:
                indice = int(input("Digite o número da tarefa a ser concluída: "))
                lista_tarefas.marcar_concluida(indice)
            except ValueError:
                print("Por favor, insira um número válido.")

        elif opcao == "4":
            lista_tarefas.listar_tarefas()
            try:
                indice = int(input("Digite o número da tarefa a ser removida: "))
                lista_tarefas.remover_tarefa(indice)
            except ValueError:
                print("Por favor, insira um número válido.")

        elif opcao == "5":
            print("Encerrando o gerenciador de tarefas...")
            break
        
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
