from flask import Flask, render_template
import utils

app = Flask(__name__)


@app.route('/')
def page_all_candidates():
    candidates = utils.get_data()
    list_candidates = ""

    for candidate in candidates:
        list_candidates += f"{candidate['name']}\n"
        list_candidates += f"{candidate['skills']}\n"
        list_candidates += f"{candidate['position']}\n"
        list_candidates += "\n"

    return "<pre>" + list_candidates + "<pre>"


@app.route('/skills/<skill>')
def page_skills_candidates(skill):
    candidates = utils.get_candidates_skills(skill)
    list_candidates = ""

    for candidate in candidates:
        list_candidates += f"{candidate['name']}\n"
        list_candidates += f"{candidate['skills']}\n"
        list_candidates += f"{candidate['position']}\n"
        list_candidates += "\n"

    return "<pre>" + list_candidates + "<pre>"


@app.route('/candidates/<int:pk>')
def page_pk_candidates(pk):
    candidate = utils.get_candidates_pk(pk)
    pk_candidates = ""

    pk_candidates += f"<img src=\"{candidate['picture']}\">\n"
    pk_candidates += f"{candidate['name']}\n"
    pk_candidates += f"{candidate['skills']}\n"
    pk_candidates += f"{candidate['position']}\n"
    pk_candidates += "\n"

    return "<pre>" + pk_candidates + "</pre>"


app.run()
