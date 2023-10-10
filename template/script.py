from jinja2 import Environment, FileSystemLoader
import pdfkit

data= {
  "vehicule": [
    {"id": 0, "desc": "vehicule4"},
    {"id": 1, "desc": "vehicule1"},
    {"id": 2, "desc": "vehicule2"},
    {"id": 3, "desc": "vehicule3"}
  ],
  "poste": [
    {"id": 0, "desc": ""},
    {"id": 1, "desc": "poste1"},
    {"id": 2, "desc": "poste2"},
    {"id": 3, "desc": "poste3"}
  ],
  "ordre": [
    {"id": 1, "desc": "ordre1_poste1_vehicule1", "poste": 1, "vehicule": 1},
    {"id": 2, "desc": "ordre2_poste1_vehicule2", "poste": 1, "vehicule": 2},
    {"id": 3, "desc": "ordre3_poste2_vehicule1", "poste": 2, "vehicule": 1},
    {"id": 4, "desc": "ordre4_poste3_vehicule2", "poste": 3, "vehicule": 2},
    {"id": 5, "desc": "ordre5_poste2_vehicule2", "poste": 2, "vehicule": 2}
  ],
  "incident": [
    {"id": 1, "desc": "incident1_ordre1", "ordre": 1, "etat": "OPEN"},
    {"id": 2, "desc": "incident2_ordre2", "ordre": 2, "etat": "OPEN"},
    {"id": 3, "desc": "incident3_ordre2", "ordre": 2, "etat": "OPEN"},
    {"id": 4, "desc": "incident4_ordre4", "ordre": 4, "etat": "OPEN"},
    {"id": 5, "desc": "incident5_ordre4", "ordre": 4, "etat": "OPEN"}
  ]
}

env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('template.html')

vehicule_id = 2
vehicule = next((v for v in data['vehicule'] if v['id'] == vehicule_id), None)

# Trouver les ordres pour ce véhicule.
related_orders = [order['id'] for order in data['ordre'] if order['vehicule'] == vehicule_id]
# Trouver les incidents liés à ces ordres.
related_incidents = [incident for incident in data['incident'] if incident['ordre'] in related_orders]

vehicule['incidents'] = related_incidents
vehicule['ordre'] = related_orders

print(vehicule)

rendered_html = template.render(vehicule=vehicule)

with open("output.html", "w") as f:
    f.write(rendered_html)

options = {
    'header-html': './header.html',
    'footer-right': '[page]',
    'margin-top': '50mm',
    'margin-bottom': '30mm',
    'no-outline': None,
    'allow': ['./logo.jpg',],  # Add this line. Specify the path where your resources (like images) are stored.
}


pdfkit.from_file('output.html', 'output.pdf', options=options)
