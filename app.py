from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_alembic import Alembic


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.sqlite3"
db = SQLAlchemy(app)
alembic = Alembic(app)


class TestModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
