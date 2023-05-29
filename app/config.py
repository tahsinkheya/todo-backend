import os
class BaseConfig:
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_$ecReT_KeY')
    
