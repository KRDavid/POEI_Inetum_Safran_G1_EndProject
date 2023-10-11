from jinja2 import Environment, FileSystemLoader
from datetime import datetime
from PyPDF2 import PdfReader

import pdfkit
import os

# Nettoie et formate une chaîne de caractères
def clean_string(s):
    return ' '.join(s.split())

# Récupère les numéros de page pour une section donnée
def get_pages_for_section(pdf_path, section_title):
    pages = []
    clean_title = clean_string(section_title)
    
    with open(pdf_path, "rb") as file:
        reader = PdfReader(file)
        for page_num, page in enumerate(reader.pages):
            if clean_title in clean_string(page.extract_text()):
                pages.append(page_num + 1)
    return pages

# Obtient les numéros de page pour chaque poste
def get_poste_pages(pdf_path, posts):
    return {post[1]: get_pages_for_section(pdf_path, f"déclarés sur le poste de travail {post[1]}")[0] for post in posts}

# Crée un PDF basé sur un template HTML et des données
def create_pdf(data):
    templateLoader = FileSystemLoader(searchpath="./")
    templateEnv = Environment(loader=templateLoader)
    template = templateEnv.get_template("./template/template.html")

    # Génère un PDF préliminaire pour analyse
    outputText = template.render(vehicule=data, pages_per_post={})
    filename = f"{data['desc']}-{datetime.now().date()}".replace('\n', '')
    htmlPath = f"./output/{filename}_temp.html"
    pdfPath = f'./output/{filename}_temp.pdf'
    
    with open(htmlPath, 'w', encoding="utf-8") as html_file:
        html_file.write(outputText)

    options = {
        'header-html': './template/header.html',
        'footer-right': '[page]',
        'margin-top': '50mm',
        'margin-bottom': '20mm',
        'no-outline': None,
        'allow': ['./template/assets/logo.jpg',],
    }

    pdfkit.from_file(htmlPath, pdfPath, options=options)

    # Obtenir les numéros de page pour chaque section et poste
    pages_per_post = get_poste_pages(pdfPath, data['posts_distinct'])
    
    outputText = template.render(
        vehicule=data, 
        resume_page=get_pages_for_section(pdfPath, "Ce rapport a pour but d’informer")[0],
        incidents_page=get_pages_for_section(pdfPath, "Le tableau ci-dessous montre la liste des incidents pour le véhicule")[0], 
        incidents_details_page=get_pages_for_section(pdfPath, "Liste détaillé des incidents")[0],
        pages_per_post=pages_per_post
    )
    
    with open(htmlPath, 'w', encoding="utf-8") as html_file:
        html_file.write(outputText)

    # Génère le PDF final et supprime les fichiers temporaires
    pdfkit.from_file(htmlPath, f'./output/{filename}.pdf', options=options)
    os.remove(htmlPath)
    os.remove(pdfPath)

    return f'/download/{filename}'
