from flask import Flask, render_template, request, url_for, redirect
import re
from applicant import Applicant

app = Flask(__name__)

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

applications = []


def check_email(email):
    return re.fullmatch(regex, email)


@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        email = request.form.get("email")
        submit = request.form.get("submit", False)

        if not first_name:
            return render_template("index.html",
                                   error="Please enter your first name",
                                   first_name=first_name,
                                   last_name=last_name,
                                   email=email)

        if not last_name:
            return render_template("index.html",
                                   error="Please enter your last name",
                                   first_name=first_name,
                                   last_name=last_name,
                                   email=email)

        if not check_email(email):
            return render_template("index.html",
                                   error="Please enter a valid email",
                                   first_name=first_name,
                                   last_name=last_name,
                                   email=email)

        if submit:
            applications.append(Applicant(first_name, last_name, email))

    return render_template("index.html")


@app.route("/trekking")
def trekking():

    return render_template("trekking.html")


if __name__ == "__main__":
    app.run(debug=True)
