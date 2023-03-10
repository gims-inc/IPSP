import models
from models.notification import Notification
from models.provider_service import ProviderService
from models.region import Region
from models.review import Review
from models.service_request import   ServiceRequest
from models .service_category import ServiceCategory
from models.town import Town
from models.user import User

import sqlalchemy
from models.base_model import BaseModel, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

#classes = {}

classes = {"ServiceRequest": ServiceRequest, "Town": Town,"Region": Region,
           "Review": Review, "User": User,"Notification":Notification,"ProviderService":ProviderService,
           "ServiceCategory":ServiceCategory}


class DBStorage:
    """interaacts with the MySQL database"""
    __engine = None
    __session = None

    def __init__(self):
        """Instantiate a DBStorage object"""
        MYSQL_USER = 'inperson'
        MYSQL_PWD = 'Development_200'
        MYSQL_HOST = 'localhost'
        MYSQL_DB = 'in_person_db'
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(MYSQL_USER,
                                             MYSQL_PWD,
                                             MYSQL_HOST,
                                             MYSQL_DB))
        # if APP_ENV == "test":
        #     Base.metadata.drop_all(self.__engine)
    def all(self, cls=None):
        """query on the current database session"""
        new_dict = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
        return (new_dict)

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    # def edit(self,cls,id):
    #     self.__session.

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """reloads data from the database"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session

    def close(self):
        """call remove() method on the private session attribute"""
        self.__session.remove()

    def get(self, cls, id):
        """
        Returns the object based on the class name and its ID, or
        None if not found
        """
        if cls not in classes.values():
            return None

        all_cls = models.storage.all(cls)
        for value in all_cls.values():
            if (value.id == id):
                return value

        return None
    
    def get_user(self, email):
        """
        Returns the object based on the class name and its email, or
        None if not found
        """
        user_dict = models.storage.all(User)
        for value in user_dict.values():
            if (value.email == email):
                return value

    def count(self, cls=None):
        """
        count the number of objects in storage
        """
        all_class = classes.values()

        if not cls:
            count = 0
            for clas in all_class:
                count += len(models.storage.all(clas).values())
        else:
            count = len(models.storage.all(cls).values())

        return count