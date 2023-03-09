from .db import db
from datetime import datetime

class Pokemon(db.Model):

    __tablename__ = "pokemons"

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    number = db.Column(db.Integer, nullable=False, unique=True)
    attack = db.Column(db.Integer, nullable=False)
    defense = db.Column(db.Integer, nullable=False)
    imageURL = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(255), nullable=False, unique=True)
    type = db.Column(db.String(255), nullable=False)
    moves = db.Column(db.String(255), nullable=False)
    encouterRate =  db.Column(db.Float(3, 2), nullable=False, default=1.00)
    catchRate = db.Column(db.Float(3, 2), nullable=False, default=1.00)
    captured = db.Column(db.Boolean, default=False)
    date = db.Column(db.Date, default=datetime.utcnow)
