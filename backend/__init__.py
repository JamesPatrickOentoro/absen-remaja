from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from os import path
import os

db = SQLAlchemy()
DB_NAME = "rmj_db"


def run_npm_serve():
    print("Running npm serve function...")
    current_dir = os.path.dirname(os.path.abspath('frontend'))
    frontend_dir = os.path.join(current_dir, 'absent-project','frontend')
    if not os.path.isdir(frontend_dir):
        print(f"Error: Directory '{frontend_dir}' not found.")
    os.chdir(frontend_dir)
    return os.system('npm run serve')

def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config['SECRET_KEY'] = 'kersos'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://root@localhost:3306/{DB_NAME}'
   
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import Jemaat, Absen, Admin

    create_database(app)

    return app


def create_database(app):
    with app.app_context():
        if not path.exists('backend/' + DB_NAME):
            db.create_all()
            print('Database Created!')
