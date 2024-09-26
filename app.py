from form_db import get_all_tasks, get_task_by_id, init_db
from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3 as sql
import os

# Caminho do banco de dados
DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tasks.db')

# Inicializa o banco de dados
init_db()

app = Flask(__name__)
app.secret_key = 'chave_secreta'

# Rota principal
@app.route("/")
@app.route("/index")
def index():
    # Recupera todas as tarefas do banco de dados
    tasks = get_all_tasks()
    return render_template("index.html", tasks=tasks)

# Rota para adicionar tarefa
@app.route("/add_task", methods=["POST", "GET"])
def add_task():
    if request.method == "POST":
        titulo = request.form["titulo"]
        descricao = request.form["descricao"]
        status = request.form["status"]
        prazo_entrega = request.form["prazo_entrega"]

        con = sql.connect(DB_PATH)
        cur = con.cursor()
        cur.execute("INSERT INTO tasks (titulo, descricao, status, prazo_entrega) VALUES (?, ?, ?, ?)",
                    (titulo, descricao, status, prazo_entrega))
        con.commit()
        con.close()

        flash("Tarefa adicionada com sucesso!", "success")
        return redirect(url_for("index"))

    return render_template("add_task.html")

# Rota para editar tarefa
@app.route("/edit_task/<int:id>", methods=["POST", "GET"])
def edit_task(id):
    if request.method == "POST":
        titulo = request.form["titulo"]
        descricao = request.form["descricao"]
        status = request.form["status"]
        prazo_entrega = request.form["prazo_entrega"]

        con = sql.connect(DB_PATH)
        cur = con.cursor()
        cur.execute("UPDATE tasks SET titulo = ?, descricao = ?, status = ?, prazo_entrega = ? WHERE id = ?",
                    (titulo, descricao, status, prazo_entrega, id))
        con.commit()
        con.close()

        flash("Tarefa atualizada com sucesso!", "success")
        return redirect(url_for("index"))

    # Obtém a tarefa pelo ID para edição
    task = get_task_by_id(id)
    return render_template("edit_task.html", task=task)

# Rota para excluir tarefa
@app.route("/delete_task/<int:id>", methods=["POST"])
def delete_task(id):
    con = sql.connect(DB_PATH)
    cur = con.cursor()
    cur.execute("DELETE FROM tasks WHERE id = ?", (id,))
    con.commit()
    con.close()

    flash("Tarefa excluída com sucesso!", "warning")
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
