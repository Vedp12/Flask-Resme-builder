from flask import Flask, render_template, request, redirect, url_for
from templates.models import Header_model,Description_model,Project_model,Work_model,web_link_model
from templates.models import db


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
        
        return redirect(url_for("Template", header_id=Resume_header.Template_id))
    
    return render_template("detail.html")



@app.route("/Template/<int:header_id>",methods = ["GET","POST"])
def Template(header_id):
    headers = Header_model.query.get_or_404(header_id)
    if request.method == "POST":
        User_Description = request.form["User_Description"]
        Resume_description = Description_model(
        User_Description = User_Description
        )
        db.session.add(Resume_description)
        db.session.commit()
        return redirect(url_for("body_temp",header_id=Resume_description.description_id))
    return render_template("template_body.html", headers=headers)




@app.route("/Template_body/<int:header_id>",methods = ["GET","POST"])
def body_temp(header_id):
    headers = Description_model.query.get_or_404(header_id)
    if request.method == "POST":
        Project_name1 = request.form["Project_name1"]
        Project_name2 = request.form["Project_name2"]
        Project_description1 = request.form["Project_description1"]
        Project_description2 = request.form["Project_description2"]
        
        Resume_project = Project_model(
            Project_name1 = Project_name1,
            Project_name2 = Project_name2,
            Project_description1 = Project_description1,
            Project_description2 = Project_description2
        )
        db.session.add(Resume_project)
        db.session.commit()
        return redirect(url_for("work_template",header_id= Resume_project.project_id))
    return render_template("body_temp.html",headers=headers)



@app.route("/temp_data/<int:header_id>",methods = ["GET","POST"])
def work_template(header_id):
    headers = Description_model.query.get_or_404(header_id)

    if request.method == "POST":
        Work_name1 = request.form["Work_name1"]
        Work_name2 = request.form["Work_name2"]
        Work_description1 = request.form["Work_description1"]
        Work_description2 = request.form["Work_description2"]
        
        Resume_Work = Work_model(
        Work_name1 = Work_name1,
        Work_name2 = Work_name2,
        Work_description1 = Work_description1,
        Work_description2 = Work_description2
        )
        db.session.add(Resume_Work)
        db.session.commit()
        return redirect(url_for("link_template",header_id = Resume_Work.Work_id))
    return render_template("workdetail_template.html",headers=headers)



@app.route("/link_template/<int:header_id>",methods = ["GET","POST"])
def link_template(header_id):
    headers = Work_model.query.get_or_404(header_id)   
    if request.method == "POST":
         web_link1 = request.form["web_link1"]
         web_link2 = request.form["web_link2"]
         web_link3 = request.form["web_link3"]
         
         Resume_links = web_link_model(
            web_link1 = web_link1,
            web_link2 = web_link2,
            web_link3 = web_link3
         )
         db.session.add(Resume_links)
         db.session.commit()
         return redirect(url_for("main_page",header_id = Resume_links.web_link_id))
    return render_template("link_temp.html",headers=headers)


@app.route("/main/<int:header_id>",methods = ["GET","POST"])
def main_page(header_id):
    Header= Header_model.query.get_or_404(header_id)
    Description= Description_model.query.get_or_404(header_id)
    Project= Project_model.query.get_or_404(header_id)
    Work= Work_model.query.get_or_404(header_id)
    web_link= web_link_model.query.get_or_404(header_id)
    return render_template("main.html",
                           Header = Header,
                           Description = Description,
                           Project = Project,
                           Work = Work,
                           web_link = web_link,
                           )
if __name__ == "__main__":
    app.run(debug=True, port=8001)