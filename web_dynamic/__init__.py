from flask import Flask, session
#import sqlalchemy
#from flask_cors import CORS
#from flask_session import Session
 



def createApp():
    app = Flask(__name__)
    # app.config["SESSION_PERMANENT"] = False
    # app.config["SESSION_TYPE"] = "filesystem"

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/auth/")

    return app