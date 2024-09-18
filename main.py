from flask import Flask, render_template, request, url_for, redirect, session
import re
from applicant import Applicant
from room import Room

app = Flask(__name__)
app.config["SECRET_KEY"] = "f2ar6YJjeD0g0kuISswBr6KG"
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

applications = []

rooms = {}


def check_email(email):
    return re.fullmatch(regex, email)


def name_available(name):
    for room in rooms:
        if name == room.name:
            return False

    return True


@app.route("/")
def landing_page():
    return render_template("index.html")


@app.route("/create", methods=["POST", "GET"])
def create():

    session.clear()
    if request.method == "POST":
        name = request.form.get("name")
        amount = request.form.get("amount")
        create = request.form.get("create", False)

        if not name:
            return render_template("create.html",
                                   error="Please give a name for the drawing",
                                   name=name,
                                   amount=amount)

        if not name_available(name):
            return render_template("create.html",
                                   error="Name is unavailable",
                                   name="",
                                   amount=amount)

        if not amount:
            return render_template("create.html",
                                   error="Pleave give the amount of winners you want",
                                   name=name,
                                   amount=amount)

        rooms[name] = Room(name, amount)
        session["room_name"] = name

        return redirect(url_for("main"))

    return render_template("create.html")


@app.route("/main", methods=["POST", "GET"])
def main():
    room_name = session.get("room_name")

    if request.method == "POST":
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        email = request.form.get("email")
        submit = request.form.get("submit", False)

        if not first_name:
            return render_template("main.html",
                                   error="Please enter your first name",
                                   first_name=first_name,
                                   last_name=last_name,
                                   email=email,
                                   room_name=room_name)

        if not last_name:
            return render_template("main.html",
                                   error="Please enter your last name",
                                   first_name=first_name,
                                   last_name=last_name,
                                   email=email,
                                   room_name=room_name)

        if not check_email(email):
            return render_template("main.html",
                                   error="Please enter a valid email",
                                   first_name=first_name,
                                   last_name=last_name,
                                   email=email,
                                   room_name=room_name)

        if submit:
            rooms[room_name].new_application(
                Applicant(first_name, last_name, email))

    return render_template("main.html", room_name=room_name)


@app.route("/trekking")
def trekking():

    return render_template("trekking.html")


if __name__ == "__main__":
    app.run(port=8000, debug=True)
