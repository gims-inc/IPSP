from flask import Blueprint,  render_template
import uuid

views = Blueprint('views',__name__)

@views.route('/home',strict_slashes=False)
def home():
    return render_template('home.html',cache_id=uuid.uuid4())
