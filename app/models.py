from app import db


class User(db.Model):
    __tablename__ = 'users'

    id= db.Column(db.Integer, primary_key=True)
    username= db.Column(db.String(255))
    email = db.Column(db.String(255),unique=True)
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


class roles(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    