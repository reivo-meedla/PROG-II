def is_singleton(factory):
    obj1 = factory()
    obj2 = factory()
    return obj1 is obj2


class Database:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance


def create_db():
    return Database()


class User:
    pass


def create_user():
    return User()


print(is_singleton(create_db))
print(is_singleton(create_user))