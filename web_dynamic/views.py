from flask import Blueprint,  render_template
import uuid
from models import storage
from models.user import User

views = Blueprint('views',__name__)

@views.route('/home',strict_slashes=False)
def home():
    users = storage.all(User.email)
    print(users)
    return render_template('home.html',cache_id=uuid.uuid4())


@views.route('/profile_view',strict_slashes=False)
def profile_view(id):
    return render_template('view_profile.html/<string:id>',userId=id,cache_id=uuid.uuid4())


@views.route('/profile_user/<string:id>',strict_slashes=False)
def profile_user(id):
    return render_template('user_profile.html',userId=id,cache_id=uuid.uuid4())

