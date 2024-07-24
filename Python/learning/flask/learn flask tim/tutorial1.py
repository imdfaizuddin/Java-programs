from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello! this is the main page <h1>Hello World!</h1>"

@app.route("/<name>")
def user(name):
    # return f"Hello {name}"
    return render_template("index.html", nameVal = name, r="print Hello 10 times:")

# @app.route("/admin")
# def admin():
#     return redirect(url_for("home"))
@app.route("/admin/")
def admin():
    return redirect(url_for("user",name="Admin! test"))

@app.route("/<something>")
def homepage():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)