from sqlalchemy import create_engine
from sqlalchemy import text

class PlaceTable:
    __scripts = {
        "select": "select * from places",
        "delete by id": text("delete from places where place_id =:id"),
        "insert new": text("INSERT INTO places (place_id, place_name) VALUES (:new_id, :new_name)"),
        "update": text("UPDATE places SET place_size = (:size) WHERE place_id = :id")
    }

    def __init__(self, connection_string):
        self.__db = create_engine(connection_string)

    def get_places(self):
        connection = self.__db.connect()
        result = connection.execute(text(self.__scripts["select"]))
        return result.fetchall()

    def new_insert(self, new_id, name ):
        connection = self.__db.connect()
        transaction = connection.begin()
        connection.execute(self.__scripts["insert new"], {'new_id': new_id, 'new_name': name})
        transaction.commit()


    def delete(self, delete_id):
        connection = self.__db.connect()
        transaction = connection.begin()
        connection.execute(self.__scripts["delete by id"], {'id': delete_id})
        transaction.commit()
        connection.close()


    def update(self,new_size, update_id):
        connection = self.__db.connect()
        transaction = connection.begin()
        connection.execute(self.__scripts["update"], {'size': new_size, 'id': update_id})
        transaction.commit()
        connection.close()
