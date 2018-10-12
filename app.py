from flask import Flask, g
from flask_restless import APIManager
from flask_login import LoginManager, current_user
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
from config import Configuration

app = Flask(__name__)
app.config.from_object(Configuration)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)
login_manager = LoginManager(app)
login_manager.login_view = "login"
bcrypt = Bcrypt(app)
api = APIManager(app, flask_sqlalchemy_db=db)


@app.before_request
def _before_request():
    g.user = current_user
