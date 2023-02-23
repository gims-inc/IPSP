from flask import Blueprint,  render_template
import uuid

views = Blueprint('views',__name__)

@views.route('/home',strict_slashes=False)
def home():
    return render_template('home.html',cache_id=uuid.uuid4())


@views.route('/profile_view',strict_slashes=False)
def profile_view():
    return render_template('view_profile.html',cache_id=uuid.uuid4())


@views.route('/profile_user',strict_slashes=False)
def profile_user():
    return render_template('user_profile.html',cache_id=uuid.uuid4())

