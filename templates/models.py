from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Header_model(db.Model):
    __tablename__ = "Resume_header_model"

    Template_id = db.Column(db.Integer,primary_key = True)
    Full_name = db.Column(db.String(),nullable=False) 
    email = db.Column(db.String(),nullable=False)
    phone = db.Column(db.BigInteger, nullable=False)
    
    def __init__(
        self,
        Full_name,
        email,
        phone,
    ):
        self.Full_name = Full_name
        self.email = email
        self.phone = phone

    def __repr__(self):
        return f"{ self.Full_name }, { self.email }, { self.phone }"
    
class Description_model(db.Model):
    __tablename__ = "Resume_description_model"
    description_id = db.Column(db.Integer,primary_key = True)
    User_Description = db.Column(db.String(),nullable = False)
    skills1 = db.Column(db.String(),nullable = False)
    skills2 = db.Column(db.String(),nullable = False)
    skills3 = db.Column(db.String(),nullable = False)
    skills4 = db.Column(db.String(),nullable = False)
    def __init__(
        self,
        User_Description,
        skills1,        
        skills2,        
        skills3,        
        skills4   
    ):
        self.User_Description = User_Description
        self.skills1 = skills1
        self.skills2 = skills2
        self.skills3 = skills3
        self.skills4 = skills4 
    
class Project_model(db.Model):
    __tablename__ = "Project_model"
    project_id = db.Column(db.Integer,primary_key = True)
    Project_name1 = db.Column(db.String(),nullable = False)
    Project_name2 = db.Column(db.String(),nullable = False)
    Project_description1 = db.Column(db.String(),nullable = False)
    Project_description2 = db.Column(db.String(),nullable = False)
    
    def __init__(self,
                Project_description1,
                Project_description2,
                Project_name1,
                Project_name2,                 
                 ):
        self.Project_description1 =  Project_description1
        self.Project_description2 =  Project_description2
        self.Project_name1 =    Project_name1
        self.Project_name2 =    Project_name2
class Work_model(db.Model):
    __tablename__ = "Work_model"
    Work_id = db.Column(db.Integer,primary_key = True)
    Work_name1 = db.Column(db.String(),nullable = False)
    Work_name2 = db.Column(db.String(),nullable = False)
    Work_description1 = db.Column(db.String(),nullable = False)
    Work_description2 = db.Column(db.String(),nullable = False)
        
    def __init__(
        self,
        Work_name1,
        Work_name2,
        Work_description1,
        Work_description2,
    ):    
        self.Work_name1 = Work_name1
        self.Work_name2 = Work_name2
        self.Work_description1 = Work_description1
        self.Work_description2 = Work_description2
            

class web_link_model(db.Model):
    __tablename__ = "web_link_model"
    web_link_id = db.Column(db.Integer,primary_key = True)
    web_link1 = db.Column(db.String(),nullable = False)
    web_link2 = db.Column(db.String(),nullable = False)
    web_link3 = db.Column(db.String(),nullable = False)
    
    def __init__(
        self,
        web_link1,
        web_link2,
        web_link3,
    ):
        self.web_link1 = web_link1
        self.web_link2 = web_link2
        self.web_link3 = web_link3
    
