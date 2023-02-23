from flask import Blueprint, render_template
import  uuid


auth = Blueprint('auth',__name__)

# @auth.route('/register')
# def register():
#     return "<h1>register</h1>"


@auth.route('/login', strict_slashes=False)
def login():
     return render_template('login.html',cache_id=uuid.uuid4())


@auth.route('/logout')
def logout():
    return "/home"