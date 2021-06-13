from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, SubmitField
from wtforms.validators import required


class PitchForm(FlaskForm):
    title = StringField('Pitch Title', validators=[required()])
    category = SelectField('Category', choices=[('PROGRAMMING','PROGRAMMING'), ('BUSINESS','BUSINESS'),('LOVE','LOVE')], validators=[required()])
    description= TextAreaField('Pitch Description', validators=[required()])
    submit = SubmitField('Upload')


