from tarefa import Tarefa

class ListaTarefas:
    def __init__(self):
        self.tarefas = []

    def adicionar_tarefa(self, descricao, prioridade="Média"):
        tarefa = Tarefa(descricao, prioridade)
        self.tarefas.append(tarefa)
        print(f"Tarefa '{descricao}' adicionada com sucesso!")

    def listar_tarefas(self):
        if not self.tarefas:
            print("Nenhuma tarefa encontrada.")
            return
        print("\n=== Tarefas ===")
        for index, tarefa in enumerate(self.tarefas, start=1):
            print(f"{index}. {tarefa}")

    def marcar_concluida(self, indice):
        if 0 < indice <= len(self.tarefas):
            self.tarefas[indice - 1].marcar_concluida()
            print(f"Tarefa '{self.tarefas[indice - 1].descricao}' marcada como concluída!")
        else:
            print("Índice inválido. Tente novamente.")

    def remover_tarefa(self, indice):
        if 0 < indice <= len(self.tarefas):
            removida = self.tarefas.pop(indice - 1)
            print(f"Tarefa '{removida.descricao}' removida com sucesso!")
        else:
            print("Índice inválido. Tente novamente.")
