import sqlite3 as sql
import os

# Caminho do banco de dados
DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tasks.db')

# Inicializa o banco de dados, criando a tabela se necessário
def init_db():
    con = sql.connect(DB_PATH)
    cur = con.cursor()

    # Criar a tabela tasks, se ela não existir
    cur.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            descricao TEXT,
            status TEXT NOT NULL,
            data_criacao DATETIME DEFAULT CURRENT_TIMESTAMP,
            prazo_entrega DATETIME
        );
    ''')

    con.commit()
    con.close()

# Função para recuperar todas as tarefas
def get_all_tasks():
    con = sql.connect(DB_PATH)
    con.row_factory = sql.Row  # Permite acessar as colunas pelo nome
    cur = con.cursor()
    cur.execute("SELECT * FROM tasks")
    tasks = cur.fetchall()  # Recupera todas as tarefas
    con.close()
    return tasks

# Função para recuperar uma tarefa pelo ID
def get_task_by_id(task_id):
    con = sql.connect(DB_PATH)
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("SELECT * FROM tasks WHERE id = ?", (task_id,))
    task = cur.fetchone()
    con.close()
    return task




