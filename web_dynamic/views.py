from flask import Blueprint, render_template, sessions, redirect,url_for
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


#@views.route('/profile_user',strict_slashes=False)
@views.route('/profile_user/<string:id>',strict_slashes=False)
def profile_user(id=None):
    if id == None:
        redirect(url_for('/auth/login'),200)
    else:
        user = storage.get(User,id)
    
        return render_template('user_profile.html',user=user,
                           cache_id=uuid.uuid4())
    

@views.route('/request_service/<string:id>',strict_slashes=False)
def request_service(id):

    return render_template('request.html',providerId=id,
                           cache_id=uuid.uuid4())

