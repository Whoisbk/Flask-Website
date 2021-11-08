from flask import Flask,redirect,render_template,request,flash,session


app = Flask(__name__)


@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/Contact")
def contact():
    return render_template("contact.html")

@app.route("/Skills")
def skills():
    return render_template("skills.html")

if __name__ == "__main__":
    app.run(debug=True)
