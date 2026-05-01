from flask import Flask, render_template, request, redirect, url_for
from templates.models import db, Header_model

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///Resume.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/detail", methods=["GET", "POST"])
def detail():
    if request.method == "POST":
        Full_name = request.form["Full_name"]
        email = request.form["email"]
        phone = request.form["phone"]
        address = request.form["address"]  
        
        Resume_header = Header_model(
            Full_name=Full_name,
            email=email,
            phone=phone,
            address=address  
        )
        db.session.add(Resume_header)
        db.session.commit()
        
        # Use Template_id (the primary key from your model)
        # return redirect(url_for("Template", header_id=Resume_header.Template_id))
        return redirect(url_for("Template", header_id=Resume_header.Template_id))
    
    return render_template("detail.html")

@app.route("/Template/<int:header_id>")
def Template(header_id):
    headers = Header_model.query.get_or_404(header_id)
    return render_template("template_body.html", headers=headers)

@app.route("/app")
def index():
    return render_template("index1.html")

if __name__ == "__main__":
    app.run(debug=True, port=8001)