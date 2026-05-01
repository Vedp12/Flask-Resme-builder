from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Header_model(db.Model):
    __tablename__ = "Resume_header_model"

    Template_id = db.Column(db.Integer,primary_key = True)
    Full_name = db.Column(db.String(),nullable=False) 
    email = db.Column(db.String(),nullable=False)
    phone = db.Column(db.BigInteger, nullable=False)
    address = db.Column(db.String(),nullable = False)   
    
    def __init__(
        self,
        Full_name,
        email,
        phone,
        address,
    ):
        self.Full_name = Full_name
        self.email = email
        self.phone = phone
        self.address = address

    def __repr__(self):
        return f"{ self.Full_name }, { self.email }, { self.phone }"