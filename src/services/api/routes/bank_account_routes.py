from flask import Blueprint, jsonify

routes = Blueprint("bank_routes", __name__)

@routes.route("/bank/register", methods=["GET"])
def register_user():
