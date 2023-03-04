from flask import Blueprint, render_template,session,redirect,url_for,flash,request,jsonify
import uuid
from models import storage
from models.user import User
from models.service_category import ServiceCategory
from models.town import Town
from models.region import Region

views = Blueprint('views',__name__)


@views.route('/home',strict_slashes=False)
@views.route('/home/<string:id>',strict_slashes=False,methods=['GET','POST'])
def home(id=None):

    users = storage.all('User').values()
    #print(users)

    regions = storage.all(Region).values()
    regions = sorted(regions, key=lambda k:k.name)
    region_town=[]

    for region in regions:
        region_town.append([region, sorted(region.towns, key=lambda k: k.name)])

    categories = storage.all(ServiceCategory).values()
    categories = sorted(categories, key=lambda k:k.category_name)
    #print(categories)

    


    return render_template('home.html',cache_id=uuid.uuid4(),
                           users=users,
                           regions=region_town,
                           categories=categories)


@views.route('/profile_view/<string:id>',strict_slashes=False)
def profile_view(id):
    if not id:
        return
    else:
        user = storage.get(User,id)

        return render_template('view_profile.html',user=user,
                           cache_id=uuid.uuid4())                                             


@views.route('/edit_profile/<string:id>',strict_slashes=False,methods=['GET','POST','PUT'])
def profile_edit(id):
    
    user = storage.get(User,id)

    if request.method == 'POST' and 'save' in request.form:
        name = request.form.get('full_name')
        username = request.form.get('username')
        # email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirmpassword')
        phone = request.form.get('phone')
        avatar = request.form.get('dp')
        address = request.form.get('address')
        town = request.form.get('town')
        region = request.form.get('region')
        skill = request.form.get('skill')
        gender = request.form.get('gender')
        bio = request.form.get('about')
        longitude = request.form.get('longitude')
        latitude = request.form.get('latitude')
        country = request.form.get('country')

        if password != confirm_password:
            flash("Your passwords do not match!",category="error")
        else:
            ignore = ['id', 'email', 'created_at', 'updated_at']

            edited_user = User(full_name=name,user_name=username,password=password,phone=phone,dp=avatar,
                               adress=address,town=town,region=region,skill=skill,gender=gender,about=bio,
                               longitude=longitude,latitude=latitude,country=country)
            
            data = edited_user.to_dict()
            for key, value in data.items():
                if key not in ignore:
                    try:
                        setattr(user, key, value)
                    except Exception:
                        pass
                    finally:
                        storage.save()
            return redirect(f'/profile_user/{user.id}')
        

    if not id:
        flash('You have to login first',category='error')
        return redirect('/auth.login')
    else:
        return render_template('edit_profile.html',user=user,
                           cache_id=uuid.uuid4())                                             


#@views.route('/profile_user',strict_slashes=False)
@views.route('/profile_user/<string:id>',strict_slashes=False)
def profile_user(id=None):
    if id == None:
        return redirect(url_for('/auth/login'),200)
    else:
        user = storage.get(User,id)
    
        return render_template('user_profile.html',user=user,
                           cache_id=uuid.uuid4())
    

@views.route('/request_service/<string:id>',strict_slashes=False, methods=['GET','POST'])
def request_service(id):
    if session['userId'] == "" or session['userId'] == None:
        flash('Kindly login first!')
        return redirect(url_for('auth.login'),200)
    else:
        requester_id = session['userId']
        return render_template('request.html',providerId=id,
                            requesterId =requester_id,
                           cache_id=uuid.uuid4())


@views.route('/accept_request/<string:id>',strict_slashes=False, methods=['GET','POST'])
def accept_request(id):
    

    return render_template('accept_request.html',providerId=id,
                           cache_id=uuid.uuid4())


@views.route('/decline_request/<string:id>',strict_slashes=False, methods=['GET','POST'])
def decline_request(id):

    return render_template('decline_request.html',providerId=id,
                           cache_id=uuid.uuid4())


@views.route('/our_story',strict_slashes=False)
def our_story():
    return render_template('about_us.html',cache_id=uuid.uuid4())


@views.route('/meet_the_team',strict_slashes=False)
def the_team():
    return render_template('the_team.html',cache_id=uuid.uuid4())