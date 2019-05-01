import yaml
import os

name = "minimaldb"


class MinimalDB(object):
    def __init__(self, path):
        self.path = os.path.expanduser(path)
        self.db = {}
        self.load(self.path)

    def load(self, path):
        if os.path.exists(path):
            return self.__load(path)
        else:
            return False

    def __load(self, path):
        try:
            with open(path, "r") as stream:
                self.db = yaml.load(stream)
                return True
        except Exception as e:
            print(f"Problem to open db with path: {path}")
            return False

    def __dump_db(self):
        try:
            with open(self.path, "w+") as stream:
                yaml.dump(self.db, stream)
                return True
        except Exception as e:
            print(f"Problem to save the db with path: {self.path}")
            return False

    def set(self, key, value):
        """
        Sets a value in the database

        :param key: <str> Key name
        :param value: Value to set
        """

        try:
            self.db[str(key)] = value
            self.__dump_db()
            return True
        except Exception as e:
            print(f"Error while saving values: {e}")
            return False

    def get(self, key):
        """
        Gets and returns a value from the database

        :param key: <str> Key name to get value of
        """

        try:
            return self.db[key]
        except KeyError:
            print(f"Error no key found: {key}")
            return False

    def delete(self, key):
        """
        Deletes a key from the database

        :param key: <str> Key name to delete from database
        """

        if key not in self.db:
            return False
        del self.db[key]
        self.__dump_db()
        return True
