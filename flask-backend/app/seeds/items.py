from app.models import db, Item
from faker import Faker
from random import choice
from sqlalchemy.sql import text

faker = Faker()


def seed_items():
    lst = list(range(1, 11))
    images = [
        "/images/pokemon_berry.svg",
        "/images/pokemon_egg.svg",
        "/images/pokemon_potion.svg",
        "/images/pokemon_super_potion.svg",
    ]
    for num in lst:
        temp = Item(
            name=faker.text(),
            price=str(choice(lst) * 2),
            happiness=str(choice(lst) * 6),
            image_url=choice(images),
            pokemon_id = num
        )
        db.session.add(temp)
    db.session.commit()


def undo_items():
    db.session.execute(text("DELETE FROM items"))
    db.session.commit()
