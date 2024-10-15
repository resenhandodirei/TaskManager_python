import json
import os

class GerenciadorTarefas:
    def __init__(self, arquivo_json='tarefas.json'):
        self.arquivo_json = arquivo_json
        self.tarefas = self.carregar_tarefas()

    def carregar_tarefas(self):
        """Carrega as tarefas do arquivo JSON, se existir."""
        if os.path.exists(self.arquivo_json):
            with open(self.arquivo_json, 'r') as arquivo:
                return json.load(arquivo)
        return []

    def salvar_tarefas(self):
        """Salva as tarefas no arquivo JSON."""
        with open(self.arquivo_json, 'w') as arquivo:
            json.dump(self.tarefas, arquivo, indent=4)

    def adicionar_tarefa(self, descricao):
        """Adiciona uma nova tarefa com a descrição fornecida."""
        nova_tarefa = {
            "id": len(self.tarefas) + 1,
            "descricao": descricao,
            "concluida": False
        }
        self.tarefas.append(nova_tarefa)
        self.salvar_tarefas()
        print(f"Tarefa '{descricao}' adicionada com sucesso!")

    def listar_tarefas(self):
        """Exibe todas as tarefas com o status de conclusão."""
        if not self.tarefas:
            print("Nenhuma tarefa encontrada.")
            return
        for tarefa in self.tarefas:
            status = "Concluída" if tarefa["concluida"] else "Pendente"
            print(f"ID: {tarefa['id']} - {tarefa['descricao']} [{status}]")

    def remover_tarefa(self, id_tarefa):
        """Remove uma tarefa pelo ID."""
        self.tarefas = [tarefa for tarefa in self.tarefas if tarefa["id"] != id_tarefa]
        self.salvar_tarefas()
        print(f"Tarefa com ID {id_tarefa} removida com sucesso!")

    def concluir_tarefa(self, id_tarefa):
        """Marca uma tarefa como concluída pelo ID."""
        for tarefa in self.tarefas:
            if tarefa["id"] == id_tarefa:
                tarefa["concluida"] = True
                self.salvar_tarefas()
                print(f"Tarefa '{tarefa['descricao']}' concluída com sucesso!")
                return
        print(f"Tarefa com ID {id_tarefa} não encontrada.")

def exibir_menu():
    print("\nGerenciador de Tarefas")
    print("1. Adicionar Tarefa")
    print("2. Listar Tarefas")
    print("3. Remover Tarefa")
    print("4. Concluir Tarefa")
    print("5. Sair")

def main():
    gerenciador = GerenciadorTarefas()

    while True:
        exibir_menu()
        opcao = input("\nEscolha uma opção: ")

        if opcao == '1':
            descricao = input("Digite a descrição da tarefa: ")
            gerenciador.adicionar_tarefa(descricao)
        elif opcao == '2':
            gerenciador.listar_tarefas()
        elif opcao == '3':
            id_tarefa = int(input("Digite o ID da tarefa a ser removida: "))
            gerenciador.remover_tarefa(id_tarefa)
        elif opcao == '4':
            id_tarefa = int(input("Digite o ID da tarefa a ser concluída: "))
            gerenciador.concluir_tarefa(id_tarefa)
        elif opcao == '5':
            print("Saindo...")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
