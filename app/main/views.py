from . import main
from flask import render_template,redirect, url_for,abort
from flask_login import login_required, current_user
from .forms import PitchForm
from ..models import Pitches
from .. import db

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/newpitch', methods = ['POST','GET'])
@login_required
def newpitch():
    """create a new pitch"""
    form = PitchForm()
    if form.validate_on_submit():
        title = form.title.data
        category = form.category.data
        description = form.description.data
        
        new_pitch = Pitches(title=title, category=category, description=description)
        new_pitch.save_pitches()
        db.session.add(new_pitch)
        db.session.commit()
        return redirect(url_for('main.newpitch'))
    else: 
        all_pitches= Pitches.query.order_by(Pitches.posted).all()
    return render_template('newpitch.html',pitch_form= form, pitches=all_pitches)

# @main.route('/pitch/<int:id>', methods=['GET'])
# @login_required
# def single_pitch(id):
#     """get single  pitch"""
#     pitch=Pitches.query.get(id)
#     if pitch is None:
#         abort(404)
#     return render_template('pitch.html', pitch=pitch)