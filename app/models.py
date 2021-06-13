from app import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class Pitch:
    """class pitch that defines all the class objects"""
    pass
class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id= db.Column(db.Integer, primary_key=True)
    username= db.Column(db.String(255))
    email = db.Column(db.String(255),unique=True)
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    pitches = db.relationship('Pitches',backref = 'user',lazy = "dynamic")
    password_hash = db.Column(db.String(255))
    pass_secure= db.Column(db.String(255))

    @property
    def password(self):
            raise AttributeError('You cannot read the passwordattribute')
    @password.setter
    def password(self,password):
            self.pass_secure=generate_password_hash(password=password)

    def verify_password(self,password):
            return check_password_hash(self.pass_secure,password)

    def __repr__(self):
            return f'User {self.username}'


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    users = db.relationship('User',backref = 'role',lazy="dynamic")

    def __repr__(self):
        return f'User {self.name}'


class Pitches:
    """
    Class that defines class objects
    """
    all_pitches=[]
    
    def __init__(self,id,title,category,description):
        self.id = id
        self.title = title
        self.category = category
        self.description = description

    def save_pitches(self):
        """save pitches"""
        Pitches.all_pitches.append(self)
    @classmethod
    def get_pitches(cls,id):
        response=[]
        for pitch in cls.all_pitches:
            response.append(pitch)


        return response


class Pitches(db.Model):

    __tablename__= 'pitches'
    id = db.Column(db.Integer, primary_key=True)
    pitch_id = db.Column(db.Integer)
    title = db.Column(db.String(255))
    category =db.Column(db.String(255))
    description = db.Column(db.String(255))
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))


    def save_pitches(self):
        db.session.add(self)
        db.session.commit()
    @classmethod
    def get_pitches(cls,id):
        pitches =Pitches.query.filter_by(pitch_id=id).all()
        return pitches


