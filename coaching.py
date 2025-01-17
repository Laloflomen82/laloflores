import flask

app = flask.Flask("coaching")

def get_html(page_name):
    html_file = open(page_name + ".html")
    content = html_file.read()
    html_file.close()
    return content

@app.route("/")
def homepage():
    return get_html("index")


@app.route("/add")
def new_mail():
    html_page = get_html("index")
    note = flask.request.args.get("email") 
    file = open("emails.txt", "a")
    file.write(note + "\n")
    file.close()
    message = "Tu correo ha sido recibido."
    return html_page.replace("ANIMATE", message)