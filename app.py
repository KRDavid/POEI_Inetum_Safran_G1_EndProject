import sqlite3

from flask import Flask, jsonify, send_from_directory, request
from flask_cors import CORS
from requests import post

from src import load_template, query_database

app = Flask(__name__)
CORS(app)

def notify_other_server(data):
    try:
        response = post('http://localhost:5001/notifications/', json=data)
        print(response.json()['message'])
        return response.text
    except Exception as e:
        print(f"Error sending notification: {e}")
        return None

# Récupération de la liste des véhicules
@app.route('/get_vehicules/')
def get_vehicules():
    with sqlite3.connect("sql/database.db") as con:  # Utilisation d'un context manager pour la gestion de la connexion
        cur = con.cursor()
        res = cur.execute("SELECT * FROM vehicule")
        results = res.fetchall()

    data = [{"id": id_, "desc": name} for id_, name in results]
    return jsonify(data)

# Générer un PDF récapitulatif pour un véhicule spécifique
@app.route('/get_summary/<int:id>')
def generate_pdf_summary_file(id: int):
    # Envoyer une notification pour informer que le fichier est demandé
    notify_other_server({"message": f"File with ID {id} has been requested"})

    with sqlite3.connect("sql/database.db") as con:
        cur = con.cursor()
        data = query_database.get_datas(cur, id)
    
    download = load_template.create_pdf(data)

    # Envoyer une notification pour informer que le fichier est créé
    notify_other_server({"message": f"File {download} with ID {id} has been created"})

    return download

# Fournir un fichier PDF pour téléchargement
@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory('output', f"{filename}.pdf", as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)
