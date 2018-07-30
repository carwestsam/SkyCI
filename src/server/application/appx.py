from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
cwd = os.getcwd()
static_path = os.path.realpath(os.path.join(cwd , '../web'))
print('static_path', static_path)

if __name__ == "__main__":
    app = Flask(__name__, static_url_path='', static_folder=static_path)
else:
    app = Flask(__name__)

CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres:123456@localhost:5433/postgres'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

