# -*- coding: utf-8 -*-
"""
    Flaskr: a microblog example application.
"""

from flask import Flask
from flask.ext.mongoengine import MongoEngine

app = Flask(__name__)
app.config.from_object('config')

db = MongoEngine(app)

def register_blueprints(app):
    # Prevents circular imports
    from flaskr.views import posts
    from flaskr.admin import admin
    app.register_blueprint(posts)
    app.register_blueprint(admin)

register_blueprints(app)

if __name__ == '__main__':
    app.run()
