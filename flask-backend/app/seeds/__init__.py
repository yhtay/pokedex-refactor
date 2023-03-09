from flask.cli import AppGroup
from .pokemon import seed_pokemon, undo_pokemon

seed_commands = AppGroup('seed')

@seed_commands.command('all')
def seed():
    pokemon = seed_pokemon()
    print('Pokemon seeded successfully')
