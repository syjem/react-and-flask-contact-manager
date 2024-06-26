from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from flask_migrate import Migrate

from config import Config
from models import db
from routes.contacts import Contacts
from routes.favorite_contacts import FavoriteContacts

app = Flask(__name__)
CORS(app)

app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app, db)

api = Api(app)

api.add_resource(Contacts, '/contacts', '/contact/<int:contact_id>')
api.add_resource(FavoriteContacts, '/contacts/favorites')

if __name__ == '__main__':
    app.run(debug=True)
