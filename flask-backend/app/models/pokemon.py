from .db import db
from datetime import datetime

class Pokemon(db.Model):

    __tablename__ = "pokemon"

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    number = db.Column(db.Integer, nullable=False, unique=True)
    attack = db.Column(db.Integer, nullable=False)
    defense = db.Column(db.Integer, nullable=False)
    image_URL = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(255), nullable=False, unique=True)
    type = db.Column(db.String(255), nullable=False)
    moves = db.Column(db.String(255), nullable=False)
    encouter_rate =  db.Column(db.Float(3, 2), nullable=False, default=1.00)
    catch_rate = db.Column(db.Float(3, 2), nullable=False, default=1.00)
    captured = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.Date, default=datetime.utcnow)
