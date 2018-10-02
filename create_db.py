import os
import sys
from main import db

sys.path.append(os.getcwd())


if __name__ == '__main__':
    db.create_all()
