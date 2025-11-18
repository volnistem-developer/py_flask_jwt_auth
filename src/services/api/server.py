from flask import Flask

from src.infraestrutura.database import db_connection_handler
from src.services.api.routes.bank_account_routes import routes as bank_account_routes

db_connection_handler.connect()

app = Flask(__name__)

app.register_blueprint(bank_account_routes)
