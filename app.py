import sqlite3
import json

from flask import Flask, render_template

from src import load_template, query_database


app = Flask(__name__)

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
