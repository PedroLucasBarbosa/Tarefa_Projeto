class Tarefa:
    def __init__(self, descricao, prioridade="Média"):
        self.descricao = descricao
        self.prioridade = prioridade
        self.concluida = False

    def marcar_concluida(self):
        self.concluida = True

    def __str__(self):
        status = "✔ Concluída" if self.concluida else "✘ Pendente"
        return f"[{status}] {self.descricao} (Prioridade: {self.prioridade})"
