
# import statement for CSRF
from flask import Flask, render_template, redirect
from flask_wtf.csrf import CSRFProtect, generate_csrf
from .models.db import db
from .config import Config
from flask_migrate import Migrate
from .seeds import seed_commands



app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
Migrate(app, db)

# Need to add the seed commands to our app
app.cli.add_command(seed_commands)
# after request code for CSRF token injection

@app.after_request
def inject_csrf_token(response):
    response.set_cookie(
        'csrf_token',
        generate_csrf(),
        secure=True if os.environ.get('FLASK_ENV') == 'production' else False,
        samesite='Strict' if os.environ.get(
            'FLASK_ENV') == 'production' else None,
        httponly=True)
    return response
