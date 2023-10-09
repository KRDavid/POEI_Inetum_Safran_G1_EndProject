import sqlite3
import json

from flask import Flask, render_template

from src import load_template, query_database

app = Flask(__name__)

from flask import Flask, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

@app.route('/get_vehicules/')
def get_vehicules():
    print('pomme')
    con = sqlite3.connect("database.db")
    cur = con.cursor()
    res = cur.execute("SELECT * FROM vehicule")
    results = res.fetchall()
    print(results)
    data = [{"id": id_, "desc": name} for id_, name in results]
    con.close()
    print(data)
    return jsonify(data)

@app.route('/get_summary/<int:id>')
def generate_pdf_summary_file(id: int):

    con = sqlite3.connect("database.db")
    cur = con.cursor()

    data = query_database.get_datas(cur, id)

    print(data)
    response = json.dumps(data)
    print(response)
    con.close()
    return response

if __name__ == '__main__':
    app.run(debug=True)