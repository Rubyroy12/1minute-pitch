from . import main
from flask import render_template,redirect, url_for,abort
from flask_login import login_required, current_user
from .forms import PitchForm
from ..models import Pitches

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/newpitch', methods = ['POST','GET'])
@login_required
def new_pitch():
    """create a new pitch"""
    form = PitchForm()
    if form.validate_on_submit():
        title = form.title.data
        category = form.category.data
        description = form.description.data
        
        new_pitch = Pitches(title=title, category=category, description=description)

        new_pitch.save_pitches()
        return redirect(url_for('main.index'))
    return render_template('newpitch.html',pitch_form= form)

@main.route('/<int:id>')
@login_required
def single_pitch(id):
    """get single  pitch"""
    pitch=Pitches.query.get(id)
    if pitch is None:
        abort(404)
    return redirect(url_for('main.pitch',pitch=pitch))