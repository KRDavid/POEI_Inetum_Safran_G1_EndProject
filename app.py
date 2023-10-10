import sqlite3
import json

from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS

from src import load_template, query_database

app = Flask(__name__)
CORS(app)


@app.route('/get_vehicules/')
def get_vehicules():
    con = sqlite3.connect("sql/database.db")
    cur = con.cursor()

    res = cur.execute("SELECT * FROM vehicule")
    results = res.fetchall()

    data = [{"id": id_, "desc": name} for id_, name in results]

    con.close()

    return jsonify(data)

@app.route('/get_summary/<int:id>')
def generate_pdf_summary_file(id: int):

    con = sqlite3.connect("sql/database.db")
    cur = con.cursor()

    data = query_database.get_datas(cur, id)
    response = json.dumps(data)
    con.close()

    download = load_template.create_pdf(data)
    return download

@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory('output', f"{filename}.pdf", as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)