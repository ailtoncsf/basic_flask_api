# blog.py - controller


# imports
from flask.json import jsonify
from flask import Flask, request, g
import sqlite3

app = Flask(__name__)


def connect_db():
    return sqlite3.connect('afropython.db')


@app.route('/create', methods=['GET'])
def create():
    g.connection = connect_db()
    g.connection.execute('CREATE TABLE pessoa (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, nome TEXT)')
    return jsonify(msg='Tabela criada com sucesso!')


@app.route('/pessoas', methods=['GET'])
def get():
    g.connection = connect_db()
    cur = g.connection.execute('SELECT * FROM pessoa')
    pessoas = cur.fetchall()
    g.connection.close()
    return jsonify(pessoas)


@app.route('/pessoa', methods=['POST'])
def add():
    nome = request.form['nome']
    if nome:
        g.connection = connect_db()
        g.connection.execute(
            'INSERT INTO pessoa (nome) VALUES (?)', [nome]
        )
        g.connection.commit()
        g.connection.close()
        return jsonify(msg='Pessoa preta adicionada com sucesso!')


@app.route('/pessoa', methods=['PUT'])
def update():
    nome = request.form['nome']
    id = request.form['id']
    if nome:
        g.connection = connect_db()
        g.connection.execute(
            'UPDATE pessoa SET nome = (?) WHERE id=?',
            [nome, id]
        )
        g.connection.commit()
        g.connection.close()
        return jsonify(msg='Nome atualizado com sucesso!')


@app.route('/pessoa', methods=['DELETE'])
def delete():
    id = request.form['id']
    if id:
        g.db = connect_db()
        g.db.execute(
            'DELETE FROM pessoa WHERE id = ?',
            [id]
        )
        g.db.commit()
        g.db.close()
        return jsonify(msg='Pessoa preta excluida com sucesso!')


if __name__ == '__main__':
    app.run(debug=True)

