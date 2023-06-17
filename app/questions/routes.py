from typing import List

from flask import render_template, request, redirect, url_for
from app.questions import bp
from app.models.question import Question
from app.extensions import db


# sitas endpoint gali priimti ir issiusti info
@bp.route("/", methods=("GET", "POST"))
def index():
    questions: List[Question] = Question.query.all()
    print(dir(request))
    print(request.form)
    # viska pasiimti kas ateina is User puses sesijos metu
    if request.method == "POST":
        # inicializuotas objektas, kuris yra RAMuose
        new_question = Question(
            content=request.form["content"], answer=request.form["answer"]
        )
        # dadetas i sesija objektas
        db.session.add(new_question)
        # kad irasas atsirastu DB reikia commit, priskiriamas automatiskai ID (kadangi neturim tiesioginio rysio)
        db.session.commit()
        # atvaizduoja ta pacia funkcija index()
        return redirect(url_for("questions.index"))

    return render_template("questions/index.html", questions=questions)


# oranzines spalvos programos reiksmes ateina is templates html
