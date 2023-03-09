from ..models.pokemon import Pokemon
from ..models.item import Item
from ..models.db import db
from sqlalchemy.sql import text
from .pokemon_list import pokemon_list

def seed_pokemon():
    
    for pokemon in pokemon_list:
        pokemon_instance = Pokemon(**pokemon)
        db.session.add(pokemon_instance)
        db.session.commit()
    
def undo_pokemon():
    db.session.execute(text("DELETE FROM pokemon"))
    db.session.commit()
