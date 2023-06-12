import os
class BaseConfig:
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_$ecReT_KeY')
    MONGO_SERVER_NAME = os.getenv("MONGO_SERVER_NAME", "localhost")
    MONGO_USER_NAME = os.environ.get('MONGO_USER_NAME','admin')
    MONGO_PASSWORD = os.environ.get('MONGO_PASSWORD','123456789')
    MONGO_URI = "mongodb://"+MONGO_USER_NAME+":"+MONGO_PASSWORD+"@"+MONGO_SERVER_NAME + \
        ":27017/test-db?authSource=admin"
    print(MONGO_URI)
    # MONGO_URI = 'mongodb://localhost:27017'

