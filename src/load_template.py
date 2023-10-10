from jinja2 import Environment, FileSystemLoader
from datetime import datetime
import pdfkit

def create_pdf(data):
    templateLoader = FileSystemLoader(searchpath="./")
    templateEnv = Environment(loader=templateLoader)
    TEMPLATE_FILE = "./template/template.html"
    template = templateEnv.get_template(TEMPLATE_FILE)
    outputText = template.render(vehicule=data)

    filename = f"{data['desc']}-{str(datetime.now().date())}".replace('\n', '')
    print(filename)
    with open(f'./output/{filename}.html', 'w', encoding="utf-8") as html_file:
        html_file.write(outputText)

    options = {
        'header-html': './template/header.html',
        'footer-right': '[page]',
        'margin-top': '50mm',
        'margin-bottom': '20mm',
        'no-outline': None,
        'allow': ['./template/assets/logo.jpg',],
    }
    
    pdfkit.from_file(f'./output/{filename}.html',f'./output/{filename}.pdf', options=options)
    return f'/download/{filename}'