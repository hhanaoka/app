import os


class Configuration:
    APPLICATION_DIR = ''  # os.path.dirname(os.path.realpath(__file__))
    DEBUG = True
    SECRET_KEY = 'flask is fun!'
    SQLALCHEMY_DATABASE_URI = (f'sqlite://{APPLICATION_DIR}/'
                               'blog.db?check_same_thread=False')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    STATIC_DIR = os.path.join(APPLICATION_DIR, 'static')
    IMAGES_DIR = os.path.join(STATIC_DIR, 'images')
