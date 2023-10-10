import sqlite3
import json

from flask import Flask, jsonify, render_template
from flask_cors import CORS

from src import load_template, query_database

app = Flask(__name__)
CORS(app)


@app.route('/get_vehicules/')
def get_vehicules():
    con = sqlite3.connect("database.db")
    cur = con.cursor()

    res = cur.execute("SELECT * FROM vehicule")
    results = res.fetchall()

    data = [{"id": id_, "desc": name} for id_, name in results]

    con.close()

    return jsonify(data)



@app.route('/get_summary/<int:id>')
def generate_pdf_summary_file(id: int):

    con = sqlite3.connect("database.db")
    cur = con.cursor()

    data = query_database.get_datas(cur, id)
    response = json.dumps(data)
    con.close()

    load_template.create_pdf(data)
    return response

if __name__ == '__main__':
    app.run(debug=True)