#############
#
#
#
#
#############

from flask import render_template
from app import app


@app.route('/')
@app.route('/home')
def index():
    user = {'nickname': 'Matthew'}  # prototype user
    return render_template('home.html',
                           title='Home',
                           user=user)
