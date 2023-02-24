
storage_t = 'db'

from models.database.db import DBStorage
storage = DBStorage()

storage.reload()