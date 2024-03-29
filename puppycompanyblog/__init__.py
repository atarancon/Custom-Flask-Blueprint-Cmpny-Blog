# puppycomapny/__init__.py
import os
from flask import Flask

#import for database 
from flask_sqlalchemy import SQLAlchemy

#import migrations 
from flask_migrate import Migrate
#lgin manager 
from flask_login import LoginManager



app = Flask(__name__)

#set secret key 
app.config['SECRET_KEY'] = os.urandom(16)

######################
######Database set up#########
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

db = SQLAlchemy(app)
Migrate(app,db)


################################
# LOGIN CONFIGS
login_manager = LoginManager()

login_manager.init_app(app)
#login view 
login_manager.login_view = 'users.login'



from puppycompanyblog.core.views import core
from puppycompanyblog.error_pages.handlers import error_pages
from puppycompanyblog.users.views import users
from puppycompanyblog.blog_posts.views import blog_posts

app.register_blueprint(error_pages)
app.register_blueprint(core)
app.register_blueprint(users)
app.register_blueprint(blog_posts)