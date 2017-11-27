########
# This script simply creates the application object (of class Flask) and then imports the views module,
# which we haven't written yet. Do not confuse app the variable (which gets assigned the Flask instance)
# with app the package (from which we import the views module).
#
# https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world
########

from flask import Flask

app = Flask(__name__)
from app import views