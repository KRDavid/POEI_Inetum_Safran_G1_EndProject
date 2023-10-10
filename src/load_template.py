from jinja2 import Environment, FileSystemLoader
import pdfkit

def create_pdf(data):
    templateLoader = FileSystemLoader(searchpath="./")
    templateEnv = Environment(loader=templateLoader)
    TEMPLATE_FILE = "./template/template.html"
    template = templateEnv.get_template(TEMPLATE_FILE)
    outputText = template.render(vehicule=data)

    html_file = open('output.html', 'w', encoding="utf-8")
    html_file.write(outputText)
    html_file.close()

    options = {
        'header-html': './header.html',
        'footer-right': '[page]',
        'margin-top': '50mm',
        'margin-bottom': '30mm',
        'no-outline': None,
        'allow': ['./logo.jpg',],
    }

    pdfkit.from_file('output.html', 'output.pdf', options=options)