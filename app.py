from flask import Flask, render_template, request, redirect, abort

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("Template.html")

if __name__ == "__main__":
    app.run(debug=True, port=8001)