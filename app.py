import os

from flask import Flask, session
from flask_session import Session
# from flask.ext.session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
# engine = create_engine("postgres://lcrwacesatfmjm:7775a710b16c87a20154bc9df86aceb643b9cc6afbb29c781bc068f25f19df21@ec2-54-247-71-245.eu-west-1.compute.amazonaws.com:5432/d6r9sefsl5m5i3")
db = scoped_session(sessionmaker(bind=engine))


@app.route("/")
def index():
    return "Project 1: TODO"
