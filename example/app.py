from flask import Flask, render_template, request

app = Flask(__name__)

# Sample data (replace with your resume data)
resume_data = {
    "name": "Ved Patel",
    "skills": ["Python", "Flask", "HTML/CSS"],
    "experience": ["Software Developer at XYZ (2022-Present)"]
}

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        selected_template = request.form.get("template")
        return render_template(f"template{selected_template}.html", **resume_data)
    return render_template("index.html")  # A page to select templates

if __name__ == "__main__":
    app.run(debug=True)
