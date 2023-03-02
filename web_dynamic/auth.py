from flask import  Flask, request, flash
from flask import Blueprint, render_template, flash, session,redirect,url_for
import  uuid
from models import storage
from models.user import User
from . import views
from utils.email_verify import isValid

auth = Blueprint('auth',__name__)


@auth.route('/login', strict_slashes=False, methods=['GET','POST'])
def login():
     if request.method == 'POST' and 'login' in request.form:
          email = request.form.get('email')
          password = request.form.get('password')

          if email == "":
               flash("Kindly provide a valid email and password!",category="error")
          elif isValid(email) == False:
               flash("Check your email!",category="error")
          else:
               user = storage.get_user(email)

               if  not user:
                    flash("Kindly click on the register tab and sign up or provide valid emal and password!",category="error")
                    return redirect('/auth/register')
          
               else:
                    userid = user.id
                    session['islogin'] = "logged_in"
                    session['userId'] = userid
                    session['username'] = user.user_name
                    username = user.user_name

          
          
          
                    flash('login sucessfull!', category='success')
                    return redirect(f'/home/{userid}')
          #return redirect(url_for('home'))

     return render_template('login.html',cache_id=uuid.uuid4())


@auth.route('/register', strict_slashes=False, methods=['GET','POST'])
def register():
     if request.method == 'POST' and 'register' in request.form:
          name = request.form.get('registerName')
          username = request.form.get('registerUsername')
          email = request.form.get('registerEmail')
          password = request.form.get('registerPassword')
          confirm_password = request.form.get('confirmpassword')

          user = storage.get_user(email)

          if password != confirm_password:
               flash("Your passwords don\'t seem to match!",category='error')
          elif name == "" and username == "" and email == "" and password == "":
               flash("Kindly fill all fields!",category="error")
          elif user != None:
               flash("The email alreay exits!",category="error")
          elif isValid(email) == False:
               flash("Kindly provied a valid email!", category="error")
          else:
               new_user = User(email=email,password=password,user_name=username,full_name=name)

               storage.new(new_user)
               storage.save()
               flash('User created successfully!',category="success")

               #render_template('login.html',cache_id=uuid.uuid4())
               return redirect('/auth/login')
          
          

     return render_template('login.html',cache_id=uuid.uuid4())


@auth.route('/logout',strict_slashes=False,methods=['GET'])
def logout():
    session['islogin'] = ""
    session['userId'] = ""
    session['username'] = ""

    #flash("logged out", category='success') 

    return redirect('/home')