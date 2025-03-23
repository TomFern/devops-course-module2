# A simple in-memory "database"
database = {}

def store_value(key, value):
    database[key] = value

def get_value(key):
    return database.get(key)
