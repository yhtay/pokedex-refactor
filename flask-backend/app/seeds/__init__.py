from flask.cli import AppGroup
from .pokemon import seed_pokemon, undo_pokemon
from .items import seed_items, undo_items

seed_commands = AppGroup('seed')

@seed_commands.command('all')
def seed():
    pokemon = seed_pokemon()
    items = seed_items()
    print('Pokemon & Items seeded successfully')

@seed_commands.command('undo')
def undo_seed():
    undo_pokemon()
    undo_items()
    print("Pokemon & Items seeds undone")
