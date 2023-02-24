from flask import Blueprint, render_template, request, flash
import  uuid


auth = Blueprint('auth',__name__)


@auth.route('/register', strict_slashes=False, methods=['GET','POST'])
def register():
     if request.method == 'POST':
          email = request.form.get('email')
          password = request.form.get('password') 

          flash('login sucessfull', category='success')
     return render_template('login.html',cache_id=uuid.uuid4())


@auth.route('/login', strict_slashes=False, methods=['GET','POST'])
def login():
     if request.method == 'POST':
          name = request.form.get('registerName')
          username = request.form.get('registerUsername')
          email = request.form.get('registerEmail')
          password = request.form.get('registerPassword')
          confirm_password = request.form.get('confirmpassword')

          if password != confirm_password:
               flash("Your passwords don\'t seem to match!",category='error')

     return render_template('login.html',cache_id=uuid.uuid4())


@auth.route('/logout',strict_slashes=False,methods=['GET'])
def logout():
    return "/home"