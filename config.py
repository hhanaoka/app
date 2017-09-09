import os


class Configuration:
    APPLICATION_DIR = os.path.dirname(os.path.realpath(__file__))
    DEBUG = True
    # SQLite objects created in a thread can only be used in that same thread.
    # -> add 'check_same_thread=False'
    database_uri_templ = 'sqlite:///{0}/blog.db?check_same_thread=False'
    SQLALCHEMY_DATABASE_URI = database_uri_templ.format(APPLICATION_DIR)
    # FSADeprecationWarning: SQLALCHEMY_TRACK_MODIFICATIONS adds significant
    # overhead and will be disabled by default in the future.
    # Set it to True or False to suppress this warning.
    SQLALCHEMY_TRACK_MODIFICATIONS = False
