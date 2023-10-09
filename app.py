from flask import Flask

app = Flask(__name__)

@app.route('/get_summary/<int:id>')
def generate_pdf_summary_file(id: int):
    return f"id: {id}"

