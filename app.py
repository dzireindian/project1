import os
import sys

from flask import Flask,render_template,request,session
from flask_session import Session

# from flask.ext.session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from werkzeug.debug import DebuggedApplication

# def load_config(mode):
#     """Load config."""
#     try:
#         if mode == 'PRODUCTION':
#             from .production import ProductionConfig
#             return ProductionConfig
#         elif mode == 'TESTING':
#             from .testing import TestingConfig
#             return TestingConfig
#         else:
#             from .development import DevelopmentConfig
#             return DevelopmentConfig
#     except ImportError:
#         from .default import Config
#         return Config

# config = load_config(mode=os.environ.get('FLASK_ENV'))
app = Flask(__name__)
# app.debug = True
# app.config.from_object(os.environ.get('FLASK_ENV'))
# if app.debug:
#     app.wsgi_app = DebuggedApplication(app.wsgi_app, evalex=True)


# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config['development'] = True
Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
# engine = create_engine("postgres://lcrwacesatfmjm:7775a710b16c87a20154bc9df86aceb643b9cc6afbb29c781bc068f25f19df21@ec2-54-247-71-245.eu-west-1.compute.amazonaws.com:5432/d6r9sefsl5m5i3")
db = scoped_session(sessionmaker(bind=engine))


@app.route("/")
def index():
    return "Project 1: TODO"

app.run(debug=True)

@app.route("/register")
def register():
     return render_template('register.html',path='./static/css/styles.min.css')

app.run(debug=True)

@app.route("/registration",methods=["POST"])
def registration():
    fname=request.form.get("first_name")
    lname=request.form.get("last_name")
    email=request.form.get("email")
    password=request.form.get("password")
    print(email+" , "+fname+" , "+lname)
    # print(email+" , "+fname+" , "+lname, file=sys.stderr)
    return email+" , "+fname+" , "+lname

app.run(debug=True)
