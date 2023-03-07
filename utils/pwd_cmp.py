from models.user import  User
from models import storage
from hashlib import md5


def isPassword(pwd,id):
    pwd = md5(pwd.encode()).hexdigest()
    user = storage.get(User,id)
    if pwd ==  user.password:
        return True
    return False