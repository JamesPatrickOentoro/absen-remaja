from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from os import path
import os

db = SQLAlchemy()
app = Flask(__name__)
DB_NAME = "rmj_db"


def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config['SECRET_KEY'] = 'kersos'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://root:@localhost:3306/{DB_NAME}'
   
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import Jemaat, Absen, Admin

    # create_database(app)

    return app
            
if __name__ == '__main__':
    # app = Flask(__name__)
    CORS(app)
    app.config['SECRET_KEY'] = 'kersos'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://root:@localhost:3306/{DB_NAME}'
   
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import Jemaat, Absen, Admin

    # create_database(app)
    app.run(debug=True)
    if not path.exists('backend/' + DB_NAME):
        db.create_all()
        print('Database Created!')

    # app.run()
    
