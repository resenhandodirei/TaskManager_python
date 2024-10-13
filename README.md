# Task Manager

## Descrição

O **Task Manager** é uma aplicação em Python que permite ao usuário adicionar, listar, remover e marcar tarefas como concluídas. As tarefas são persistidas em um arquivo JSON, permitindo que o usuário feche o programa e continue de onde parou na próxima execução. Este projeto serve como uma introdução à persistência de dados utilizando JSON, além de boas práticas de manipulação de arquivos e interação com o usuário no terminal.

## Funcionalidades

- **Adicionar tarefa**: Crie novas tarefas com uma descrição.
- **Listar tarefas**: Visualize todas as tarefas, tanto pendentes quanto concluídas.
- **Remover tarefa**: Exclua uma tarefa pelo seu ID.
- **Marcar tarefa como concluída**: Atualize o status de uma tarefa para "concluída".
- **Persistência de dados**: As tarefas são armazenadas em um arquivo JSON para que os dados possam ser recuperados em futuras execuções do programa.

## Pré-requisitos

Para executar o projeto, você precisará de:

- Python 3.x instalado no sistema.

## Como executar o projeto

1. Clone este repositório para o seu ambiente local:
    ```bash
    git clone https://github.com/seu-usuario/gerenciador-de-tarefas.git
    ```
   
2. Acesse a pasta do projeto:
    ```bash
    cd gerenciador-de-tarefas
    ```

3. Execute o arquivo `main.py`:
    ```bash
    python main.py
    ```

4. Siga as instruções no terminal para interagir com o sistema de gerenciamento de tarefas.

## Exemplo de uso

### Menu Principal:

```
Gerenciador de Tarefas
1. Adicionar Tarefa
2. Listar Tarefas
3. Remover Tarefa
4. Concluir Tarefa
5. Sair
```

### Adicionando uma nova tarefa:

```
Escolha uma opção: 1
Digite a descrição da tarefa: Estudar Python
Tarefa 'Estudar Python' adicionada com sucesso!
```

### Listando tarefas:

```
Escolha uma opção: 2
ID: 1 - Estudar Python [Pendente]
```

### Concluindo uma tarefa:

```
Escolha uma opção: 4
Digite o ID da tarefa a ser concluída: 1
Tarefa 'Estudar Python' concluída com sucesso!
```

### Removendo uma tarefa:

```
Escolha uma opção: 3
Digite o ID da tarefa a ser removida: 1
Tarefa com ID 1 removida com sucesso!
```

## Estrutura do projeto

```
gerenciador-de-tarefas/
│
├── tarefas.json         # Arquivo onde as tarefas serão persistidas
├── main.py              # Script principal para execução do sistema
├── README.md            # Documentação do projeto
└── .gitignore           # Arquivos e pastas a serem ignorados pelo Git
```

## Tecnologias Utilizadas

- **Python**: Linguagem principal utilizada para o desenvolvimento do sistema.
- **JSON**: Formato de arquivo utilizado para a persistência dos dados de tarefas.

## Melhorias Futuras

Algumas possíveis melhorias para versões futuras do projeto:

- Adicionar validações de entrada para evitar erros de digitação.
- Implementar a possibilidade de editar descrições de tarefas.
- Implementar filtragem de tarefas por status (pendentes ou concluídas).
- Criar uma interface gráfica utilizando bibliotecas como `tkinter` ou `PyQt`.

## Contribuições

Contribuições são sempre bem-vindas! Sinta-se à vontade para abrir *issues* ou enviar *pull requests*.

---

## Licença

Este projeto está licenciado sob a Licença MIT - consulte o arquivo [LICENSE](LICENSE) para mais detalhes.

---

## Contato

- **Desenvolvedor**: Larissa Corrêa
- **Email**: larissamscorrea@gmail.com

