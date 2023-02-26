from web_dynamic import createApp
from models import storage
import uuid


app = createApp()
app.secret_key = 'my_ap_secret_key'

@app.teardown_appcontext
def close_db(error):
    """ Remove the current SQLAlchemy Session """
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
