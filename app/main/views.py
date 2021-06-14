from . import main
from flask import render_template,redirect, url_for,abort
from flask_login import login_required, current_user
from .forms import PitchForm,CommentsForm
from ..models import Pitches,Comments,User
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
        return redirect(url_for('main.single_pitch'))
    else: 
        all_pitches= Pitches.query.order_by(Pitches.posted).all()
       
        
    return render_template('newpitch.html',pitch_form= form, pitches=all_pitches)

@main.route('/pitch', methods=['POST','GET']) 
@login_required
def single_pitch():
    """get single  pitch"""
   
    commentform= CommentsForm()
    if commentform.validate_on_submit():
            new_comment= commentform.comment.data
            user_id = current_user._get_current_object().id
            pitch_id = current_user._get_current_object().id
            # pitch_id=Pitches.query.get(Pitches.id)
            new_comment= Comments(comment=new_comment,user_id=user_id,pitch_id=pitch_id)
            new_comment.save_comment()
            db.session.add(new_comment)
            db.session.commit()
            return redirect(url_for('main.single_pitch'))
    else:

        all_pitches= Pitches.query.order_by(Pitches.posted).all()
        comments=Comments.query.order_by(Comments.comment).all()
        
    
    return render_template('pitch.html', pitches=all_pitches,commentform=commentform,comments=comments)

# @main.route('/profile',methods=['POST','GET'])
# def profile():
    
