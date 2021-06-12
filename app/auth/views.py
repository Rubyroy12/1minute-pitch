from flask import render_template
from . import auth


@auth.route('/login')
def login():
    """user login"""

    return render_template('auth/login.html')

