from flask import Blueprint


auth = Blueprint('auth',__name__)

@auth.route('/register')
def register():
    return "<h1>register</h1>"


@auth.route('/login')
def login():
    return "<h1>login</h1>"


@auth.route('/logout')
def logout():
    return "/home"