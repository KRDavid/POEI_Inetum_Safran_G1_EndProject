from flask import Flask
import sqlite3
import json

app = Flask(__name__)




@app.route('/get_summary/<int:id>')
def generate_pdf_summary_file(id: int):
    con = sqlite3.connect("database.db")
    cur = con.cursor()
    res = cur.execute("SELECT * FROM vehicule WHERE vehicule_id = ?", [str(id)])
    data = res.fetchall()
    print(data)
    response = json.dumps(data)
    print(response)
    con.close()
    return response

