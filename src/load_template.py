import jinja2


def load_template(data):
    templateLoader = jinja2.FileSystemLoader(searchpath="./")
    templateEnv = jinja2.Environment(loader=templateLoader)
    TEMPLATE_FILE = "./template/template.html"
    template = templateEnv.get_template(TEMPLATE_FILE)
    outputText = template.render(vehicule={"desc": 'Jordan t es mort'})

    html_file = open('test.html', 'w', encoding="utf-8")
    html_file.write(outputText)
    html_file.close()