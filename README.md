# TaskFlow

**TaskFlow** é um sistema simples de gerenciamento de tarefas com funcionalidades de **CRUD** (Criar, Ler, Atualizar e Deletar). Desenvolvido utilizando **Python**, **Flask**, **SQLite**, **HTML** e **CSS**, o projeto permite ao usuário criar, visualizar, editar e excluir tarefas de forma interativa em uma única página.

## Funcionalidades

- **Adicionar tarefas**: O usuário pode adicionar tarefas com título, descrição, status e datas de criação e entrega.
- **Editar tarefas**: O usuário pode modificar os detalhes de uma tarefa existente.
- **Excluir tarefas**: O sistema permite que o usuário exclua tarefas, confirmando antes da exclusão.
- **Status das tarefas**: As tarefas possuem três estados — *Pendente*, *Em andamento* e *Concluída*.
- **Interface de uma única página**: Todas as interações (adicionar, editar e excluir) ocorrem na mesma página, proporcionando uma experiência fluida e dinâmica para o usuário.
- **Banco de dados SQLite**: As tarefas são armazenadas em um banco de dados SQLite, garantindo persistência das informações.
- **Design responsivo**: O layout foi estilizado com **CSS**, incluindo efeitos visuais como sombras em cartões de tarefas, proporcionando uma interface agradável e profissional.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação principal para a lógica do sistema.
- **Flask**: Framework web utilizado para criar a aplicação, lidar com rotas e interações.
- **SQLite**: Banco de dados leve e local para armazenar as informações das tarefas.
- **HTML e CSS**: Para criar a interface web e estilizar os componentes de forma responsiva e visualmente atraente.

## Como Executar o Projeto

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/CaiioH/TaskFlow.git

2. **Instale as dependências utilizando o Poetry (gerenciador de dependências do projeto):**

   ```bash
   poetry install

3. **Ative o ambiente virtual e inicie o servidor Flask:**

   ```bash
    poetry shell
   
    flask run

## Estrutura do Projeto

```bash
taskflow
├── app.py                  # Arquivo principal com Flask
├── templates/              # Pasta com arquivos HTML
│   ├── index.html          # Página principal
│   ├── form.html           # Formulário para adicionar tarefas
│   └── edit.html           # Formulário para editar tarefas
├── static/                 # Arquivos estáticos (CSS, JS, imagens)
│   └── styles.css          # Arquivo CSS
├── form_db.py              # Arquivo para manipulação do banco de dados
└── tasks.db                # Banco de dados SQLite, que será criado na mesma pasta que o arquivo app.py




