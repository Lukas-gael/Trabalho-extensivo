from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/reciclagem")
def reciclagem():
    return render_template("reciclagem.html")


@app.route("/suporte")
def suporte():
    return render_template("suporte.html")

@app.route("/mapaReciclagem")
def mapaReciclagem():
    return render_template("mapaReciclagem.html")


if __name__ == "__main__":
    app.run(debug=True)
